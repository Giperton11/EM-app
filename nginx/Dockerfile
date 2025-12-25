FROM nginx:stable-alpine

# Метаинформация
LABEL maintainer="Giperton11@gmail.com" \
      description="Nginx reverse proxy for Effective Mobile test task" \
      version="1.0"

RUN rm -f /etc/nginx/nginx.conf

COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]

