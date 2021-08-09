FROM python:3.6

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

RUN python3 test.py

CMD python3 app.py