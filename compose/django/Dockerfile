FROM python:3.12-bullseye

# Define your working directory
WORKDIR /app

# Install dependencies and update image packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    # dépendances à installer selon la doc de psycopg2: https://www.psycopg.org/docs/install.html#build-prerequisites
    build-essential \
    libpq-dev

# Copy Pipfile
COPY ./Pipfile ./Pipfile.lock .

# Installer les dépendances python
RUN pip install pipenv && pipenv sync --system --dev 

# Copy the project files
COPY . .

# Remove unwanted characters generated under windows for bash scripts
RUN sed -i 's/\r//g' /app/compose/django/entrypoint 
# Make the script executable
RUN chmod +x /app/compose/django/entrypoint

RUN sed -i 's/\r//g' /app/compose/django/start 
RUN chmod +x /app/compose/django/start

ENTRYPOINT ["/app/compose/django/entrypoint"]