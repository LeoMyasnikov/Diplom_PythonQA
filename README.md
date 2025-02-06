# Автоматизированный тестовый набор для диплома по курсу Python

Проект включает:
Автоматизированные тесты с использованием Selenium WebDriver.
Генерацию отчетов о тестировании с помощью Allure.
Пример структуры проекта, основанной на паттерне Page Object.

## Предварительные требования
- Python 3.8+
- Selenium WebDriver
- pip
- pytest
- ChromeDriver
- Allure для генерации отчетов

## Установка
1. Клонируйте репозиторий:git clone https://github.com/LeoMyasnikov/Diplom_PythonQA.git
2. Перейдите в каталог проекта:cd project-name
3. Установите зависимости: pip install -r requirements.txt
4. Установите зависимости: pip install pytest allure-pytest

## Использование
Чтобы запустить все тесты: python -m pytest tests --alluredir allure-results 
Чтобы запустить конкретный тест: python -m pytest tests/test_example.py --alluredir allure-results
Чтобы сгенерировать отчет о тестах: allure generate /allure-results --clean -o ./allure-report
Чтобы открыть отчет: allure open ./allure-report


## Структура тестов
- `сore/`: Содержит базовые классы, которые используются во всем проекте
  -`base`: Содержит общие методы, такие как поиск элементов, проверки видимости, ввод текста и т.д

- `data/`: Содержит данные, используемые в тестах, такие как учетные данные, конфигурации и другие параметры
  - `cridentials`: Файл с учетными данными, в моем случае с доменом. Чтобы избежать хардкода в тестах

- `pages/`: классы, реализующие Page Object Model для различных страниц веб-приложения. Каждый файл представляет отдельную страницу или функциональность. 
  - `edit_page.py`: Включает класс для страницы редактирования данных входа пользователя (например, смены пароля)
  - `login_page.py`: Включает класс для страницы авторизации 
  - `personal_page.py`: Включает класс для персональной страницы пользователя, идущей после авторизации. Из этой страницы можно переходить на другие станции
  - `scanning_page.py`: Включает класс для страницы сканирования. Веб-станция Сканирования предназначена для ввода отсканированных документов, формирования пакетов и отправки их для дальнейшей обработки

- `tests/`: Содержит тестовые сценарии, организованные по функциональности. Каждый файл тестов соответствует определенной странице или набору функций
  - `conftest.py`: Представляет собой настройку фикстуры driver для Pytest, которая используется для инициализации и управления экземпляром браузера Google Chrome через Selenium WebDriver.
  - `test_edit_page.py`: Представляет собой набор автоматизированных тестов для страницы редактирования пользовательских данных
  - `test_login_page.py`: Представляет собой набор автоматизированных тестов для страницы авторизации
  - `test_scanning_page.py`: Представляет собой набор автоматизированных тестов для страницы сканирования

- `allure-report/`: Папка для результатов Allure

