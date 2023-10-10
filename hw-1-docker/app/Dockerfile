FROM python:3.11-bullseye

# specify working directory
WORKDIR /app

# copy all files from current directory to working directory
COPY . .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# expose port 9090
EXPOSE 9090

# run main.py
CMD ["python", "main.py"]
