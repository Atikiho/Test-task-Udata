ARG PYTHON_VERSION=alpine
FROM python:${PYTHON_VERSION} as base

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN adduser \
    --disabled-password \
    --home /app \
    appuser

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

USER appuser

COPY . .

EXPOSE 8000

CMD ["gunicorn", "API.main:app", "--workers", "10", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000", "--log-level", "info", "--access-logfile", "-", "--error-logfile", "-"]
