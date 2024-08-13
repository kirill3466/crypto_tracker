FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update -y
RUN apt-get upgrade -y

WORKDIR /app

COPY ./pyproject.toml ./poetry.lock* /app/
RUN pip install --no-cache-dir poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi


COPY . .

COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

# fix \r typos in entrypoint made by windows after copying to container
RUN apt-get install dos2unix
RUN dos2unix entrypoint.sh

ENTRYPOINT ["sh", "entrypoint.sh"]
