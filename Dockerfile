FROM python:3.10

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y python3 python3-pip

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "-m", "app.main"]

