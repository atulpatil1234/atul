#1.because of below issue container is failing to start 
2024/08/05 15:18:20 error while reading the file "/csvserver/inputdata": open /csvserver/inputdata: no such file or directory
#2.application is running on below port
9300
#3.create below dockerfile to run the application on port 9393
# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set environment variable for border color
ENV CSVSERVER_BORDER=Orange

# Set working directory
WORKDIR /app

# Copy application files and input file to the container
COPY . /app

# Install Flask and other dependencies
RUN pip install Flask

# Expose the port the application will run on
EXPOSE 9393

# Run the application
CMD ["python", "app.py"]

docker build -t app .
docker run -td -p 9393:9393 app


