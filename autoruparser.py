import requests
from bs4 import BeautifulSoup
import csv
import lxml 
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def write_csv(f,model,desc,price,year,km):
    lenlist = len(model)
    i=0
    with open('BASE.csv', 'a') as f:
        writer = csv.writer(f)
        while i <= (lenlist-1):
            writer.writerow([model[i], desc[i], price[i], year[i],km[i]])
            i=i+1
 

 
def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')


    temp1 = soup.find_all('div', class_='listing-item__name') # models
    model = []
    for element in temp1:
      model.append(element.text)

    temp2 = soup.find_all('div', class_='listing-item__description') # description
    desc = []
    for element in temp2:
      string = (element.text).replace(u'\xa0', u' ') # delete '\xa0' 
      desc.append(string)

    temp3 = soup.find_all('div', class_='listing-item__price') # price
    price = []
    for element in temp3:
      string = (element.text).replace(u'\xa0', u' ') # delete '\xa0' 
      price.append(string)
    
    temp4 = soup.find_all('div', class_='listing-item__year') # year
    year = []
    for element in temp4:
      year.append(element.text)

    temp5 = soup.find_all('div', class_='listing-item__km') # km
    km = []
    for element in temp5:
      string = (element.text).replace(u'\xa0', u' ') # delete '\xa0' 
      km.append(string)
    
          
    return model,desc,price,year,km



def main():
    base_url = 'https://auto.ru/moskva/motorcycle/all/?beaten=1&custom_state_key=CLEARED&geo_id=213&geo_radius=200&image=true&sort_offers=cr_date-DESC&top_days=off&currency=RUR&output_type=list&page_num_offers='

    browser = webdriver.Firefox()
    f = open('BASE.csv', 'w')

    for i in range(1, 2):
        url_gen = base_url + str(i)
        print(url_gen) 
        browser.get(url_gen)
        html = browser.page_source
        model,desc,price,year,km=get_page_data(html)
        write_csv(f,model,desc,price,year,km) 

    f.close()
 
if __name__ == '__main__':
    main()
