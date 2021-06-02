import json

import boto3
from botocore.exceptions import ClientError

AWS_REGION = "us-east-1"
USERPOOLID = "us-east-1_FC8kBApuy"
CLIENTID = "235qakl0if7b3vss5ikehppnmi"

def lambda_handler(event, context):
    
    RESCODE = 200
    RESBODY = json.dumps("All Good!")
    
    if event['prewarm'] == 'yes':
        return {
            'statusCode': RESCODE,
            'body': RESBODY
        }
    
    item = ''

    dynamodb = boto3.resource('dynamodb',region_name=AWS_REGION)

    table = dynamodb.Table('CdkStack-magiclinkTableE01A1656-51952RVXND2N')
    
    try:
        response = table.get_item(Key={'id': event['username']})
    except ClientError as e:
        print(e.response['Error']['Message'])
        RESBODY = json.dumps(e.response['Error']['Message'])
        RESCODE = 400
    else:
        print(response)
        item = response['Item']
        RESBODY = json.dumps({"username": event['username'], "session": item['session']})

    print (RESBODY)
    return {
        'statusCode': RESCODE,
        'body': RESBODY
    }
