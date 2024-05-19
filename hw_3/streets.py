import requests
from geopy.distance import geodesic
from bs4 import BeautifulSoup
import re
import pickle


def latitude_and_longitude(address):
    api_key = "my_api_key"
    url = f"https://geocode-maps.yandex.ru/1.x/?apikey={api_key}&format=json&geocode={address}"
    response = requests.get(url)
    data = response.json()
    coordinates = data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"].split(" ")
    return float(coordinates[1]), float(coordinates[0])


def distance(lat1, lon1, lat2, lon2):
    return geodesic((lat1, lon1), (lat2, lon2)).kilometers


def all_streets_spb():
    url = "https://100realt.ru/sankt-peterburg/ulitsy"
    response = requests.get(url)
    content = None
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        content = soup.get_text()
        content = content.split("Улицы Санкт-Петербурга")[1].split("Проспекты Санкт-Петербурга")[0]
        content = content.replace("Проспекты Санкт-Петербурга", ' ')
        content = content.split('\n')
        content = [s for s in content if re.match("[А-Яа-я]", s)]
    with open('streets_spb.txt', 'w') as file:
        for line in content:
            file.write(f"{line}\n")


def all_streets_spb_with_coords():
    f = open('streets_spb.txt', 'r').readlines()
    for i in range(len(f)):
        f[i] = f[i].replace('\n', '')
    with open('streets_spb_with_coords.txt', 'w') as file:
        for address in f:
            file.write(f"{address} {latitude_and_longitude(address + ', Санкт-Петербург')}\n")



def make_voc():
    f = open('streets_spb_with_coords.txt', 'r').readlines()
    voc = {}
    for i in range(len(f)):
        f[i] = f[i].replace('\n', '')
        num = re.findall(r'\d+\.\d+', f[i])
        text = re.sub(r'\(\d+\.\d+, \d+\.\d+\)', '', f[i]).strip()
        voc[text] = {}
        for j in range(len(f)):
            if i != j:
                text2 = re.sub(r'\(\d+\.\d+, \d+\.\d+\)', '', f[j]).strip()
                num2 = re.findall(r'\d+\.\d+', f[j])
                voc[text][text2] = distance(num[0], num[1], num2[0], num2[1])
    with open('spb_streets_voc.pkl', 'wb') as file:
        pickle.dump(voc, file)


make_voc()