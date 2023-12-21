import requests
from geopy.geocoders import Nominatim  # модуль конвертации адреса в долготу и широту

url = "https://api.foursquare.com/v3/places/search"
address = 'Москва, Красная площадь'
LIMIT = 10     # Лимит по количеству объектов запроса
radius = 1000  # Радиус поиска объектов от центральной точки (в метрах)

headers = {
    "Accept": "application/json",
    "Authorization": "fsq3KHqn/0O9Yppp0vwz/B99aVtbL6ZbH98ehhpKqzrEua8=",
}

if __name__ == '__main__':
    geolocator = Nominatim(user_agent="foursquare_agent")  # Получаем долготу и широту указанного адреса
    location = geolocator.geocode(address)
    if location:
        latitude = location.latitude
        longitude = location.longitude

        print('Введите "/exit" для выхода')
        while True:
            search_query = input('Введите заведение: ')
            if search_query == '/exit':
                break
            params = {
                "ll": f"{latitude},{longitude}",
                "query": search_query,
                "limit": LIMIT,
                "sort": "DISTANCE",                # Сортировка по возрастанию расстояния от центра поиска
                "radius": radius,
                "fields": "name,location,rating",  # Только эти поля нам понадобятся
            }
            response = requests.request("GET", url, params=params, headers=headers)
            if response.status_code == 200:
                data = response.json()
                for row in data['results']:
                    print(f"{row.get('name', 'Nan')}; "
                          f"{row.get('location', 'Nan').get('address', 'Nan')}; "
                          f"{row.get('rating', 'Nan')}")
                print()
            else:
                print(f'Error {response.status_code}')
    else:
        print('Location not found!')

# Результат работы:

# C:\Work\python\Data\PyData_dz1\venv\Scripts\python.exe C:\Work\python\Data\PyData_dz1\main.py
# Введите "/exit" для выхода
# Введите заведение: cafe
# Red Square (Красная площадь); Nan; 9.3
# Bosco Bar; Красная пл., 3; 8.2
# Ресторан Му-Му; Малый Гнездниковский пер., 9; Nan
# Organic Cafe; Бол. Садовая Ул., д. 6/2; Nan
# Торговый дом Тибет; Жуков Пр., 19; Nan
# Бубликшоп, кафе-кулинария; Ленинский Пр., 57; Nan
# СВС; Люблинская, 96 ст2; Nan
# United Catering Assistance, кейтеринговая компания; Нижняя, 14-БЦ Petrovsky; Nan
# Saltenas, сеть гриль-кафе; Киевского Вокзала пл., 2; Nan
# DJ BOWLING CAFE; Минское ш., 23 км; Nan
#
# Введите заведение: museum
# Lenin's Mausoleum (Мавзолей В. И. Ленина); Красная пл., д.1/2; 5.6
# ВОЕННО-ИСТОРИЧЕСКИЙ МУЗЕЙ БРОНЕТАНКОВОГО ВООРУЖЕНИЯ И ТЕХНИКИ; Минское ш., 64 км; Nan
# Музей П.И. Чайковский и Москва; Поварская, 54/46; Nan
# POBEDA; пл Красная, д.33 линия; Nan
# St. Basil's Cathedral (Храм Василия Блаженного); Nan; 8.7
# Музей печатной графики; Хрустальный пер., д.11; Nan
# Старый гостиный двор; Хрустальный пер., 1; 5.6
# МУЗЕЙ ПАРФЮМЕРНОГО ИСКУССТВА; Ильинка Ул. 4; Nan
# Kazan Cathedral, Moscow; Nan; Nan
# Выставочный комплекс Артиллерийский двор - Цены на услуги; пл Красная, д.1; Nan
#
# Введите заведение: shop
# Motor-shop.ru, интернет-магазин автозапчастей; Шипиловская Ул., д.34; Nan
# SantShop, интернет-магазин; Каширское ш., 1; Nan
# Shop and go, журнал; Мира Пр., 95; Nan
# ANEX SHOP, сеть туристических агентств; Большая Тульская, 2; Nan
# Termal-Shop, торгово-производственная компания; Вербная, 8б; Nan
# Shopzont, магазин зонтов; Шарикоподшипниковская, 13, 75 павильон; Nan
# ANEX SHOP, сеть туристических агентств; Пушечная, 3; Nan
# ShopSirop, интернет-магазин; Покровка, 41/8 ст2; Nan
# ANEX SHOP, Сеть туристических агентств; Комсомольский Пр., 44; Nan
# Slk-shop, магазин пиротехники и сувениров; Профсоюзная, 109; Nan
#
# Введите заведение: /exit
#
# Process finished with exit code 0
