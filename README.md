# Effective Mobile — Тестовое задание

Простое веб-приложение с backend на Python и Nginx в качестве reverse proxy, полностью контейнеризированное с помощью Docker и Docker Compose.

## Архитектура
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


## Troubleshooting 

Если что-то пошло не так — вот самые частые проблемы и способы их решения:

| Проблема                                      | Симптомы / Ошибка                                                                 | Решение                                                                                     |
|-----------------------------------------------|------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| curl: Failed to connect to localhost port 80  | `curl: (7) Failed to connect...`                                                   | 1. Проверьте `docker compose ps`<br>2. Освободите порт 80 (`sudo systemctl stop apache2` или аналог)<br>3. Или измените `NGINX_PORT=8080` в `.env` |
| 502 Bad Gateway от nginx                      | Nginx запускается, но возвращает 502                                               | 1. `docker compose logs backend`<br>2. Убедитесь, что backend не падает<br>3. Проверьте `proxy_pass http://backend/;` (слеш в конце обязателен) |
| NameError: name 'os' is not defined           | Backend падает сразу после запуска                                                | Добавьте `import os` в начало `backend/app.py`                                              |
| Permission denied в nginx (/var/cache/nginx)  | `[emerg] mkdir() ... failed (13: Permission denied)`                              | Удалите строку `USER nginx` из `nginx/Dockerfile` (самый простой и рекомендуемый способ)   |
| Контейнер backend restarts endlessly          | `docker compose ps` показывает restart                                             | Проверьте логи: `docker compose logs backend`<br>Обычно — ошибка в коде app.py             |
| curl работает, но отвечает HTML nginx         | Возвращает дефолтную страницу nginx                                               | Убедитесь, что вы удалили/перезаписали `/etc/nginx/conf.d/default.conf` в Dockerfile nginx |
| Изменения в коде не применяются               | После правок в app.py или nginx.conf ничего не меняется                           | `docker compose up -d --build` (флаг `--build` обязателен)                                 |

### Полезные команды для диагностики

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
