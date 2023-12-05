FROM python:3.8.10-alpine3.13

WORKDIR /app

# Copy the django app to the working directory
COPY . /app

# Set the environment variables
ENV CITAS_DB_HOST 10.128.0.5
ENV PACIENTES_HOST 10.128.0.2
ENV HORARIOS_HOST 10.128.0.9
ENV MEDICOS_HOST 10.128.0.6
# Install Python dependencies
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["sh", "init.sh"]