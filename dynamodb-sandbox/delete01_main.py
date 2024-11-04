from dotenv import load_dotenv

load_dotenv()

import time

from local import get_local_client

dynamodb = get_local_client()


dynamodb.delete_item(
    TableName="Sample01",
    Key={
        "PColumn": {"S": "000001"},
        "SColumn": {"N": "2"},
    },
)
