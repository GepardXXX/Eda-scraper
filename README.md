# Eda parser
[![GitHub license](https://img.shields.io/github/license/GepardXXX/Message-Collector-bot)](https://github.com/GepardXXX/Message-Collector-bot/blob/main/LICENSE)
[![Python Version](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100)
![GitHub repo size](https://img.shields.io/github/repo-size/GepardXXX/Message-Collector-bot)

Этот проект представляет собой парсер для сбора информации о рецептах блюд с сайта [eda.ru](https://eda.ru/recepty/afishaeda/russkaya-kuhnya/osnovnye-blyuda?page=1)

## Требования

Для корректной работы проекта необходимо наличие следующих программ и библиотек:

- Python 3.x
- Библиотека BeautifulSoup (`beautifulsoup4`)
- Библиотека requests

Установить все необходимые зависимости можно с помощью команды:

```bash
pip install -r requirements.txt
```
## Структура проекта
```css
eda_parser/
├── main/
│   ├── data.json
│   └── eda_parser.py
├── README.md
└── requirements.txt
```
- `data.json` - JSON-файл, в который сохраняется информация о рецептах блюд.
- `eda_parser.py` - Скрипт для парсинга рецептов с сайта eda.ru.
- `requirements.txt` - Файл со списком зависимостей, необходимых для проекта.

## Использование
1. Установите необходимые зависимости, выполнив команду:

```bash
pip install -r requirements.txt
```
2. Запустите скрипт eda_parser.py:

```bash
python main/eda_parser.py
```
Скрипт начнет собирать информацию о рецептах с сайта eda.ru и сохранять ее в файл `data.json`

### Как это работает?
Скрипт eda_parser.py выполняет следующие действия:
1. Загружает страницы с рецептами с сайта eda.ru.
2. Извлекает информацию о названии блюда, калорийности, содержании белков, жиров и углеводов.
3. Сохраняет собранную информацию в файл `data.json`.

## Связь
Если у вас есть какие-либо вопросы, предложения или проблемы с этим проектом, вы можете связаться со мной через [__GitHub__](https://github.com/GepardXXX) или [__Telegram__](https://t.me/GepardXXX).