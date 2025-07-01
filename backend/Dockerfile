#Python image
FROM python:3.12.6-slim-bullseye

# Set env variables
# 1. Disable pip version check 
ENV PIP_DISABLE_PIP_VERSION_CHECK=1 
# 2. Dont generate .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
# 3. Deactivate buffer outputs
ENV PYTHONUNBUFFERED=1

# Set working folder
WORKDIR /code

# Copy dependecies file to install them later
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the project
COPY . .

