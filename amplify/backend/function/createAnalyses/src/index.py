import json
import os
import uuid
from datetime import datetime

import boto3
from botocore.exceptions import ClientError


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
        resource = boto3.resource('dynamodb')
        table_name = os.environ['STORAGE_ANALYSE_NAME']
        table = resource.Table(table_name)
        create_analyse(table)
        response['statusCode'] = 200
    except (Exception, ClientError) as error:
        response['statusCode'] = 400
        response['body'] = json.dumps({'error': str(error)})

    return response

def create_analyse(table):
    currentDate = f'{str(datetime.now().isoformat())}Z'
    analyse = {
        'id': str(uuid.uuid1()),
        'title': None,
        'description': None,
        'created_by': None,
        'updated_by': None,
        'creation_date': currentDate,
        'updated_date': currentDate,
        'transcript': None
    }
    table.put_item(Item=analyse)
