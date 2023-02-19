FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /mysite

RUN apt-get update && apt-get install nano

COPY . .

RUN pip install -r req.txt

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]