# Use the official Node.js image as a base image
FROM python:3

# To include the vulnerabilities patch packages
RUN apt-get update && apt-get upgrade -y && apt-get install -y curl

# Install tzdata for timezone configuration
RUN apk add --no-cache tzdata

# Create a non-root user and group
RUN addgroup -S appgroup && adduser -S appusr -G appgroup

WORKDIR /app

# Change ownership of the working directory to the non-root user
RUN chown -R appusr:appgroup /app

# Switch to the non-root user
USER appusr

# Setup timezone
ENV TZ=Asia/Kolkata

# Add build argument for commit ID
ARG COMMIT_ID

# Set the commit ID as an environment variable
ENV COMMIT_ID=${COMMIT_ID}

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the app source code to the working directory
COPY . .

# Expose port 8080
EXPOSE 8080


CMD ["python", "test-connection.py"]


# FROM python:3

# WORKDIR /usr/src/app

# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt

# COPY . .

# CMD [ "python", "./your-daemon-or-script.py" ]
