from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from testTask.settings import YOUTUBE_API_KEY
import os
import pickle
import requests

SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]


def auth():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    api_service_name = "youtube"
    api_version = "v3"
    credentials_filename = "credentials.json"
    credentials = None
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            credentials = pickle.load(token)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credentials_filename, SCOPES)
            credentials = flow.run_local_server(port=8000)
        with open("token.pickle", "wb") as token:
            pickle.dump(credentials, token)
    return build(api_service_name, api_version, credentials=credentials)


def search(query):
    response = requests.get('https://youtube.googleapis.com/youtube/v3/search', params={
        'key': YOUTUBE_API_KEY,
        'part': 'snippet',
        'q': query,
        'type': 'video',
        'maxResults': 30
    })
    return response.json()


def get_video_details(ids):
    response = requests.get('https://youtube.googleapis.com/youtube/v3/videos', params={
        'key': YOUTUBE_API_KEY,
        'part': 'snippet,statistics',
        'id': ids
    })
    return response.json()