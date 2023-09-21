from __future__ import print_function
import os.path
import os
from datetime import datetime
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from utils.constants import Constants
import base64
import smtplib
import ssl
from contextlib import closing
import pickle


SCOPES = ['https://www.googleapis.com/auth/calender']


class GoogleCalender:

    def __init__(self):
        self.creds = None

        if os.path.exists('token.json'):
            self.creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                self.creds = flow.run_local_server(port=0)
            with open('token.json', 'w') as token:
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




events = GoogleCalender().read_num_events(4)
print(events)