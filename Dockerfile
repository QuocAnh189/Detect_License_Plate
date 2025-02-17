FROM python:3.11.3

WORKDIR /app

RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir opencv-python-headless
RUN pip install wheel setuptools pip --upgrade

COPY src /app/src
COPY . .

RUN chmod -R 755 /app/src/

# EXPOSE 5000
CMD ["python", "src/app.py"]
# CMD ["flask", "run", "--host=0.0.0.0", "--debug"]
# CMD ["flask", "run", "--host=0.0.0.0"]
