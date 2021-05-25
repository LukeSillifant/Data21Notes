import boto3
from pprint import pprint
import json
import pandas as pd

# Three ways

# Low level access
s3_client = boto3.client('s3')
# print(s3_client)


bucket_list = s3_client.list_buckets()
# pprint(bucket_list, sort_dicts=False)
# pprint(bucket_list['Buckets'])
# print("\n")

# for bucket in bucket_list["Buckets"]:
#     pprint(bucket["Name"])

bucket_name = "data-eng-resources"
# bucket_contents = s3_client.list_objects_v2(Bucket=bucket_name, Prefix='big-data/pig-demo')
# pprint(bucket_contents)

# for name in bucket_contents["Contents"]:
#     pprint(name["Key"])


s3_resource = boto3.resource('s3')

bucket = s3_resource.Bucket(bucket_name)
# contents = bucket.objects.all()
# print(bucket)
# pprint(contents)
# for objects in contents:
#     print(objects.key)

# s3_object = s3_client.get_object(Bucket=bucket_name, Key="python/chatbot-intent.json")
# pprint(s3_object["Body"])
#
# contents = s3_object["Body"].read()
# contents_dict = json.loads(contents)
# pprint(contents_dict)

s3_object2 = s3_client.get_object(Bucket=bucket_name, Key="python/fish-market.csv")
pprint(s3_object2["Body"])

df = pd.read_csv(s3_object2["Body"])
pprint(df)

# Write to S3

