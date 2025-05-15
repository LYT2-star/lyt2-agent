# Dockerfile in /opt/LYT2/
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# ✅ 现在 COPY 包含 apps/ 和 packages/

ENV PYTHONPATH="/app:/app/packages"

CMD ["uvicorn", "apps.api.main:app", "--host", "0.0.0.0", "--port", "8000"]

