Markdown# Effective Mobile — Тестовое задание 🚀

Markdown# Effective Mobile — Тестовое задание

Простое веб-приложение с backend на Python и Nginx в качестве reverse proxy, полностью контейнеризированное с помощью Docker и Docker Compose.

## Архитектура
[Клиент / curl]
│
▼   http://localhost
┌─────────────────────┐
│     Nginx           │  ← порт 80 на хосте
│  reverse proxy      │
└──────────┬──────────┘
│ proxy_pass http://backend:8080/
▼
┌─────────────────────┐
│     Backend         │  ← Python HTTP-сервер
│  (порт 8080)        │    "Hello from Effective Mobile!"
└─────────────────────┘
(только внутри docker-сети app-network)
text## Используемые технологии

- Python 3.12 (alpine)
- http.server (стандартная библиотека)
- Nginx (stable-alpine)
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
textHello from Effective Mobile!
Остановка
Bashdocker compose down
Структура проекта
text├── backend/
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
