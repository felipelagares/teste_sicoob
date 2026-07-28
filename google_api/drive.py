from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCOPES = ["https://www.googleapis.com/auth/drive.file"]


def get_drive_service():
    creds = None

    token = Path("config/token.json")

    if token.exists():
        creds = Credentials.from_authorized_user_file(
            token,
            SCOPES
        )

    if not creds or not creds.valid:

        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "config/client_secret.json",
                SCOPES
            )

            creds = flow.run_local_server(port=0)

        token.write_text(creds.to_json())

    return build("drive", "v3", credentials=creds)

def create_folder(folder_name):
    service = get_drive_service()

    metadata = {
        "name": folder_name,
        "mimeType": "application/vnd.google-apps.folder"
    }

    folder = service.files().create(
        body=metadata,
        fields="id"
    ).execute()

    return folder["id"]

def upload_image(file_path, folder_id):

    service = get_drive_service()

    metadata = {
        "name": Path(file_path).name,
        "parents": [folder_id]
    }

    media = MediaFileUpload(file_path)

    file = service.files().create(
        body=metadata,
        media_body=media,
        fields="id, webViewLink"
    ).execute()

    return file["webViewLink"]