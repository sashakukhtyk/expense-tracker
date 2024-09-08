# Use the official Python image as the base image
FROM python:3.12.2

# Set the working directory inside the container
WORKDIR /app

# Copy the necessary files to the container
ADD create_db.py .
ADD main.py .

# Create the database by running the script
RUN python create_db.py

# Run the main script
CMD ["python", "main.py"]