from __future__ import print_function
import os.path
import os
from datetime import datetime, timedelta
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import json


SCOPES = ['https://www.googleapis.com/auth/calender']


class GoogleCalender:

    def __init__(self):
        self.creds = None

        if os.path.exists('/Users/vedant/PycharmProjects/pythonProject/FridayAI/token.json'):
            self.creds = Credentials.from_authorized_user_file('/Users/vedant/PycharmProjects/pythonProject/FridayAI/token.json', SCOPES)
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    '/Users/vedant/PycharmProjects/pythonProject/FridayAI/credentials.json', SCOPES)
                self.creds = flow.run_local_server(port=0)
            with open('/Users/vedant/PycharmProjects/pythonProject/FridayAI/token.json', 'w') as token:
                token.write(self.creds.to_json())



    def read_num_events(self,num,startTime = datetime.now().isoformat() + "Z"):
        try:
            service = build('calendar', 'v3', credentials=self.creds)
            events_result = service.events().list(calendarId='primary', timeMin=startTime,
                                              maxResults=num, singleEvents=True,
                                              orderBy='startTime').execute()
            events = events_result.get("items",[])
            if not events:
                return (f"No upcoming Events form this start time : {str(startTime)}")
            
            for event in events:
                start = event["start"].get("dateTime",event["start"].get("date"))
                return start,event["summary"]

        except Exception as e:
            print(f"An Exception Occurred during the reading of the Events : {str(e)}")
            return (f"An error Occurred please stop the Execution : {str(e)}")


    def create_event(self,event_name,startTime,endTime,emails):
        try:
            service = build('calendar', 'v3', credentials=self.creds)

            event = {
                "summary": event_name,
                "location": "https://whereby.com/vedant-ghost",
                "description": "It is Event created by GPT",
                "colorId": 6,
                "start":{
                    "dateTime": str(startTime),
                    "timeZone": "Asia/Kolkata",
                },
                "end":{
                    "dateTime": str(endTime),
                    "timeZone": "Asia/Kolkata",
                },
                "recurrence": [
                    "RRule:FREQ=DAILY;COUNT=1"
                ],
                "attendees": emails
            }

            
            creation  = service.events().insert(calendarId='primary',body=event).execute()

            print(f"Event Created Successfully")

            return (f"Event created successfully you can stop the execution link is this : {str(creation.get('htmlLink'))}")



        except Exception as e:
            return (f"An error Occurred please stop the Execution : {str(e)}")




# email_dict =[ {
#     "email":"arka2910.pramanik@gmail.com"
# },{
#     "email":"raajzz109109@gmail.com"
# },{
#     "email":"gauravkumar281217@gmail.com"
# }]
# events = GoogleCalender().create_event(
#     event_name="Test Event",
#     startTime="2023-09-22T00:18:20+0200",
#     endTime="2023-09-22T00:19:20+0200",
#     emails=email_dict
# )
# # events = GoogleCalender().read_num_events(num=1)
# print(events)