import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from webexample.models import FTTx

#URL = 'https://shop.nag.ru/catalog/01919.opticheskij-kabel/08679.fttx?count=20&default_view=2&filter_147_1=true&in_stock=&page=1&sort=popularity_desc'
#URL1 = 'https://shop.nag.ru/catalog/01919.opticheskij-kabel/06006.podvesnoj-samonesuschij-adss?count=20&default_view=2&filter_147_1=true&filter_148_0,6=true&in_stock=&page=1&sort=popularity_desc'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
           'accept': '*/*'}
HOST = 'https://shop.nag.ru'
VOLOKNA = [4, 8, 16, 32, 64]


#получение страницы для парсинга
def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

#получение данных со страницы
def get_content(html, volokno, kN=0):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='col-lg-3 col-lm-4 col-md-6 col-sm-12 col-xxl-25')
    cabel = []
    if kN:
        kN=kN
    for item in items:
        cabel.append({
            'name': item.find('div', class_='product-name slideup').get_text().replace('  file_copy ', ''),
            'link': HOST + item.find('a', class_='cut-clamp').get('href'),
            'price': item.find('div', class_='sale').get_text(strip=True).replace('\xa0', '').replace('От ',''),
            'volokna': volokno,
            'kN': kN
        })


    return  cabel

#получаем количество страниц
def get_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    pages = soup.find_all('ul', class_='flat-pagination style1')
    if pages:
        for page in pages:
            page = page.find_all('li')[-2].get_text(strip=True)
            return int(page)
    else:
        return 1


def get_kN(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('ul', class_='box-checkbox')
    items = items[2].find_all('li', class_='check-box')
    kN = []
    for item in items:
        a = item.get_text(strip=True).split('\n')
        kN.append(a[0])
    return kN




#парсинг
def parse_FTTx():
    cabel_FTTx = []
    for volokno in VOLOKNA:
        html = get_html(f'https://shop.nag.ru/catalog/01919.opticheskij-kabel/08679.fttx?count=20&default_view=2&filter_147_{volokno}=true&in_stock=&page=1&sort=popularity_desc')
        if html.status_code == 200:
            page_count = get_page(html.text)
            for page in range(1, page_count+1):
                print(f'Идет парсинг страницы {page} из {page_count}')
                html = get_html(f'https://shop.nag.ru/catalog/01919.opticheskij-kabel/08679.fttx?count=20&default_view=2&filter_147_{volokno}=true&in_stock=&page=1&sort=popularity_desc', params= {'page': page})
                cabel_FTTx.extend(get_content(html.text, volokno))
        else:
            print('Error')
    for i in range(0, len(cabel_FTTx)):
       try:
           fttx = FTTx.objects.get(link = cabel_FTTx[i]['link'])
           fttx.name = cabel_FTTx[i]['name']
           fttx.volokno = int(cabel_FTTx[i]['volokna'])
           fttx.kN = cabel_FTTx[i]['kN']
           fttx.price = int(cabel_FTTx[i]['price'])
           fttx.save()
       except FTTx.DoesNotExist:
           fttx = FTTx(
                name = cabel_FTTx[i]['name'],
                volokno = int(cabel_FTTx[i]['volokna']),
                kN = cabel_FTTx[i]['kN'],
                price = int(cabel_FTTx[i]['price']),
                link = cabel_FTTx[i]['link'],
            ).save()
    print(f'cabel {fttx}')


#парсинг
def parse_ADSS():
    cabel_ADSS = []
    for volokno in VOLOKNA:
        html = get_html(f'https://shop.nag.ru/catalog/01919.opticheskij-kabel/06006.podvesnoj-samonesuschij-adss?count=20&default_view=2&filter_147_{volokno}=true&in_stock=&page=1&sort=popularity_desc')
        if html.status_code == 200:
            page_count = get_page(html.text)
            for page in range(1, page_count+1):
                print(f'Идет парсинг страницы {page} из {page_count}')
                html = get_html(f'https://shop.nag.ru/catalog/01919.opticheskij-kabel/06006.podvesnoj-samonesuschij-adss?count=20&default_view=2&filter_147_{volokno}=true&in_stock=&page=1&sort=popularity_desc', params= {'page': page})
                cabel_ADSS.extend(get_content(html.text, volokno))
        else:
            print('Error')
    print(cabel_ADSS)


#класс команды
class Command(BaseCommand):
    help = 'Parser'

    def handle(self, *args, **options):
        parse_FTTx()
        #parse_ADSS()
