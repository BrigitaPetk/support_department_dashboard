FROM python:3.9.10
WORKDIR /app
COPY main.py .
COPY requirements.txt .
COPY data_processing data_processing
RUN pip install -r requirements.txt
ENTRYPOINT ["python3", "./main.py"]
