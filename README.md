# Подсистема авторизации DH

---

## Описание 

Базовые механизмы авторизации в приложениях экосистемы DH

---

## Состав

* ```celery_tasks``` - отложенные задачи
* ```exceptions``` - исключения
* ```helpers``` - вспомогательные функции
  * ```get_token``` - получение токена из запроса
  * ```get_user_id_from_token``` - получение идентификатора пользователя из токена
* ```models``` - модели
* ```repository``` - репозитории для работы с данными
* ```routes``` - конечные точки
* ```schemas``` - схемы данных
* ```services``` - сервисы
* ```config``` - конфигурация приложения
* ```consts``` - константы
---

## Подключение

Для подключения используется команда:
```bash
poetry add git+https://github.com/JohnSoi/dh-auth.git
```

В файл ```migrations/env.py``` нужно добавить импорт моделей:
```python
from dh_auth.models import *
```

В файле ```.env``` должны быть следующие поля:

```dotenv
SECRET_KEY=
CRYPTO_CONTEXT_SCHEME=
ENCODE_ALGORITHM=
TOKEN_EXPIRE_DAY=
TOKEN_COOKIE_NAME=
CELERY_AUTH_NAME=
```