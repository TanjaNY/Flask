# Use an official Python runtime as a parent image
FROM python:3.9-slim AS base

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=app.py

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

# Expose the port that Flask runs on
EXPOSE 5000

# Run Flask on port 5000 (default Flask port)
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]
