FROM python:3.10.14-alpine

COPY file-organiser.py .
COPY requirements.txt .
COPY README.md .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "file-organiser.py"]