import boto3
import json
import pandas as pd
import io

s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')

my_dict = {"Name": "Luke", "groceries": ["Chocolate Hobnobs", "Chicken"]}


# JSON

# with open("luke-dict.json", "w") as jsonfile:
#     json.dump(my_dict, jsonfile)
#
# s3_client.upload_file(Filename="luke-dict.json", Bucket="data-eng-resources", Key="Data21/lukesillifant.json")

# s3_client.put_object(Body=json.dumps(my_dict), Bucket="data-eng-resources", Key="Data21/Put/lukesillifant.json")


# CSV

df = pd.DataFrame([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

str_buffer = io.StringIO()
df.to_csv(str_buffer)

s3_client.put_object(Body=str_buffer.getvalue(), Bucket="data-eng-resources", Key="Data21/CSV/lukesillifant.csv")

s3_resource.Object("data-eng-resources", "Data21/CSV/lukesillifant.csv").put(Body=str_buffer.getvalue())