# homework-selenium

## Настройка окружения

```bash
python3 -m venv venv
sourсe venv/bin/activate
pip install -r requirements.txt
```

## Настройка окружения 
Создать .env файл формата:

```
EMAIL_ACCOUNT=test_test@mail.ru
PASSWORD_ACCOUNT=test_pw
```
Регистрация на сайте возможна только через О2 и был выбран почтовый сервис mail.ru

## Запуск
```bash
export ALLURE_OUTPUT_PATH=$(pwd)
./runner_tests.sh
```

## Просморт отчета
```bash
allure serve allure-results --host localhost --port 9999
```
