from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCOPES = ["https://www.googleapis.com/auth/drive"]
SERVICE_ACCOUNT_FILE = "config/credentials.json"


def get_drive_service():
    credentials = Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=SCOPES
    )

    return build("drive", "v3", credentials=credentials)


def create_folder(folder_name):
    service = get_drive_service()

    folder_metadata = {
        "name": folder_name,
        "mimeType": "application/vnd.google-apps.folder"
    }

    folder = service.files().create(
        body=folder_metadata,
        fields="id"
    ).execute()

    return folder["id"]


def upload_image(file_path, folder_id):
    service = get_drive_service()

    file_metadata = {
        "name": file_path.split("/")[-1],
        "parents": [folder_id]
    }

    media = MediaFileUpload(file_path)

    file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields="id, webViewLink"
    ).execute()

    return file["webViewLink"]