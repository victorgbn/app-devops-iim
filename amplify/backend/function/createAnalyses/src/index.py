import json
import os
import uuid
from datetime import datetime

import boto3
from botocore.exceptions import ClientError

from utils import get_user_id

def handler(event, context):
    print('received event:')
    print(event)

    response = {
        'headers': {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
        }
    }

    try:
        user_id = get_user_id(event)
        resource = boto3.resource('dynamodb')
        table_name = os.environ['STORAGE_ANALYSE_NAME']
        table_user_name = os.environ['STORAGE_USERS_NAME']

        table = resource.Table(table_name)
        table_user = resource.Table(table_user_name)

        analyse_id = create_analyse(table, user_id)
        update_user(user_id, table_user, analyse_id)
        response['body'] = json.dumps({'analyseId': analyse_id})
        response['statusCode'] = 200
    except (Exception, ClientError) as error:
        print(error)
        response['statusCode'] = 400
        response['body'] = json.dumps({'error': str(error)})

    return response

def create_analyse(table, user_id):
    currentDate = f'{str(datetime.now().isoformat())}Z'
    analyse = {
        'id': str(uuid.uuid1()),
        'title': None,
        'description': None,
        'created_by': user_id,
        'updated_by': user_id,
        'creation_date': currentDate,
        'updated_date': currentDate,
        'transcript': None,
    }
    table.put_item(Item=analyse)
    return analyse['id']

def update_user(user_id, table_user, analyse_id):
    currentDate = f'{str(datetime.now().isoformat())}Z'
    to_update = {
        ':al' : [{'id' : analyse_id}],
        ':upd' : currentDate
    }

    expression = 'SET analyses = list_append(analyses, :al), updateDate = :upd'

    table_user.update_item(
        Key={'id': user_id},
        UpdateExpression=expression,
        ExpressionAttributeValues=to_update
    )