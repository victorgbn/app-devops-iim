import json
import os

import boto3
from botocore.exceptions import ClientError
from utils import get_user_id


def handler(event, context):
    response = {
        'headers': {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
        }
    }

    try:
        userId = get_user_id(event)
        resource = boto3.resource('dynamodb')
        analysisTableName = os.environ['STORAGE_ANALYSE_NAME']
        usersTableName = os.environ['STORAGE_USERS_NAME']
        analysisTable = resource.Table(analysisTableName)
        usersTable = resource.Table(usersTableName)

        analysesIds = getUserColumn(usersTable, userId)
        analyseObjects = getUserAnalysisById(analysisTable, analysesIds, resource)

        response['body'] = json.dumps({ 'analyseObjects': analyseObjects})
        response['statusCode'] = 200
    except (Exception, ClientError) as error:
        print(error)
        response['statusCode'] = 400
        response['body'] = json.dumps({'error': str(error)})

    return response

def getUserColumn(usersTable, userId):
    expression = 'analyses'
    user = usersTable.get_item(
        ProjectionExpression=expression,
        Key={'id': userId}
    )

    if 'Item' not in user:
        raise ValueError('User not found')
    
    return user['Item']['analyses']

def getUserAnalysisById(analysisTable, analysisIds, resource):
    items_data = resource.batch_get_item(
        RequestItems = {
            analysisTable.name: {
                'Keys': analysisIds,
                'ProjectionExpression': 'id, title, description, created_by, updated_by, updated_date, transcript, creation_date'
            }
        }
    )
    return items_data['Responses'][analysisTable.name]
