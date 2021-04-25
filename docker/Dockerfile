FROM python:3.9-slim
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libc-dev \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir "uvicorn[standard]" gunicorn fastapi graphene \
    && apt-get purge -y --auto-remove gcc libc-dev
COPY docker/start.sh docker/start-reload.sh docker/gunicorn_conf.py /
COPY ./fastapi-graphql /app
WORKDIR /app/
ENV PYTHONPATH=/app
EXPOSE 80
# Run the start script, it will check for an /app/prestart.sh script (e.g. for migrations)
# And then will start Gunicorn with Uvicorn
CMD ["/start.sh"]
