import requests
from geopy.geocoders import Nominatim # module to convert an address into latitude and longitude values

CLIENT_ID = 'GO4ILQMV0FPGDVJEAQ0HBUN0AJNDRBIYDK1FE5WP2EH4AOCR'
CLIENT_SECRET = 'DVAHS50CDEHDSGPSNPPMTE1NH0FZMI3WHDB13ZUIB1YX3UAC'
url = "https://api.foursquare.com/v3/places/search"

address = '89 E 42nd St, New York, NY 10017'

geolocator = Nominatim(user_agent="foursquare_agent")
location = geolocator.geocode(address)
latitude = location.latitude
longitude = location.longitude
LIMIT = 2
radius = 1000
search_query = 'Pizza'

headers = {
    "Accept": "application/json",
    "Authorization": "fsq3KHqn/0O9Yppp0vwz/B99aVtbL6ZbH98ehhpKqzrEua8=",
}


if __name__ == '__main__':
    url = f'https://api.foursquare.com/v3/places/search?ll=40.7,-74&query=sushi&limit=2'
    response = requests.request("GET", url, headers=headers)
    print(response.text)

#Client Id = GO4ILQMV0FPGDVJEAQ0HBUN0AJNDRBIYDK1FE5WP2EH4AOCR
#Client Secret = DVAHS50CDEHDSGPSNPPMTE1NH0FZMI3WHDB13ZUIB1YX3UAC
#Token = fsq3KHqn/0O9Yppp0vwz/B99aVtbL6ZbH98ehhpKqzrEua8=
#https://www.kaggle.com/code/kristoft/tutorial-foursquare-api-search
# import requests
#
# # Замените YOUR_CLIENT_ID и YOUR_CLIENT_SECRET на ваши реальные ключи Foursquare
# CLIENT_ID = 'GO4ILQMV0FPGDVJEAQ0HBUN0AJNDRBIYDK1FE5WP2EH4AOCR'
# CLIENT_SECRET = 'DVAHS50CDEHDSGPSNPPMTE1NH0FZMI3WHDB13ZUIB1YX3UAC'
# VERSION = '20231220'  # Версия API
#
# # Координаты (например, центр города)
# latitude = 40.7128
# longitude = -74.0060
#
# # Параметры запроса
# params = {
#     'client_id': CLIENT_ID,
#     'client_secret': CLIENT_SECRET,
#     'v': VERSION,
#     'll': f'{latitude},{longitude}',
#     'query': 'музей',
#     'intent': 'browse',
#     'radius': 1000,  # Радиус поиска в метрах
#     'limit': 10  # Ограничение на количество результатов
# }
#
# # URL для запроса
# url = 'https://api.foursquare.com/v3/venues/search'
#
# # Выполнение запроса
# response = requests.get(url, params=params)
# data = response.json()
#
# print(data)
# # Вывод результатов
# for venue in data['response']['venues']:
#     print(f"Название: {venue['name']}")
#     print(f"Адрес: {venue['location']['address']}")
#     print("-" * 30)


#RESTClient https://api.foursquare.com/v3/places/search?ll=40.7,-74&query=музей&limit=1
