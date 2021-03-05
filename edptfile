FROM python:3.8-alpine
ENV PYTHONUNBUFFERED=1
WORKDIR /supervisor-driver-service
COPY . .
RUN apk add --no-cache docker gcc musl-dev linux-headers
RUN pip install -r requirements.txt
EXPOSE 8888 6969
ENTRYPOINT ["python3", "falc.py", "-p", "8888", "-s", "6969", "-4"]
