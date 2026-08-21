import os.path
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


SCOPES = [
    "https://www.googleapis.com/auth/calendar.readonly"
]

TIMEZONE = ZoneInfo("America/Argentina/Buenos_Aires")


def get_credentials():
    creds = None

    # token.json se genera después de que autorices
    # la aplicación por primera vez.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file(
            "token.json",
            SCOPES,
        )

    # Si no existen credenciales válidas...
    if not creds or not creds.valid:

        # Si tenemos refresh token, renovamos
        # el access token automáticamente.
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

        # Primera ejecución:
        # abre el navegador para autorizar nuestra app.
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json",
                SCOPES,
            )

            creds = flow.run_local_server(port=0)

        # Guardamos access token + refresh token.
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    return creds


def get_today_events():
    creds = get_credentials()

    service = build(
        "calendar",
        "v3",
        credentials=creds,
    )

    now = datetime.now(TIMEZONE)

    # 00:00 de hoy
    start_of_day = now.replace(
        hour=0,
        minute=0,
        second=0,
        microsecond=0,
    )

    # 00:00 de mañana
    end_of_day = start_of_day + timedelta(days=1)

    events_result = (
        service.events()
        .list(
            calendarId="primary",

            timeMin=start_of_day.isoformat(),
            timeMax=end_of_day.isoformat(),

            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )

    events = events_result.get("items", [])

    return parse_events(events)


def parse_events(events):
    parsed_events = []

    for event in events:
        start = event["start"]
        end = event["end"]

        # Los eventos normales tienen dateTime.
        # Los eventos de día completo tienen date.
        start_value = start.get(
            "dateTime",
            start.get("date"),
        )

        end_value = end.get(
            "dateTime",
            end.get("date"),
        )

        parsed_events.append({
            "name": event.get(
                "summary",
                "Sin título",
            ),

            "start": start_value,
            "end": end_value,

            "location": event.get("location"),
        })

    return parsed_events