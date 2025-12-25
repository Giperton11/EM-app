FROM python:3.11-alpine

LABEL maintainer="Giperton11@gmail.com" \
      description="Simple HTTP server for Effective Mobile test task" \
      version="1.0"

WORKDIR /app

RUN addgroup -S appgroup && adduser -S appuser -G appgroup

COPY --chown=appuser:appgroup app.py .

USER appuser

ENV BACKEND_PORT=8080

EXPOSE ${BACKEND_PORT:-8080}

CMD ["python", "app.py"]

