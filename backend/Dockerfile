FROM python:latest

#RUN mkdir /root/.aws
#COPY .aws/config      /root/.aws/config
#COPY .aws/credentials /root/.aws/credentials

WORKDIR /app 

COPY requirements.txt requirements.txt
#COPY app.py app.py

RUN pip3 install -r requirements.txt

CMD ["python3", "-m" , "uvicorn", "app:app", "--reload", "--host=0.0.0.0", "--port=80"]
# python3 -m uvicorn app:app --reload --host=0.0.0.0 --port=8080

EXPOSE 80
