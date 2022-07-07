import json
import os
from datetime import datetime
import boto3
from botocore.exceptions import ClientError
from utils import get_user_id

def handler(event, context):
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
        table_analyse_name = os.environ['STORAGE_ANALYSE_NAME']
        table_analyse = resource.Table(table_analyse_name)

        body = json.loads(event['body'])


        update_analyse(user_id, table_analyse, body)


        response['statusCode'] = 200
    except (Exception, ClientError) as error:
        print(error)
        response['statusCode'] = 400
        response['body'] = json.dumps({'error': str(error)})

    return response

def update_analyse(user_id, table, body ):

  analyse_id = body['analyse_id']
  title = body['title']
  description = body['description']
  currentDate = f'{str(datetime.now().isoformat())}Z'

  to_update = {
      ':tl' : title,
      ':des' : description,
      ':upd': currentDate,
      ':upb': user_id
    }

  expression = 'SET title = :tl, description = :des, updated_by = :upb, updated_date = :upd'

  table.update_item(
      Key={'id': analyse_id},
      UpdateExpression=expression,
      ExpressionAttributeValues=to_update
    )
