# Инструкция по развертыванию

## Требования
- Docker
- Docker Compose

## Инструкция

1. Клонировать репозиторий:
```bash
git clone <ссылка на репозиторий>
cd <название папки>
```

2. Создать файл `.env` из шаблона:
```bash
cp backend/.env.template backend/.env
```

3. Заполнить переменные в `backend/.env`:
```
DATABASE_URL=postgresql://user:password@postgres:5432/dbname
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=dbname
```

4. Запустить все сервисы:
```bash
docker compose up -d
```

5. Применить миграции:
```bash
docker exec -it flask uv run alembic upgrade head
```

6. Открыть в браузере:
- Форма: http://localhost/form
- Данные: http://localhost/info