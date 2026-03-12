FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN pip install uv && \
    uv sync --no-dev --frozen

COPY . .

EXPOSE 8000