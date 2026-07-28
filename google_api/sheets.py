from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

from googleapiclient.discovery import build


SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets"
]


def get_sheets_service():

    creds = None

    token_path = Path("config/token_sheets.json")

    if token_path.exists():
        creds = Credentials.from_authorized_user_file(
            token_path,
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

        token_path.write_text(
            creds.to_json()
        )

    return build(
        "sheets",
        "v4",
        credentials=creds
    )


def create_sheet(title):

    service = get_sheets_service()

    spreadsheet = {
        "properties": {
            "title": title
        }
    }

    response = service.spreadsheets().create(
        body=spreadsheet,
        fields="spreadsheetId"
    ).execute()

    return response["spreadsheetId"]


def insert_books(sheet_id, books):

    service = get_sheets_service()

    values = [
        [
            "Título",
            "link da Capa",
            "Preço",
            "Rating",
            "Disponibilidade"
        ]
    ]

    for book in books:
        values.append(
            [
                book["name"],
                book["cover"],
                book["price"],
                book["rating"],
                book["availability"]
            ]
        )

    body = {
        "values": values
    }

    service.spreadsheets().values().update(
        spreadsheetId=sheet_id,
        range="A1",
        valueInputOption="RAW",
        body=body
    ).execute()