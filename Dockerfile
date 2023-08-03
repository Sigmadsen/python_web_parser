FROM python:3.10-slim

RUN apt-get update \
    && rm -rf /var/lib/apt/lists/* \
    && python -m pip install --upgrade pip \
    && pip install -r requirements.txt

ENTRYPOINT ["docker/test.sh"]
