FROM python:3.8.5

WORKDIR /test
COPY . .

EXPOSE 8000

RUN pip install -r requirements.txt
CMD python3 ./app.py