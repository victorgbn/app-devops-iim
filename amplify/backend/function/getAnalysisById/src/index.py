import json
import os

import boto3
from botocore.exceptions import ClientError


def handler(event, context):
    print('received event:')
    print(event)

    response = {
        'headers': {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
        }
    }
    pathParam = event['pathParameters']
    analysisId = pathParam['proxy']
    
    if analysisId is None or len(analysisId) <= 0:
      raise ValueError('Input error: analysisId')

    try:
      resource = boto3.resource('dynamodb')
      analysisTableName = os.environ['STORAGE_ANALYSE_NAME']
      analysisTable = resource.Table(analysisTableName)
      
      print('fetching Analysis with id ' + analysisId)
      analysis = getUserAnalysisById(analysisTable, analysisId)
      print(analysis)
      response['body'] = json.dumps({'analysis': analysis})
      response['statusCode'] = 200
    except (Exception, ClientError) as error:
      print(error)
      response['statusCode'] = 400
      response['body'] = json.dumps({'error': str(error)})
      
    return response
      
def getUserAnalysisById(analysisTable, analysisId):
    item_data = analysisTable.get_item(Key={'id': analysisId})
    return item_data['Item']
