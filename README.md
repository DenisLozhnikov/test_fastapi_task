### Тестовое задание для Estesis. REST микросервис на FastAPI.


- База данных: PostgreSQL.

- ORM: SQLAlchemy.

- Валидаторы данных (схемы) - Pydantic.

### Как развернуть?

- С помощью Docker и Uvicorn, на локальном сервере (порт 8000).

`docker-compose up -d`

### Обработчики

- POST /tasks/add

Добавляет задачу в базу данных:

```
{
    "task_uuid": "UUID",
    "description": "тестовая задача",
    "params": {
        "param_1": "1",
        "param_2": 1
    }
}
```
- GET /tasks

Получает все существующие задачи.

- PUT /tasks/<task_sid>

Обновляет задачу по uuid.