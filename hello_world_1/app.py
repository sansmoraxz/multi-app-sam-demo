import json

import boto3
import os
import time

bucket_name = os.getenv('BUCKET_NAME', 'my-bucket')

def lambda_handler(event, context):

    s3 = boto3.resource('s3')
    current_time = time.time()

    body = {
        "message": "hello from lambda 1",
        "time": current_time
    }

    s3.put_object(Bucket=bucket_name, Key='hello_world_1.txt', Body=json.dumps(body))

    return {
        "statusCode": 200,
        "body": json.dumps(body),
    }

if __name__ == '__main__':
    print(lambda_handler(None, None))
