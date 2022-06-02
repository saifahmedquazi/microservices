FROM alpine
COPY . .
RUN apk add python3 py-pip && pip install -r requirements.txt
CMD python3 app.py

EXPOSE 80