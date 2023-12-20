import requests
from geopy.geocoders import Nominatim  # модуль конвертации адреса в долготу и широту

url = "https://api.foursquare.com/v3/places/search"

address = 'Москва, Красная площадь'
search_query = 'museum'

LIMIT = 10
radius = 1000

headers = {
    "Accept": "application/json",
    "Authorization": "fsq3KHqn/0O9Yppp0vwz/B99aVtbL6ZbH98ehhpKqzrEua8=",
}

if __name__ == '__main__':
    geolocator = Nominatim(user_agent="foursquare_agent")
    location = geolocator.geocode(address)
    if location:
        latitude = location.latitude
        longitude = location.longitude

        params = {
            "ll": f"{latitude},{longitude}",
            "query": search_query,
            "limit": LIMIT,
            "sort": "DISTANCE",
            "radius": radius,
            "fields": "name,location,rating"
        }
        response = requests.request("GET", url, params=params, headers=headers)
        if response.status_code == 200:
            data = response.json()
            for row in data['results']:
                print(f"{row.get('name', 'Nan')}; "
                      f"{row.get('location', 'Nan').get('address', 'Nan')}; "
                      f"{row.get('rating', 'Nan')}")
        else:
            print(f'Error {response.status_code}')
    else:
        print('Location not found!')
