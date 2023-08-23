# Eda scraper
[![GitHub license](https://img.shields.io/github/license/GepardXXX/eda_parser)](https://github.com/GepardXXX/Eda-scraper/blob/main/LICENSE)
[![Python Version](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100)
![GitHub repo size](https://img.shields.io/github/repo-size/GepardXXX/Eda-scraper)

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
Eda-scraper/
├── main/
│   ├── data.json
│   └── scraper.py
├── README.md
├──LICENSE
└── requirements.txt
```
- `scraper.py` - Скрипт для парсинга рецептов с сайта eda.ru.
- `README.md`: Файл, содержащий описание проекта, инструкции по использованию и связи.
- `LICENSE`: Файл с лицензией, определяющей условия распространения и использования вашего кода.
- `data.json` - JSON-файл, в который сохраняется информация о рецептах блюд.
- `requirements.txt` - Файл со списком зависимостей, необходимых для проекта.

## Использование
1. Установите необходимые зависимости, выполнив команду:

```bash
pip install -r requirements.txt
```
2. Запустите скрипт `scraper.py`:

```bash
python main/scraper.py
```
Скрипт начнет собирать информацию о рецептах с сайта eda.ru и сохранять ее в файл `data.json`

### Как это работает?
Скрипт eda_parser.py выполняет следующие действия:
1. Загружает страницы с рецептами с сайта eda.ru.
2. Извлекает информацию о названии блюда, калорийности, содержании белков, жиров и углеводов.
3. Сохраняет собранную информацию в файл `data.json`.

## Связь
Если у вас есть какие-либо вопросы, предложения или проблемы с этим проектом, вы можете связаться со мной через [__GitHub__](https://github.com/GepardXXX) или [__Telegram__](https://t.me/GepardXXX).