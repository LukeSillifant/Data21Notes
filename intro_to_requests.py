import requests
import json


post_code_req = requests.get("http://api.postcodes.io/postcodes/se120nb")
# Serialises data into json string
json_body = json.dumps({"postcodes": ["PR3 0SG", "M45 6GN", "EX16 5BL"]})

# Expecting use of json
headers = {"Content-Type": "application/json"}

post_code_req_multiple = requests.post("http://api.postcodes.io/postcodes", headers=headers, data=json_body)

# Returns status code
# print(post_code_req.status_code)

# Returns dictionary in 'bytes'
# print(post_code_req.content)

# Returns in better form
# print(post_code_req.json())

print(post_code_req_multiple.json())

