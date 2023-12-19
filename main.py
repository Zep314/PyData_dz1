import requests

url = "https://api.foursquare.com/v3/places/search"

headers = {
    "Accept": "application/json",
    "Authorization": "fsq3KHqn/0O9Yppp0vwz/B99aVtbL6ZbH98ehhpKqzrEua8="
}

if __name__ == '__main__':
    response = requests.request("GET", url, headers=headers)
    print(response.text)

#Client Id = GO4ILQMV0FPGDVJEAQ0HBUN0AJNDRBIYDK1FE5WP2EH4AOCR
#Client Secret = DVAHS50CDEHDSGPSNPPMTE1NH0FZMI3WHDB13ZUIB1YX3UAC
#Token = fsq3KHqn/0O9Yppp0vwz/B99aVtbL6ZbH98ehhpKqzrEua8=
#https://www.kaggle.com/code/kristoft/tutorial-foursquare-api-search
