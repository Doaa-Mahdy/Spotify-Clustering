# Use an official lightweight Python image
FROM python:3.9-slim

WORKDIR /bd_a1

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Set the entry point
CMD ["python", "process_data.py"]
