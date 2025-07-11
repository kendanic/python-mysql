FROM python:3.11-slim

# Set timezone
ENV TZ=Asia/Kolkata

# Non-root user
RUN adduser --disabled-password --gecos '' appusr

WORKDIR /app
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

USER appusr

EXPOSE 5000

ARG COMMIT_ID
ENV COMMIT_ID=${COMMIT_ID}

CMD ["python", "test-connection.py"]
