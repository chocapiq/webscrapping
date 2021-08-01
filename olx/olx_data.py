# scrapes data from olx to rent flat in Warsaw: price of rent, district and dependant on link returns number of
# rooms, area, level, if there are furnitures
import requests
from bs4 import BeautifulSoup
import csv
import re
import time

csv_file = open('scrapped_olx.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['dzielnica', 'cena', 'rodzaj_zabudowy', 'liczba pokoi', 'powierzchnia', 'poziom', 'umeblowanie'])

my_file = open('list_of_links.txt', 'r')
content = my_file.read()
content_list = content.split(" ")
del content_list[-1]

URL = content_list
print('...')
page_number = 0
for url_link in URL:
    print(url_link)

    launch_page = requests.get(url_link).text
    launch_soup = BeautifulSoup(launch_page, 'lxml')

    page_number += 1
    print(page_number)
    if page_number%100 == 0:
        time.sleep(4)

    # check legend.txt
    if 'floor_10' in url_link:
        floor = 10
    elif 'floor_11' in url_link:
        floor = 11
    else:
        floor = url_link.split('5D=floor_', 1)[1][0]

    if 'furniture%5D%5B0%5D=no' in url_link:
        furniture = 1
    elif 'furniture%5D%5B0%5D=yes' in url_link:
        furniture = 2
    else:
        furniture = 0

    if 'builttype%5D%5B0%5D=blok' in url_link:
        built_type = 1
    elif 'builttype%5D%5B0%5D=kamienica' in url_link:
        built_type = 2
    elif 'builttype%5D%5B0%5D=wolnostojacy' in url_link:
        built_type = 3
    elif 'builttype%5D%5B0%5D=szeregowiec' in url_link:
        built_type = 4
    elif 'builttype%5D%5B0%5D=apartamentowiec' in url_link:
        built_type = 5
    elif 'builttype%5D%5B0%5D=loft' in url_link:
        built_type = 6
    else:
        built_type = 0

    if 'float_m%3Ato%5D=' in url_link:
        area = url_link.split('float_m%3Ato%5D=', 1)[1][:2]
    elif 'float_m%3Afrom%5D=76' in url_link:
        area = 76
    else:
        area = 0

    if 'rooms%5D%5B0%5D=one' in url_link:
        rooms = 1
    elif 'rooms%5D%5B0%5D=two' in url_link:
        rooms = 2
    elif 'rooms%5D%5B0%5D=three' in url_link:
        rooms = 3
    elif 'rooms%5D%5B0%5D=four' in url_link:
        rooms = 4
    else:
        rooms = 0

    # finds out how many pages site has
    kappa = launch_soup.find('div', class_='pager rel clr')
    nr_pages = str(kappa).count('span')
    nr_pages = (nr_pages - 12) / 4
    numberOfPage = 1

    while numberOfPage <= nr_pages:
        url_link = url_link + '&page=' + str(numberOfPage)
        numberOfPage += 1
        page = requests.get(url_link).text

        soup = BeautifulSoup(page, 'lxml')

        apartment = soup.find('div', class_='offer-wrapper')

        for apartment in soup.find_all('div', class_='offer-wrapper'):

            price = apartment.find('p', class_='price')
            price = price.find('strong').get_text()

            for district in apartment.find_all('small', class_='breadcrumb x-normal'):
                district = str(district.find('span'))
                district = re.findall(r"Warszawa.*", district)
                for i in district:
                    if i is not None:
                        i = i.replace('</span>', '')
            csv_writer.writerow([i, price, built_type, rooms, area, floor, furniture])

'''    except:
        print('exception')
        continue'''