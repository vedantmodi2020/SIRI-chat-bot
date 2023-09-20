from __future__ import print_function

import os.path
import os
from datetime import datetime
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from constants import Constants
import base64
import smtplib
import ssl
from contextlib import closing
import pickle


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

class GoogleEmail:

    def __init__(self):
        self.creds = None
        self.smtp_port = Constants.gogle_smtp_port
        self.smtp_server = Constants.google_smtp_server
        self.email_from = Constants.google_email_from
        self.pswd = Constants.google_email_pwd
        self.simple_email_context = ssl._create_unverified_context()

        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                self.creds = pickle.load(token)

        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
                self.creds = flow.run_local_server(port=0)

            with open('token.pickle', 'wb') as token:
                pickle.dump(self.creds, token)


    def _get_service(self):
        return build('gmail', 'v1', credentials=self.creds)

    def _list_messages(self, query):
        try:
            service = self._get_service()
            results = service.users().messages().list(userId='me', q=query).execute()
            messages = results.get('messages', [])
            return messages

        except HttpError as error:
            print(f'An error occurred: {error}')
            return []
        
    def _get_message(self, message_id):
        try:
            service = self._get_service()
            message = service.users().messages().get(userId='me', id=message_id).execute()
            return message

        except HttpError as error:
            print(f'An error occurred: {error}')
            return None

    def _decode_message_body_plain(self, message):
        body = message['payload']["parts"][0]["body"]
        if body['size'] > 0:
            data = body['data']
            decoded_data = base64.urlsafe_b64decode(data.encode('UTF-8')).decode('UTF-8')
            return decoded_data
        return ''
    
    def _decode_message_body_html(self,message):
        body = message['payload']["parts"][1]["body"]
        if body['size'] > 0:
            data = body['data']
            decoded_data = base64.urlsafe_b64decode(data.encode('UTF-8')).decode('UTF-8')
            return decoded_data
        return ''

    def read_labels(self):
        try:
            service = build('gmail', 'v1', credentials=self.creds)
            results = service.users().labels().list(userId='me').execute()
            labels = results.get('labels', [])

            if not labels:
                print('No labels found.')
                return
            print('Labels:')
            for label in labels:
                print(label['name'])

        except HttpError as error:
            print(f'An error occurred: {error}')

    def search_by_subject(self, subject:str):
        query = f'subject:{subject}'
        messages = self._list_messages(query)
        return messages

    def search_by_sender(self, sender:str):
        query = f'from:{sender}'
        messages = self._list_messages(query)
        return messages

    def search_by_date(self, date):
        start_date = datetime.strptime(date[0], '%Y-%m-%d').strftime('%Y/%m/%d')
        end_date = datetime.strptime(date[1], '%Y-%m-%d').strftime('%Y/%m/%d')
        query = f'after:{start_date} before:{end_date}'
        messages = self._list_messages(query)
        return messages
    
    def print_message_content_plain(self, message_id :str):
        message = self._get_message(message_id)
        if message:
            content = self._decode_message_body_plain(message)
            print('Message Content:\n', content)
            return content

    def print_message_content_html(self, message_id :str):
        message = self._get_message(message_id)
        if message:
            content = self._decode_message_body_html(message)
            print('Message Content:\n', content)
            return content

    def send_email(self,data):
        try:
            print("Connecting to server...")
            to_email = data.get("to_email")
            subject = data.get("subject")
            message_body = data.get("message_body")
            with closing(smtplib.SMTP(self.smtp_server, self.smtp_port)) as server:
                server.ehlo()
                server.starttls(context=self.simple_email_context)
                server.login(self.email_from, self.pswd)
                message = f'From: {self.email_from}\n' \
                    f'To: {to_email}\n' \
                    f'Subject: {subject}\n\n' \
                    f'{message_body}'
                server.sendmail(self.email_from, to_email, message)
                server.quit()
            print('Email sent successfully!')
            return ("Email sent successfully")

        except Exception as error:
            print(f'An error occurred: {error}')

    def send_email_attachments(self,data):
        try:
            to_email = data.get("to_email")
            subject = data.get("subject")
            message_body = data.get("message_body")
            file_path = data.get("file_path")
            msg = MIMEMultipart()
            msg["From"] = self.email_from
            msg["To"] = to_email
            msg["Subject"] = subject

            file_name = os.path.basename(file_path)

            msg.attach(MIMEText(message_body,'plain'))
            attachment = open(file_path,'rb')
            attachment_package = MIMEBase('application','octet-stream')
            attachment_package.set_payload(attachment.read())
            encoders.encode_base64(attachment_package)
            attachment_package.add_header('Content-Disposition', "attachment; filename= " + file_name)
            msg.attach(attachment_package)

            text = msg.as_string()

            print("Connecting to server...")
            with closing(smtplib.SMTP(self.smtp_server, self.smtp_port)) as server:
                server.starttls()
                server.login(self.email_from, self.pswd)
                print("Succesfully connected to server")
                print()


                # Send emails to "person" as list is iterated
                print(f"Sending email to: {to_email}...")
                server.sendmail(self.email_from, to_email, text)
                print(f"Email sent to: {to_email}")
                print()
                server.quit()

            return ("Email sent successfully")

        except Exception as e:
            print(f'An error occurred: {e}')
