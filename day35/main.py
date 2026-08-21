from weather import get_today_weather
from calendar_service import get_today_events
from ai_service import generate_daily_brief
from telegram_service import send_telegram_message


def main():
    weather = get_today_weather()
    events = get_today_events()

    message = generate_daily_brief(
        weather=weather,
        events=events,
    )

    send_telegram_message(message)


if __name__ == "__main__":
    main()


