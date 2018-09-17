import requests
from bs4 import BeautifulSoup
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

pages = [str(i) for i in range(100,200)]
for page in pages:
    html = requests.get('https://statesassembly.gov.je/Pages/Members.aspx?MemberID='+page).text
    def get_page_data():
        soup = BeautifulSoup(html, 'lxml')
        name = soup.find('h1').text
        title = soup.find(class_='gel-layout__item gel-2/3@m gel-1/1@s').find('h2').text
        data = {'name': name,
                'title': title,
                }

        return (data)

    data = get_page_data()
    with open('Members.csv','a') as output_file:
        writer = csv.writer(output_file, delimiter=';')
        writer.writerow((data['name'],
                        data['title'],
                        ))
