# Effective Mobile — Тестовое задание

Простое веб-приложение с backend на Python и Nginx в качестве reverse proxy, полностью контейнеризированное с помощью Docker и Docker Compose.

## Архитектура

```text
[Клиент / curl]
          │
          ▼   http://localhost
┌────────────────────────────┐
│          Nginx             │
│   (порт 80 на хосте)       │
│     reverse proxy          │
└──────────────┬─────────────┘
               │
               ▼ proxy_pass http://backend:8080/
               
┌────────────────────────────┐
│          Backend           │
│   Python HTTP-сервер       │
│       порт 8080            │
│ "Hello from Effective Mobile!" │
└────────────────────────────┘

(Backend доступен только внутри docker-сети app-network)
## Используемые технологии

- Python 3.12 (alpine)-(http.server)
- Nginx (stable-alpine)-(reverse proxy)
- Docker + Docker Compose
- Отдельная bridge-сеть
- Запуск без root (где возможно)

## Быстрый запуск

```bash
# 1. Клонировать репозиторий
git clone https://github.com/almazbek/EM-app.git
cd EM-app

# 2. (Опционально) настроить порт в .env
cp .env.example .env

# 3. Запустить
docker compose up -d --build

# 4. Проверить
curl http://localhost
Ожидаемый ответ:
Hello from Effective Mobile!

Остановка
docker compose down

Структура проекта

├── backend/
│   ├── Dockerfile
│   └── app.py
├── nginx/
│   ├── Dockerfile
│   └── nginx.conf
├── .env.example
├── .env                 (в .gitignore)
├── docker-compose.yml
├── .gitignore
└── README.md



## Полезные команды для диагностики

```bash
# Состояние контейнеров
docker compose ps

# Логи nginx (последние 30 строк)
docker compose logs nginx | tail -n 30

# Логи backend
docker compose logs backend

# Тест связи из nginx → backend
docker compose exec nginx curl -v http://backend:8080

# Перезапуск с полной пересборкой
docker compose down
docker compose up -d --build --force-recreate
