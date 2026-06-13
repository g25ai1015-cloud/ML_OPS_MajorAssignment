FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Run train.py during build to ensure savedmodel.pth exists inside the container
RUN python train.py

EXPOSE 5000

CMD ["python", "app.py"]