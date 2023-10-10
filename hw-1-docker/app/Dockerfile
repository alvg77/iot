FROM python:3.11-alpine

# specify working directory
WORKDIR /app

# copy all files from current directory to working directory
COPY . .

# install dev tools needed for installing psutil
RUN apk add build-base linux-headers

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# expose port 9090
EXPOSE 9090

# run main.py
CMD ["python", "main.py"]
