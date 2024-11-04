from dotenv import load_dotenv
load_dotenv()

from local import get_local_client

dynamodb = get_local_client()

dynamodb.put_item(
    TableName="Sample01",
    Item={
        "PColumn": {"S": "000001"},
        "SColumn": {"N": "1"},
        "FirstName": {"S": "太郎"},
        "FamilyName": {"S": "山田"}
    }
)
