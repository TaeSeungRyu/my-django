# 운영 도커 파일 샘플(지금 빌드하면 오류난당~)

FROM python:3.12-slim

WORKDIR /app

RUN pip install django gunicorn  

COPY . .

EXPOSE 8000

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]