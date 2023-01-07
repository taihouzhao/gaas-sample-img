FROM ghcr.io/taihouzhao/gaas-docker-base:v1.4.4

COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir --upgrade -r /requirements.txt

COPY . /app
WORKDIR /app

ENTRYPOINT python main.py