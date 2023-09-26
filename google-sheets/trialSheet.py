import os
# imports
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class GoogleSheetsAPI:
    def __init__(self, credentials="token1.json", key ="./credentials.json" , SPREAD_ID = None):
        self.SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]  #accessed by multiple functions in multiple places 
        self.credentials = credentials
        self.key = key
        self.SPREAD_ID = SPREAD_ID # we leave this parameter as none since whenever a new object is specified this will be unique identifier of it

    def auth(self):
        credentials = None
        if os.path.exists(self.credentials):
            credentials = Credentials.from_authorized_user_file(self.credentials, self.SCOPES)
        if not credentials or not credentials.valid:
            if credentials and credentials.expired and credentials.refresh_token:
                credentials.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(self.key, self.SCOPES)
                credentials = flow.run_local_server(port=0)
            with open(self.credentials, "w") as token:
                token.write(credentials.to_json())
        self.service = build("sheets", "v4", credentials=credentials) #now this variable will be available in other method

    def modify(self, SHEET_NAME):
        try:
           
            sheets = self.service.spreadsheets()

            result = sheets.values().get(spreadsheetId=self.SPREAD_ID, range=f"{SHEET_NAME}!A1:C6").execute()
            values = result.get("values", [])

            for row in range(2, 7):
                num1 = int(sheets.values().get(spreadsheetId=self.SPREAD_ID, range=f"{SHEET_NAME}!A{row}").execute().get("values")[0][0])
                num2 = int(sheets.values().get(spreadsheetId=self.SPREAD_ID, range=f"{SHEET_NAME}!B{row}").execute().get("values")[0][0])
                res = num1 + num2
                print(f"Processing {num1} + {num2} ")

                sheets.values().update(spreadsheetId=self.SPREAD_ID, range=f"{SHEET_NAME}!C{row}", valueInputOption="USER_ENTERED", body={"values": [[f"{res}"]]}).execute()

                sheets.values().update(spreadsheetId=self.SPREAD_ID, range=f"{SHEET_NAME}!D{row}", valueInputOption="USER_ENTERED", body={"values": [["DONE!"]]}).execute()

        except HttpError as error:
            print(error)


if __name__ == "__main__":
    test = GoogleSheetsAPI(SPREAD_ID="1ViRolg6v9k83s7BD35qeCf8z_T_11pRNEt9qflQr0CA")
    test.auth()
    test.modify(SHEET_NAME="Sheet1")