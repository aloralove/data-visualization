# This file is essential for creating a Docker container image 
# of your app. It specifies the base image to use (Python), 
# sets up your environment, copies your app files into the container, 
# and defines the command to run your app (using Gunicorn).


# Use an official Python runtime as a parent image
FROM python:3.11.3

# Set environment variables to ensure Python runs 
# in unbuffered mode, which is recommended when 
# running Python within Docker containers.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
# all files in Django project
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run the application Gunicorn is a Python WSGI HTTP Server for UNIX. 
# pre-requisite: have gunicorn specified in requirements.txt
CMD gunicorn --bind :$PORT commerce.wsgi:application

