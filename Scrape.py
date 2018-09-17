import requests
from bs4 import BeautifulSoup
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# Authoriztion with requests with session saving
# s = requests.session()
# url = 'LOGIN_PAGE'
# values = {'login':'YOURLOGIN','password':'YOURPASS'}
# r = s.post(url, data=values, verify=False)

pages = [str(i) for i in range(100,200)] #number of pages you want to pass

#Iteration through the numbers pf pages and scrape data with BeautifulSoup

for page in pages:
    try:
        html = requests.get('https://statesassembly.gov.je/Pages/Members.aspx?MemberID='+page).text
        def get_page_data():
            soup = BeautifulSoup(html, 'lxml') #Soup object
            name = soup.find('h1').text #Finding Name
            title = soup.find(class_='gel-layout__item gel-2/3@m gel-1/1@s').find('h2').text #Finding position
# Addind to dictionary
            data = {'name': name,
                    'title': title,
                    }

            return (data)

    except requests.exceptions.ConnectionError: #excepting connecting error which I encountered recently
        continue

    data = get_page_data()
    # import to CSV
    with open('Members.csv','a') as output_file:
        writer = csv.writer(output_file, delimiter=';') #using ';' delimeter for Excel
        writer.writerow((data['name'],
                        data['title'],
                        ))
