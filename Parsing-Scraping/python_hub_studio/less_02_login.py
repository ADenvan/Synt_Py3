from requests import Session  # Для сохранения фаилов coocu.
from bs4 import BeautifulSoup
from time import sleep

# Заголовок браузера.
headers = {"User-Agent" : "https://translated.turbopages.org/proxy_u/en-ru.ru.ef421a52-655f299f-c5fc7083-74722d776562/https/i.stack.imgur.com/1dolH.png "}


work = Session()

# Вход на страницу.
work.get("https://quotes.toscrape.com/", headers=headers)

# Нажимаем на кнопку ЛИГИНА. С формай авторизации.
response = work.get("https://quotes.toscrape.com/login", headers=headers)

# Разбираем форму.
soup = BeautifulSoup(response.text, "lxml")

# Вытягиваем ключь (ТОКЕН)
token = soup.find("form").find("input").get("value")

# Фармируем словарь.
data = {"csrf_token": token, "username": "noname", "password": "password"}

result = work.post("https://quotes.toscrape.com/login", headers=headers, data=data, allow_redirects=True)

result = soup.find_all("span", class_="text")
author = soup.find_all("small", class_="author")

# Проверка всех страниц с текстом.
# if len(result) != 0:
#     print(result)
# else:
#     break
