FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update -y
RUN apt-get upgrade -y

WORKDIR /app

COPY ./requirements.txt ./
RUN pip install -r requirements.txt


COPY . .

COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

# fix \r typos in entrypoint made by windows after copying to container
RUN apt-get install dos2unix
RUN dos2unix entrypoint.sh

ENTRYPOINT ["sh", "entrypoint.sh"]
