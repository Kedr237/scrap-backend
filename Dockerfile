FROM python:3.11.9

RUN apt-get update \
    && apt-get install -y netcat-traditional

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip --no-cache-dir \
    && pip install -r requirements.txt --no-cache-dir

COPY . .

EXPOSE ${ROOT_PORT}

ENTRYPOINT ["sh", "entrypoint.sh"]
