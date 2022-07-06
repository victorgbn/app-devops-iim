import json
from datetime import datetime
import os
import boto3
from botocore.exceptions import ClientError

def handler(event, context):
  print('received event:')
  print(event)

  try:
    if event['triggerSource'] != "PostConfirmation_ConfirmSignUp":
      raise ValueError("Error event")
    resource = boto3.resource('dynamodb')
    table_name = os.environ['STORAGE_USERS_NAME']
    table = resource.Table(table_name)
    create_user(table, event)
    return event
  except (Exception, ClientError) as error:
    print(error)

def create_user(table, event):
    currentDate = f'{str(datetime.now().isoformat())}Z'
    user = {
      'id' : event['request']['userAttributes']['sub'],
      'updateDate': currentDate,
      'analyses': []
    }
    table.put_item(Item=user)
