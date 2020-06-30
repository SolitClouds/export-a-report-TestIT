FROM python:3.8

ADD . /app/
WORKDIR /app
RUN pip install -r requirements.txt

CMD ["gunicorn", "-w 4", "-t 3600", "-b 0.0.0.0", "service:app"]