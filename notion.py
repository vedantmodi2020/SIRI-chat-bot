import json
import requests
from datetime import datetime


class NotionClient:

    def __init__(self, token, database_id) -> None:
        self.database_id = database_id

        self.headers = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json",
            "Notion-Version": "2021-08-16"
        }

    # read, update
    def create_page(self, description ):
        status="Active"
        date = datetime.now().astimezone().isoformat()
        create_url = f'https://api.notion.com/v1/databases/{self.database_id}/pages'

        data = {
        "parent": { "database_id": self.database_id },
        "properties": {
            "Description": {
                "title": [
                    {
                        "text": {
                            "content": description
                        }
                    }
                ]
            },
            "Date": {
                "date": {
                            "start": date,
                            "end": None
                        }
            },
            "Status": {
                "rich_text": [
                    {
                        "text": {
                            "content": status
                        }
                    }
                ]
            }
        }}

        data = json.dumps(data)
        res = requests.post(create_url, headers=self.headers, data=data)
        print(res.status_code)
        return res
    

