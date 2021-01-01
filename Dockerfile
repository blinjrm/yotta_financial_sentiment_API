FROM python:3.8

WORKDIR /app

RUN pip3 install poetry
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./
COPY ./app ./
RUN poetry install --no-dev

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
