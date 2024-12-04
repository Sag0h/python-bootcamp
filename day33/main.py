import requests
import time

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



def print_iss_location(my_loc, has_location=False):        
    try:
        response = requests.get(url="http://api.open-notify.org/iss-now.json")
        data = response.json()

        longitude = data['iss_position']['longitude']
        latitude = data['iss_position']['latitude']
        
        print(f"The ISS current position is long= {longitude} lat= {latitude}")
        if(has_location):
            if latitude == my_loc[0] and longitude == my_loc[1]:
                print("The ISS is literally above you. Look up to the sky and say hi!")
        time.sleep(1)
    except:
        print("signal lost")
        time.sleep(1)

my_location, has_loc= get_address_from_ip()
while True:
    print_iss_location(my_location, has_loc)