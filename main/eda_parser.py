import requests
import json
from bs4 import BeautifulSoup as bs


def get_data(url):
    headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
    }

    data_list = []
    total = 16
    print(f'Всего страниц: {total}')

    for page in range(1,17):
        req = requests.get(f'{url}={page}', headers=headers)
        soup = bs(req.text, 'lxml')
        
        all_href = []

        all_elements = soup.find_all('a', 'emotion-18hxz5k')

        for element in all_elements:
            href = f'https://eda.ru{element.get("href")}'
            all_href.append(href)
        
        for href in all_href:
            req = requests.get(href, headers=headers)
            soup = bs(req.text, 'lxml')
            name = soup.find('h1', 'emotion-gl52ge').text
            categories = soup.find_all('div', 'emotion-8fp9e2')

            data_list.append(
                {
                'Название блюда': name.strip(),
                'Калорийность': f'{categories[0].text} ккал',
                'Белки': f'{categories[1].text} грамм',
                'Жиры': f'{categories[2].text} грамм',
                'Углеводы': f'{categories[3].text} грамм',
                'URL-ссылка': href
                }
            )

            with open('main\data.json', 'w', encoding='utf-8') as f:
                json.dump(data_list, f, indent=4, ensure_ascii=False)

        if total == 0:
            print('Сбор данных завершён')
        else:
            print(f'Информация со страницы {page} обработана')
            total -= 1

        
def main():
    get_data('https://eda.ru/recepty/afishaeda/russkaya-kuhnya/osnovnye-blyuda?page')


if __name__ == '__main__':
    main()
