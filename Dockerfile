FROM python:3.7-alpine
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]

# Docker build command: docker build -t shaikh .
# Docker run command: docker run -d -p 5001:5000 shaikh