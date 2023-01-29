# Docker file, image, container
FROM python:3.8

# Set the working directory
WORKDIR /TRADE-BOT

# Copy the requirements.txt file to the container 
COPY requirements.txt /TRADE-BOT/

# Install the packages from the requirements.txt file
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files to the container 
COPY . .

# Set teh default command to run when the container starts 
CMD ["python","-u","./app/main.py"]
