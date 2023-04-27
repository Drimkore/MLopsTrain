
WORKDIR /app

EXPOSE 5000
COPY req.txt ./req.txt 
RUN pip install -r req.txt
COPY . .


CMD python model_testing.py
