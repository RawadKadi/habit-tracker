import requests
from datetime import datetime
USERNAME="rawadkadi"
TOKEN="asdflaskjdf"
pixela_endpoint="https://pixe.la/v1/users"
GRAPH_ID="graph1"
user_params={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}
graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config={
    "id":GRAPH_ID,
    "name":"Cycling Graph",
    "unit":"Km",
    "type":"float",
    "color":"ajisai",
}
headers={
    "X-USER-TOKEN":TOKEN,
}

pixel_condition_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
print(pixel_condition_endpoint)
today=datetime.now()

pixel_data={
    "date":today.strftime("%Y%m%d"),
    "quantity":"9.74",
}

# response=requests.post(url=pixel_condition_endpoint,json=pixel_data,headers=headers)
# print(response.text)

update_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data={
    "quantity":"4.5",
}

delete_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

response=requests.put(url=delete_endpoint,headers=headers)
print(response.text)
