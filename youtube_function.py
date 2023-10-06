import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import webbrowser
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class Youtube: 
     
     def __init__(self, credentials ="./credentials.json", token="./token.json" , query =None,url=None) -> None:
        self.credentials = credentials
        self.token = token
        self.SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]
        self.query= query 
        self.url = url

        credentials = None
        if os.path.exists(token):
                credentials = Credentials.from_authorized_user_file(token, self.SCOPES)
        if not credentials or not credentials.valid:
                if credentials and credentials.expired and credentials.refresh_token:
                    credentials.refresh(Request())
        # Initialize the OAuth2 flow
                else: 
                    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
                            credentials ,self.SCOPES)
                    credentials = flow.run_local_server(port=0)
                with open(token, "w") as token:
                    token.write(credentials.to_json())
 # Create a YouTube API client
        self.youtube = googleapiclient.discovery.build('youtube', 'v3', credentials=credentials)

     def search_play(self):
        youtube = self.youtube
        # Perform a YouTube search
        request = youtube.search().list(
            q=self.query,
            type='video',
            part='id,snippet',
            maxResults=10  # You can adjust the number of results you want to retrieve
        )

        response = request.execute()

        # Process and print the search results
        for item in response['items']:
            video_title = item['snippet']['title']
            video_id = item['id']['videoId']
            print(f'Title: {video_title}\nVideo ID: {video_id}\n')

        if 'items' in response and len(response['items']) > 0:
            first_result = response['items'][0]
            video_id = first_result['id']['videoId']
            video_url = f'https://www.youtube.com/watch?v={video_id}'
            webbrowser.open(video_url) 

     def open_url(self):
          webbrowser.open(self.url)




    