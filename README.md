# Задача по PostgreSQL

## Дано

Файл от 500 мб до 1 гб

## Требуется

Сохранить файл в бд в поле типа bytea

При этом:
- размер таблицы не должен превышать размер файла более чем на 10%
- нельзя использовать LargeObject (lo_*)
- данные одного файла нужно сохранить в одной строке в таблице
- нельзя использовать ORM

### Установка и запуск

- Установить python3.9, pipenv, postgresql
- Склонировать репозиторий
- Установить зависимости с помощью команды `pipenv install`
- Создать в psql пустую БД и пользователя с правами **SUPERUSER** и с паролем
- В файле [settings.py](./settings.py) заменить данные на корректные

*Генерация файла*

```bash
sudo pipenv run generate.py
```

*Сохранение файла в бд*

```bash
sudo pipenv run upload.py
```