FROM python:3.8-alpine
LABEL maintainer "Akashdeep Dhar <t0xic0der@fedoraproject.org>"
ENV PYTHONUNBUFFERED=1
RUN apk add --no-cache docker gcc musl-dev linux-headers redis
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY src/svdriver svdriver
WORKDIR /svdriver
EXPOSE 8888 6969
ENTRYPOINT ["python3", "falc.py", "-d", "10", "-q", "2160", "-p", "8888", "-s", "6969", "-4"]
