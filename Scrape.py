import unicodedata
import requests
from bs4 import BeautifulSoup
import csv
from multiprocessing import Pool
import urllib3
import time


def get_html(url):
    # Authoriztion with requests with session saving also headers could be added
    # s = requests.session()
    # url_1 = 'LOGIN_PAGE'
    # values = {'login':'YOURLOGIN','password':'YOURPASS'}
    # r_1 = s.post(url, data=values, verify=False)
    r = requests.get(url) #if authorization is needed pass session here.
    return r.text

def all_pages(html):
    pages = [str(i) for i in range(1,10)] #range of pages
    links = [] #dictionary with all links to pass to pool's map function
    for page in pages:
        html = 'https://statesassembly.gov.je/Pages/Members.aspx?MemberID='+page
        links.append(html) #append to a dictionary
    return links
def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml') #Soup object
    name = soup.find('h1').text#Finding Name
    title = soup.find(class_='gel-layout__item gel-2/3@m gel-1/1@s').find('h2').text #Finding position
# Addind to dictionary
    data = {'name': name,
            'title': title,
            }

    return (data)

# import to CSV
def write_csv(data):
    with open('Members.csv','a') as output_file:
        writer = csv.writer(output_file, delimiter=';') #using ';' delimeter for Excel
        writer.writerow((data['name'],
                        data['title'],
                        ))
    print(data['name'],'done') #printing results

#defining function for multiprocessing Pool
def mps(url):
    html = get_html(url)
    data = get_page_data(html)
    write_csv(data)


def main():
    while True:
        try:
            url = 'https://statesassembly.gov.je/Pages/Members.aspx?MemberID='
            all_links = all_pages(get_html(url))
            with Pool(10) as p: #Pool number of processes
                p.map(mps,all_links) #map function + dictionary
        except:
            time.sleep(5) # trying to reconnect after 5 seconds

if __name__ == '__main__':
    main()
