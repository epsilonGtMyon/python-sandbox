from dotenv import load_dotenv
load_dotenv()

import time

from local import get_local_client

dynamodb = get_local_client()

table_name = "Sample01"

dynamodb.put_item(
    TableName=table_name,
    Item={
        "PColumn": {"S": "000001"},
        "SColumn": {"N": "1"},
        "FirstName": {"S": "太郎"},
        "FamilyName": {"S": "山田"},
        "CreatedAt": {"N": str(time.time())},
        "UpdatedAt": {"N": str(time.time())}
    }
)

dynamodb.put_item(
    TableName=table_name,
    Item={
        "PColumn": {"S": "000001"},
        "SColumn": {"N": "2"},
        "FirstName": {"S": "二郎"},
        "FamilyName": {"S": "山田"},
        "CreatedAt": {"N": str(time.time())},
        "UpdatedAt": {"N": str(time.time())}
    }
)


dynamodb.put_item(
    TableName=table_name,
    Item={
        "PColumn": {"S": "000002"},
        "SColumn": {"N": "1"},
        "FirstName": {"S": "一郎"},
        "FamilyName": {"S": "田中"},
        "CreatedAt": {"N": str(time.time())},
        "UpdatedAt": {"N": str(time.time())}
    }
)

dynamodb.put_item(
    TableName=table_name,
    Item={
        "PColumn": {"S": "000002"},
        "SColumn": {"N": "2"},
        "FirstName": {"S": "かずお"},
        "FamilyName": {"S": "田中"},
        "CreatedAt": {"N": str(time.time())},
        "UpdatedAt": {"N": str(time.time())}
    }
)


