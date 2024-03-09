FROM python:3.11

COPY *.py /app/
COPY requirements.txt /app/
COPY *.csv /app/
COPY *.html /app/

WORKDIR /app/

RUN pip install -r requirements.txt

RUN python model.py

EXPOSE 80

CMD [ "uvicorn", "server:app", "--reload", "--host", "0.0.0.0", "--port","80" ]



