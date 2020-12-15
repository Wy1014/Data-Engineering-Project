FROM python:3.6.12

WORKDIR /home/


ENV FLASK_APP = app.py

COPY requirements.txt .


RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
