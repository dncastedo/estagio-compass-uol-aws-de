FROM python

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY script.py .
COPY .env .

VOLUME /app/data

CMD ["python", "script.py"]
