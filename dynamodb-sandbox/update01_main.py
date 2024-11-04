from dotenv import load_dotenv

load_dotenv()

import time

from local import get_local_client

dynamodb = get_local_client()


dynamodb.update_item(
    TableName="Sample01",
    Key={
        "PColumn": {"S": "000001"},
        "SColumn": {"N": "1"},
    },
    UpdateExpression="set UpdatedAt=:UpdatedAt",
    ExpressionAttributeValues={":UpdatedAt": {"N": str(time.time())}},
)
