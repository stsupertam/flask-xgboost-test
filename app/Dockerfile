FROM python:3.7.6-buster

WORKDIR /app

COPY . /app
RUN pip install -r /app/requirements.txt

# --- Nginx Setup ---
WORKDIR /
COPY scripts/install-nginx-debian.sh /
RUN bash /install-nginx-debian.sh

COPY config/nginx/default.conf /etc/nginx/conf.d/
RUN chmod g+rwx /var/cache/nginx /var/run /var/log/nginx
RUN chgrp -R root /var/cache/nginx
RUN sed -i.bak 's/^user/#user/' /etc/nginx/nginx.conf
RUN addgroup nginx root

EXPOSE 8080
CMD gunicorn --bind 0.0.0.0:5000 wsgi --chdir /app & nginx -g 'daemon off;'