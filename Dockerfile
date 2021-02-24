FROM python:3.8-alpine
ENV PYTHONUNBUFFERED=1
WORKDIR /supervisor-driver-service
COPY requirements.txt requirements.txt
RUN apk add --no-cache docker gcc musl-dev linux-headers
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8888
EXPOSE 6969
