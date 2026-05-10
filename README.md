# Restaurant Ordering System 🍕

Групповой проект по созданию веб-сервиса доставки еды. Проект разделен на Backend (FastAPI) и Frontend (в разработке).

## 🚀 Быстрый запуск (Docker)

Для запуска всего проекта (база + бэкенд) вам понадобится только Docker и Docker Compose.

1.  **Создайте файл `.env`** в корне (можете скопировать из `.env.example`):
    ```bash
    cp .env.example .env
    ```
2.  **Запустите проект**:
    ```bash
    docker-compose up --build
    ```
    API будет доступно по адресу: [http://localhost:8000](http://localhost:8000)
    Документация Swagger: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🛠 Технологический стек

- **Backend**: Python 3.11, FastAPI, SQLAlchemy 2.0
- **Database**: PostgreSQL 16
- **Migrations**: Alembic
- **DevOps**: Docker, Docker Compose, GitHub Actions (CI/CD)

---

## 📖 Инструкция для разработчиков

### 📦 Структура проекта
```text
.
├── backend/            # Исходный код бэкенда
│   ├── app/            # Логика FastAPI (main, models, schemas)
│   ├── migrations/     # Миграции базы данных (Alembic)
│   └── Dockerfile      # Конфиг сборки бэкенда
├── frontend/           # Клиентская часть (в разработке)
├── docker-compose.yml  # Оркестрация сервисов
└── .github/workflows   # Настройки CI/CD (GitHub Actions)
```

### 🗄 Работа с базой данных (Миграции)
Мы используем **Alembic**. Все изменения в `models.py` должны сопровождаться миграцией.

**Создание миграции (после изменения моделей):**
```bash
docker exec -it restaurant_backend alembic revision --autogenerate -m "Описание изменений"
```

**Применение миграций:**
Происходит автоматически при запуске контейнера через `start.sh`.

### 🧪 Линтинг
Перед пушем кода рекомендуется проверять его на соответствие стандартам:
```bash
# Проверка
ruff check backend

# Исправление мелких ошибок и форматирование
ruff check backend --fix
ruff format backend
```

---

### 🚢 CI/CD (GitHub Actions)
В репозитории настроен пайплайн:
1.  При каждом пуше или PR запускается линтер.
2.  При пуше в ветку `main` собирается Docker-образ и пушится на Docker Hub.
