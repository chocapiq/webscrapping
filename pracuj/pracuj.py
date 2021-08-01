import requests
from bs4 import BeautifulSoup
import csv
import random
import time

csv_file = open('praca.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Nazwa oferty', 'Link oferty pracy', 'Który link', 'Data'])

URL = ['https://www.pracuj.pl/praca/czestochowa;wp?rd=30',
       'https://www.pracuj.pl/praca?rd=30&rw=true',
       'https://www.pracuj.pl/praca?rd=30&et=17',
       'https://www.pracuj.pl/praca/python;kw?rd=30&et=1%2c3%2c17']
look_for = ['test', 'python', 'commerce', 'analy', 'anali', 'data', 'dane', 'danych', 'program', 'software']
link_list = []

for i in URL:

    for j in range(1, 40):
        a = random.random()
        time.sleep(a)
        url_link = i + '&pn=' + str(j)
        launch_page = requests.get(url_link).text
        launch_soup = BeautifulSoup(launch_page, 'lxml')

        praca_names = launch_soup.find_all('a', class_='offer-details__title-link')
        what_links = launch_soup.find_all('li', class_='offer-labels__item offer-labels__item--location')
        dates = launch_soup.find_all('span', class_='offer-actions__date')
        for (praca_name, what_link, date) in zip(praca_names, what_links, dates):
            praca_link = str(praca_name)
            praca_link = praca_link.split('\"')
            for v in range (len(praca_link) - 1):
                if 'http' in praca_link[v]:
                    praca_link = praca_link[v]
            praca_name = praca_name.text
            what_link = what_link.text
            date = date.text
            date = date.split('\n')
            date = date[1]

            if 'lipca' in date.lower():
                break

            if 'zdalna' in what_link.lower():
                what_link = 'zdalna'
            elif 'częstochowa' in what_link.lower():
                what_link = 'Częstochowa'
            else:
                what_link = 'Inne'
            print(praca_name, what_link, date)
            if 'senior' or 'starszy' not in praca_name:
                for keyword in look_for:
                    if keyword in praca_name.lower():
                        if praca_link in link_list:
                            break
                        link_list.append(praca_link)
                        csv_writer.writerow([praca_name, praca_link, what_link, date])
                        break
                    elif 'IT' in praca_name:
                        if praca_link in link_list:
                            break
                        link_list.append(praca_link)
                        csv_writer.writerow([praca_name, praca_link, what_link, date])

