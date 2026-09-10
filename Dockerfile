FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY niv0.py .
COPY regression.joblib .

CMD ["uvicorn", "niv0:app", "--host", "0.0.0.0", "--port", "8000"]
