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
- **Auth**: JWT, Passlib (bcrypt)
- **Database**: PostgreSQL 16
- **Migrations**: Alembic
- **Testing**: Pytest, HTTPX
- **DevOps**: Docker, GitHub Actions (CI/CD)

---

## 📖 Инструкция для разработчиков

### 📦 Структура проекта
```text
.
├── backend/            # Исходный код бэкенда
│   ├── routers/        # Эндпоинты API
│   ├── migrations/     # Миграции базы данных (Alembic)
│   ├── tests/          # Автотесты (Pytest)
│   ├── models.py       # Модели SQLAlchemy
│   ├── auth.py         # Логика безопасности и JWT
│   └── Dockerfile      # Конфиг сборки бэкенда
├── frontend/           # Клиентская часть (в разработке)
├── docker-compose.yml  # Оркестрация сервисов
└── .github/workflows   # Настройки CI/CD (тесты и деплой)
```

### 🧪 Тестирование и Линтинг
Перед пушем кода обязательно запускайте тесты и проверку стиля:

```bash
# Запуск тестов (локально из папки backend)
cd backend
pytest tests

# Проверка стиля (из корня)
ruff check backend
```

### 🗄 Работа с базой данных (Миграции)
Мы используем **Alembic**. Все изменения в `models.py` должны сопровождаться миграцией.

**Создание миграции:**
```bash
docker exec -it restaurant_backend alembic revision --autogenerate -m "Описание изменений"
```

---

### 🚢 CI/CD (GitHub Actions)
В репозитории настроены два пайплайна:
1.  **Tests**: Запускается при каждом Push/PR. Проверяет код линтером и прогоняет все тесты.
2.  **Docker Publish**: Запускается при пуше в `main`. Собирает образ и пушит его в Docker Hub.
