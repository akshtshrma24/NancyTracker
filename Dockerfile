FROM python:3.10.1

WORKDIR /nancy_tracker

EXPOSE 5000

COPY requirements.txt .

RUN pip3 install --upgrade pip

RUN pip install -r ./requirements.txt

COPY /influx/ .

COPY /data/ .

COPY logger.py . 

COPY /scraper/ .

#Pinging Google's Public DNS Server
CMD [ "python3", "scraper.py", "50"]