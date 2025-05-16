ЗАДАНИЕ: АЛГОРИТМЫ, SELENIUM И ДОКУМЕНТАЦИЯ

ЧАСТЬ 1: АЛГОРИТМЫ НА PYTHON
Файл: algorithms.py

Что делает:
1.Получает список чисел от пользователя
2.Выводит чётные числа
3.Находит максимум и минимум
4.Сортирует список по возрастанию (без функции sorted)

ЧАСТЬ 2: АВТОМАТИЗАЦИЯ ТЕСТИРОВАНИЯ (SELENIUM)
Файл: test1.py

Что делает:
1.Открывает сайт https://example.com
2.Проверяет, что заголовок содержит "Example"
3.Находит и кликает по ссылке "More information..."
4.Проверяет, что открывается https://www.iana.org/help/example-domains

УСТАНОВКА:

1. Установить Python 3.10 или новее
2. Установить библиотеку Selenium:
   pip install selenium (или через python interpreter)
3. Скачать ChromeDriver с сайта:
   https://sites.google.com/chromium.org/driver/

Важно учесть, что версия ChromeDriver должна совпадать с версией браузера Google Chrome.
Положить исполняемый файл chromedriver в ту же папку, где находится скрипт.

ЗАПУСК:
В консоль пишем:
python test1.py

ИСПОЛЬЗУЕМЫЕ ВЕРСИИ:
1.Python: 3.12
2.Selenium: последняя версия
3.Chrome: 136.0.7103.114
