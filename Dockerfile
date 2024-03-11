# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Poetry
RUN pip install poetry

# Configure Poetry: 
# - Do not create a virtual environment inside the Docker container
# - Do not ask any interactive question
RUN poetry config virtualenvs.create false \
  && poetry config installer.parallel false

# Install dependencies using Poetry
RUN poetry install --no-dev --no-interaction --no-ansi

# Download data by running the script with Poetry
RUN poetry run python download_data.py

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV PYTHONUNBUFFERED=1

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
