FROM python:3.12.2

WORKDIR /expense-trcker

# Install dependencis
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Create a database
RUN python create_db.py
