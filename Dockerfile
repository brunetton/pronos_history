FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    gcc \
    libxml2-dev \
    libxslt-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy files to container
COPY requirements.txt save_pronos.py /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Init result file
RUN touch /app/results

# Define entry point
CMD ["python", "save_pronos.py"]
