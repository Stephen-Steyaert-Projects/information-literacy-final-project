FROM python:3.13-alpine AS build

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Set working directory
WORKDIR /app

# Copy dependency files
COPY pyproject.toml uv.lock* ./

# Install dependencies into a virtual environment
RUN uv sync --frozen --no-dev --group prod

# Copy application code
COPY . .

# Production stage
FROM python:3.13-alpine

WORKDIR /app

# Copy virtual environment and app from build stage
COPY --from=build /app/.venv /app/.venv
COPY --from=build /app /app

# Set environment variables
ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONUNBUFFERED=1

# Expose gunicorn port
EXPOSE 8000

# Run the application with gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "2", "--worker-class", "sync", "main:app"]
