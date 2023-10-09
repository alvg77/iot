FROM python:3.11-alpine

WORKDIR /app

COPY . /app

# for psutil
RUN apk add build-base linux-headers
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 9090

CMD ["python", "main.py"]
