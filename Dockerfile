FROM python:3.12.2

WORKDIR /expense-trcker

# Create a database
RUN python create_db.py
RUN python main.py
