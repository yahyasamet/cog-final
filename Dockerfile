# Use a base image with Python and Flask pre-installed for Windows
FROM python:3.10.8

# Set the working directory within the container
WORKDIR /app

# Copy the requirements.txt file and install dependencies
COPY requirements.txt requirements.txt


RUN pip install -r requirements.txt
# Use a base image with Python and Flask pre-installed for Windows
FROM python:3.10.8

# Set the working directory within the container
WORKDIR /app

# Copy the requirements.txt file and install dependencies
COPY requirements.txt requirements.txt

RUN apt-get update && apt-get install -y libasound2 libasound2-dev portaudio19-dev

RUN pip install -r requirements.txt

# Copy the rest of your application code
COPY . .

# Expose the port your Flask app will run on
EXPOSE 5000

# Define the command to run your application
CMD ["python", "run.py"]

