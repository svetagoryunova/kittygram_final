# kittygram_final

![example workflow](https://github.com/svetagoryunova/kittygram_final/actions/workflows/main.yml/badge.svg)

### Описание

Kittygram — социальная сеть для обмена фотографиями любимых питомцев.

### Как запустить проект:

**Настроить запуск проекта Kittygram в контейнерах и CI/CD с помощью GitHub Actions**

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:svetagoryunova/kittygram_final.git
```

**Шаг первый: настройка контейнеризации**

Напишите Dockerfile для образа kittygram_backend

Для создания образа kittygram_gateway используйте готовый Dockerfile из папки nginx/

Для создания образа kittygram_frontend используйте готовый Dockerfile из папки frontend/

Создайте файл .env для PostgreSQL c переменными с определёнными названиями:

- POSTGRES_USER — имя пользователя
- POSTGRES_PASSWORD — пароль пользователя
- POSTGRES_DB — имя базы данных

**Шаг второй: настройка CI/CD**

В файле .github/workflows/main.yml замените username на ваш логин на Docker Hub:

- username/kittygram_backend
- username/kittygram_frontend
- username/kittygram_gateway

Сделайте коммит с файлом main.yml и со всеми остальными изменёнными файлами, запушьте его в удалённый репозиторий:

```
/kittygram_final$ git add .
/kittygram_final$ git commit -m 'Add Actions'
/kittygram_final$ git push
```

### Технологии

Python 3.9, Django 3.2.3, djangorestframework 3.12.4, PostgreSQL 13.10, Docker

### Автор

[Светлана Горюнова](https://github.com/svetagoryunova)
