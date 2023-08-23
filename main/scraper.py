import requests
import json
from bs4 import BeautifulSoup as bs


# Функция для получения данных о рецептах
def get_data(url):
    headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
    }

    data_list = []  # Список для хранения данных о рецептах
    total = 16  # Общее количество страниц
    print(f'Всего страниц: {total}')

    # Перебираем страницы
    for page in range(1,17):
        req = requests.get(f'{url}={page}', headers=headers)
        soup = bs(req.text, 'lxml')
        
        all_href = []

        # Ищем ссылки на рецепты на текущей странице
        all_elements = soup.find_all('a', 'emotion-18hxz5k')

        for element in all_elements:
            href = f'https://eda.ru{element.get("href")}'
            all_href.append(href)
        
        # Обрабатываем каждую ссылку на рецепт
        for href in all_href:
            req = requests.get(href, headers=headers)
            soup = bs(req.text, 'lxml')
            name = soup.find('h1', 'emotion-gl52ge').text
            categories = soup.find_all('div', 'emotion-8fp9e2')

            # Добавляем данные о рецепте в список
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

            # Сохраняем данные в JSON-файл
            with open('main\data.json', 'w', encoding='utf-8') as f:
                json.dump(data_list, f, indent=4, ensure_ascii=False)

        if total == 0:
            print('Сбор данных завершён')
        else:
            print(f'Информация со страницы {page} обработана')
            total -= 1


# Функция для запуска парсера
def main():
    get_data('https://eda.ru/recepty/afishaeda/russkaya-kuhnya/osnovnye-blyuda?page')

# Запуск парсера при выполнении скрипта напрямую
if __name__ == '__main__':
    main()
