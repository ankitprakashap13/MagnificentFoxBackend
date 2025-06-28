# Stage 1: Build Django Backend
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
    libwebp-dev && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && pip install -r requirements.txt

# Copy Django project files & environment config
COPY MagnificentFox/ ./MagnificentFox/
COPY api/ ./api/
COPY manage.py ./
COPY .env ./

# Entrypoint script
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

EXPOSE 8000

CMD ["./entrypoint.sh"]
