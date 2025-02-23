FROM python:3.11.3

WORKDIR /app

EXPOSE 50051

# Cài đặt các thư viện hệ thống cần thiết
RUN apt-get update && apt-get install -y \
    git \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install --no-cache-dir opencv-python-headless
RUN pip install --no-cache-dir wheel setuptools pip --upgrade

COPY . .

RUN chmod -R 755 /app/src/

CMD ["python", "-u" ,"src/grpc_server.py"]
