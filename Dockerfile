FROM python:3.13.2-slim AS backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    pkg-config \
    gcc \
    python3-dev \
    build-essential \
    libyaml-dev \
    netcat-traditional \
    libjpeg-dev \
    zlib1g-dev \
    libfreetype6-dev \
    libtiff5-dev \
    libwebp-dev \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && pip install -r requirements.txt

# Copy Django project files & environment config
COPY MagnificentFox/ ./MagnificentFox/
COPY api/ ./api/
COPY manage.py ./
COPY .env ./

EXPOSE 8000

CMD ["sh", "-c", "python manage.py collectstatic --noinput && python manage.py migrate && gunicorn MagnificentFox.wsgi:application --bind 0.0.0.0:8000"]
