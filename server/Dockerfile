FROM python:3.11-alpine3.20

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /server

COPY ["./app", "/server/app"]
copy ["./requirements.txt", "/server"]

RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["sh", "-c" , "python -m app.main"]