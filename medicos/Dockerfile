FROM python:3.8.10-alpine3.13

WORKDIR /app

# Copy the django app to the working directory
COPY . /app

# Set the environment variables
ENV MEDICOS_DB_HOST 10.128.0.8

# Install Python dependencies

#RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    musl-dev

# Install MongoDB dependencies
RUN apt-get install -y \
    libssl-dev \
    libffi-dev

# Install the MongoDB driver for Django
RUN pip install --no-cache-dir djongo



RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["sh", "init.sh"]