import requests


def get_address_from_ip():
    api_key = "929b93a319c547faa10172b96a16d8a5"
    try:
        response = requests.get('https://api.ipify.org?format=json')
        ip_info = response.json()
        ip_address = ip_info['ip']
        url = f"https://api.ipgeolocation.io/ipgeo?apiKey={api_key}"
        response_geo = requests.get(url)
        geo_data = response_geo.json()
        latitude = geo_data['latitude']
        longitude = geo_data['longitude']
        print(f"Your location is long={longitude} lat={latitude}")
        return (latitude, longitude), True
    except Exception:
        return (0, 0), False

parameters, has_location = get_address_from_ip()

full_params = {
    "lat": parameters[0],
    "lng": parameters[1],
    "formatted": 1,
}

if has_location:
    response = requests.get("https://api.sunrise-sunset.org/json", params=full_params)
    data = response.json()
    sunset = data["results"]["sunset"]
    print(f"your sunset time is {sunset}")