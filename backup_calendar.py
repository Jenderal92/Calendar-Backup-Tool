import os
import json
import time
from datetime import datetime
from apiclient.discovery import build
from oauth2client.file import Storage
from oauth2client.client import flow_from_clientsecrets
from oauth2client import tools
from googleapiclient.http import MediaFileUpload

def print_banner():
    banner = """
    =================================================
           CALENDAR BACKUP TOOL
           Secure your schedule. Backup with ease.
    =================================================
    """
    print(banner)

SCOPES = ['https://www.googleapis.com/auth/drive.file', 
          'https://www.googleapis.com/auth/calendar.readonly']
CREDENTIALS_FILE = 'credentials.json'
TOKEN_FILE = 'token.json'
BACKUP_FOLDER_NAME = "Calendar_Backups"

def authenticate_google_api():
    storage = Storage(TOKEN_FILE)
    creds = storage.get()
    
    if not creds or creds.invalid:
        flow = flow_from_clientsecrets(CREDENTIALS_FILE, scope=SCOPES)
        creds = tools.run_flow(flow, storage)
    
    return creds

def backup_calendar():
    print("Authenticating...")
    creds = authenticate_google_api()
    calendar_service = build('calendar', 'v3', credentials=creds)
    drive_service = build('drive', 'v3', credentials=creds)

    print("Fetching calendar list...")
    calendar_list = calendar_service.calendarList().list().execute()
    
    if 'items' not in calendar_list:
        print("No calendars found.")
        return

    for calendar in calendar_list['items']:
        calendar_id = calendar['id']
        print("Backing up calendar: {}".format(calendar['summary']))

        events = calendar_service.events().list(calendarId=calendar_id).execute()
        backup_file = "{}_backup_{}.json".format(
            calendar['summary'], datetime.now().strftime('%Y%m%d')
        )
        
        with open(backup_file, 'w') as file:
            json.dump(events, file, indent=4)

        upload_to_drive(drive_service, backup_file)

def upload_to_drive(drive_service, file_name):
    print("Uploading {} to Google Drive...".format(file_name))
    folder_id = get_or_create_folder(drive_service, BACKUP_FOLDER_NAME)

    file_metadata = {
        'name': file_name,
        'parents': [folder_id]
    }
    media = MediaFileUpload(file_name, mimetype='application/json')
    drive_service.files().create(body=file_metadata, media_body=media).execute()
    print("File {} uploaded successfully!".format(file_name))

def get_or_create_folder(drive_service, folder_name):
    query = "mimeType='application/vnd.google-apps.folder' and name='{}'".format(folder_name)
    results = drive_service.files().list(q=query).execute()
    items = results.get('files', [])
    
    if items:
        return items[0]['id']
    else:
        folder_metadata = {
            'name': folder_name,
            'mimeType': 'application/vnd.google-apps.folder'
        }
        folder = drive_service.files().create(body=folder_metadata).execute()
        return folder['id']

if __name__ == "__main__":
    print_banner()
    try:
        backup_calendar()
    except Exception as e:
        print("An error occurred: {}".format(e))
