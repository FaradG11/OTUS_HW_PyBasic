
#   Чтобы запустить контейнер используйте
#   команду 'docker run -it-p 8000:8000 app'

FROM python:3.9-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /homework_03

RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./
RUN poetry install

COPY app .

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host=0.0.0.0", "--port=8000"]