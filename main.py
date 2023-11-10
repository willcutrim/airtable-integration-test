
import os
import requests

token_get = 'SEU_TOKEN_GET'


base_id = "SUA_BASE_ID"
token_post = "SEU_TOKEN_POST"
table_name_or_id = "SUA_TABLE_NAME_OR_ID"

url=f'https://api.airtable.com/v0/{base_id}/{table_name_or_id}'

headers = {
    "Authorization": f"Bearer {token_post}",
    "Content-Type": "application/json"
}



def get_records():
    get_data = requests.get('https://api.airtable.com/v0/appYtvKOmLmmVXqqB/table01?maxRecords=3&view=Grid%20view', 
                            headers={
                            "Authorization": f"Bearer {token_get}",
                            "Content-Type": "application/json"
    })

    return get_data


def post_records(nome, email=None):

    if nome is None:
        return
    
    data = {
        "records": [
            {
                "fields": {
                    "nome": nome,
                    "email": email
                }
            }
        ]
    }
    
    response = requests.post(url, json=data, headers=headers)

    return response


