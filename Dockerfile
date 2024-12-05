FROM python:3.9-slim

# Copy files to container
COPY requirements.txt save_pronos.py /app/

# Install dependencies
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

# Init result file
RUN touch /app/results

# Define entry point
CMD ["python", "save_pronos.py"]
