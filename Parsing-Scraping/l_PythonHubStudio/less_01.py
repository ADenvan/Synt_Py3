import requests
from bs4 import BeautifulSoup
from time import sleep


# Заголовок браузера.
headers = {"User-Agent" : "https://translated.turbopages.org/proxy_u/en-ru.ru.ef421a52-655f299f-c5fc7083-74722d776562/https/i.stack.imgur.com/1dolH.png "}


# Загруска фото.
def download(url):
    # Должна быть потокавая передача.
    # stream=True -Будет грузиться не сразу а по частям.
    resp = requests.get(url, stream=True)
    # Создаем фаил в которы запишем байты полученого изображения.
    r = open("D:\\Lan-Python\\Project\\Parsing-Scraping\\BfS4_Requ\\imags\\" + url.split("/")[-1], "wb")

    for value in resp.iter_content(1024):
        # Позволит перемещяться по потоку передаваемых данных
        r.write(value)
    r.close()

# Функция генератор. В целях экономии Памяти.
def get_url():
    # Цикл перебора страниц
    for count in range(1, 2):
        url = f"https://scrapingclub.com/exercise/list_basic/?page={count}"

        # Получаем первую страничку товаров
        response = requests.get(url, headers=headers)

        # Парсим. Получаем данные со страницы.
        soup = BeautifulSoup(response.text, "lxml")

        # Находим карточку товара. Первая попавшася карточка.
        data = soup.findAll("div", class_="w-full rounded border")

        # Проходим циклом по data -и собираем все href в СПИСОК.
        for i in data:
            
            card_url = "https://scrapingclub.com" + i.find("a").get("href")
            yield card_url


# Функция Генератор. В целях экономии Памяти.
def array():
    # Циклом проходим в каждую отдельно и собираем все ее информацию.
    for card_url in get_url():
        response = requests.get(card_url, headers=headers)
        sleep(3)
        # Получаем данные со страницы.
        soup = BeautifulSoup(response.text, "lxml")

        # Находим карточку товара. Первая попавшася карточка.
        # data = soup.find("p", class_="card-description")
        data = soup.find("div", class_="my-8 w-full rounded border")

        name = data.find("h3", class_="card-title").text
        price = data.find("h4", class_="my-4 card-price").text
        text = data.find("p", class_="card-description").text
        url_img = "https://scrapingclub.com" + data.find("img", class_="card-img-top").get("src")

        download(url_img)
        yield name, price, text, url_img
