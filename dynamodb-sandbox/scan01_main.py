from dotenv import load_dotenv

load_dotenv()

from local import get_local_client
from boto3.dynamodb.types import TypeDeserializer

dynamodb = get_local_client()

deserializer = TypeDeserializer()

def deserialize_dynamodb_response_item(obj: dict):
   return {k: deserializer.deserialize(v) for k, v in obj.items()}

# 細かい条件はつけずscanする。
res = dynamodb.scan(TableName="Sample01")

# そのままだと結果は扱いづらい形になっている。
for rec in res["Items"]:
    print(rec)

# デシリアライズすると使いやすい形に
print("------")
for rec in res["Items"]:
    rec2 = deserialize_dynamodb_response_item(rec)
    print(rec2)

# Itemごとデシリアライズ
print("------")
deserialized_items = map(deserialize_dynamodb_response_item, res["Items"])
for rec in deserialized_items:
  print(rec)
