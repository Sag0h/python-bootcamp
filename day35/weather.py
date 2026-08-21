import requests
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo


URL = "https://api.open-meteo.com/v1/forecast"

LATITUDE = -34.9215
LONGITUDE = -57.9545

TIMEZONE_NAME = "America/Argentina/Buenos_Aires"
TIMEZONE = ZoneInfo(TIMEZONE_NAME)


def get_today_weather():
    params = {
        "latitude": LATITUDE,
        "longitude": LONGITUDE,

        "hourly": [
            "temperature_2m",
            "precipitation_probability",
            "precipitation",
            "wind_speed_10m",
        ],

        "daily": [
            "temperature_2m_max",
            "temperature_2m_min",
            "precipitation_probability_max",
        ],

        "timezone": TIMEZONE_NAME,

        # Pedimos hoy + mañana porque queremos conservar
        # también las primeras horas de la madrugada siguiente.
        "forecast_days": 2,
    }

    response = requests.get(
        URL,
        params=params,
        timeout=10,
    )

    response.raise_for_status()

    data = response.json()

    return parse_weather(data)

def calculate_feels_like(temperature, wind_speed):
    """
    Calcula wind chill cuando hace frío.

    Fórmula válida aproximadamente para:
    - temperatura <= 10 °C
    - viento > 4.8 km/h

    Si no se cumplen esas condiciones,
    devolvemos la temperatura real.
    """

    if temperature <= 10 and wind_speed > 4.8:
        feels_like = (
            13.12
            + 0.6215 * temperature
            - 11.37 * (wind_speed ** 0.16)
            + 0.3965
            * temperature
            * (wind_speed ** 0.16)
        )

        return round(feels_like, 1)

    return temperature

def parse_weather(data):
    daily = data["daily"]
    hourly = data["hourly"]

    now = datetime.now(TIMEZONE)

    # -----------------------------------------------------
    # INICIO DEL PRONÓSTICO
    # -----------------------------------------------------
    # Nos quedamos con la próxima hora completa.
    #
    # Ejemplo:
    # 06:37 -> empezamos desde las 07:00
    # 07:12 -> empezamos desde las 08:00
    #
    # Si justo son las 07:00 exactas, conservamos las 07:00.
    # -----------------------------------------------------

    start_time = now.replace(
        minute=0,
        second=0,
        microsecond=0,
    )

    if now.minute > 0 or now.second > 0 or now.microsecond > 0:
        start_time += timedelta(hours=1)

    # -----------------------------------------------------
    # FIN DEL PRONÓSTICO
    # -----------------------------------------------------
    # Queremos información hasta las 02:00 del día siguiente,
    # inclusive.
    # -----------------------------------------------------

    tomorrow = now.date() + timedelta(days=1)

    end_time = datetime(
        year=tomorrow.year,
        month=tomorrow.month,
        day=tomorrow.day,
        hour=2,
        minute=0,
        tzinfo=TIMEZONE,
    )

    # -----------------------------------------------------
    # INFORMACIÓN HORARIA
    # -----------------------------------------------------

    hourly_weather = []

    for i in range(len(hourly["time"])):

        # Open-Meteo devuelve algo como:
        # "2026-08-21T18:00"
        weather_time = datetime.fromisoformat(
            hourly["time"][i]
        ).replace(tzinfo=TIMEZONE)

        # Ignoramos las horas que ya pasaron y también
        # cualquier cosa posterior a mañana a las 02:00.
        if start_time <= weather_time <= end_time:
            temperature = hourly["temperature_2m"][i]
            wind_speed = hourly["wind_speed_10m"][i]
            hourly_weather.append({
                # Conservamos fecha + hora porque después
                # tendremos datos pertenecientes a dos días.
                "datetime": weather_time.isoformat(),

                "temperature": temperature,

                "feels_like": calculate_feels_like(
                    temperature,
                    wind_speed,
                ),

                "rain_probability":
                    hourly["precipitation_probability"][i],

                "precipitation":
                    hourly["precipitation"][i],
                    
                "wind_speed": wind_speed,
            })

    # -----------------------------------------------------
    # INFORMACIÓN DIARIA
    # -----------------------------------------------------
    #
    # forecast_days=2 hace que Open-Meteo devuelva:
    #
    # daily["time"][0] -> hoy
    # daily["time"][1] -> mañana
    #
    # Como max/min/max rain pertenecen al resumen DEL DÍA
    # DE HOY, usamos índice [0].
    # -----------------------------------------------------

    today_weather = {
        "date": daily["time"][0],

        "min_temperature":
            daily["temperature_2m_min"][0],

        "max_temperature":
            daily["temperature_2m_max"][0],

        "max_rain_probability":
            daily["precipitation_probability_max"][0],
    }

    # -----------------------------------------------------
    # RESPUESTA NORMALIZADA DE NUESTRO SERVICIO
    # -----------------------------------------------------

    return {
        "today": today_weather,

        "forecast_from": start_time.isoformat(),
        "forecast_until": end_time.isoformat(),

        "hourly": hourly_weather,
    }


def get_rainy_hours(weather, threshold=40):
    rainy_hours = []

    for hour in weather["hourly"]:
        if hour["rain_probability"] >= threshold:
            rainy_hours.append(hour)

    return rainy_hours