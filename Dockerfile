FROM python:3.8-alpine
COPY . .
RUN apk add --no-cache gcc musl-dev linux-headers
RUN pip3 install -r requirements.txt
EXPOSE 6969
CMD ["python3", "falc.py", "-p", "6969", "-6"]
