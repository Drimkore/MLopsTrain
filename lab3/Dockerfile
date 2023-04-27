FROM python:3

WORKDIR /usr/src/app

EXPOSE 5000
COPY req.txt ./req.txt 
RUN pip install -r req.txt
COPY . .
RUN run.sh
