FROM python:3.10-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY src/ /app/src/

RUN apt-get update && apt-get install \
  curl libpq-dev vim glpk-utils coinor-cbc gcc python3-dev python3-pip musl-dev \
  -y --no-install-recommends

COPY local.env /app/.env
COPY README.md /app/

COPY pyproject.toml /app/
COPY requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN addgroup --system app && adduser --system --group app

USER app

CMD gunicorn -w 4 -k uvicorn.workers.UvicornWorker 'src.app:create_app()' -b 0.0.0.0:8000

EXPOSE 8000