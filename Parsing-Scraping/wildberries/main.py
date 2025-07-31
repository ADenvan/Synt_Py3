import requests
import json



def finde_item(response, id_articul: int):
  for ind, val in enumerate(response.json()["products"]):
    if int(val["id"]) == id_articul:
      return ind + 1

def get_page():
  page = 1
  headers = {
    'accept': '*/*',
    'accept-language': 'ru,en;q=0.9',
    'origin': 'https://www.wildberries.ru',
    'priority': 'u=1, i',
    'referer': 'https://www.wildberries.ru/catalog/0/search.aspx?search=%D0%BD%D0%B0%D1%83%D1%88%D0%BD%D0%B8%D0%BA%D0%B8%20%D0%B1%D0%B5%D1%81%D0%BF%D1%80%D0%BE%D0%B2%D0%BE%D0%B4%D0%BD%D1%8B%D0%B5',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    'x-captcha-id': 'Catalog 1|1|1752912588|AA==|69826acb1d2e4f9594077c26a9da3de7|S0gVLv75RiIG3tbitaPnd8lWvCBCytJOLSAU6k0FTRg',
    'x-queryid': 'qid516681524173400007220250718125815',
    'x-userid': '0',
  }

  while True:
    print(page)
    response = requests.get(
      'https://search.wb.ru/exactmatch/ru/common/v14/search?ab_testid=brandoriginaloff&appType=1&curr=rub&dest=123589415&hide_dtype=13;14&lang=ru&page=F{page}&query=%D0%BD%D0%B0%D1%83%D1%88%D0%BD%D0%B8%D0%BA%D0%B8%20%D0%B1%D0%B5%D1%81%D0%BF%D1%80%D0%BE%D0%B2%D0%BE%D0%B4%D0%BD%D1%8B%D0%B5&resultset=catalog&sort=popular&spp=30&suppressSpellcheck=false',
      headers=headers,)
    if len(response.json()) != 0:
      result = finde_item(response, 444266900)
      if result:
        return (page - 1) * 100 + result
    else:
      return None
    page += 1

  # with open('json.json', "w", encoding="utf-8") as file:
  #   json.dump(response.json(), file)

def main():
  log = get_page()
  print(log)

if __name__ == '__main__':
  main()
  