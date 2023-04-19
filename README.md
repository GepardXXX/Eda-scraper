# __Eda_parser__
Данный скрипт парсит сайт [eda.ru](https://eda.ru/recepty/afishaeda/russkaya-kuhnya/osnovnye-blyuda?page=1)
____
## __Примеры__
Скрипт собирает данные и записывает их в файл .json:
```python
   {
        "Название блюда": "Голубцы",
        "Калорийность": "541 ккал",
        "Белки": "20 грамм",
        "Жиры": "35 грамм",
        "Углеводы": "37 грамм",
        "URL-ссылка": "https://eda.ru/recepty/osnovnye-blyuda/golubcy-114527"
    }
```
___
## __Установка__
```
pip install requests bs4 json
```
____
[Code](https://github.com/GepardXXX/eda_parser/blob/main/main/eda_parser.py)
