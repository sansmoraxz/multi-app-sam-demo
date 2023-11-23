import json

import numpy as np


def lambda_handler(event, context):

    arr = np.arange(100).reshape(10, 10)
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": arr.tolist(),
            # "location": ip.text.replace("\n", "")
        }),
    }

if __name__ == '__main__':
    print(lambda_handler(None, None))
