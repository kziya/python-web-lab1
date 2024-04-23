FROM python:3.11.3-slim-bullseye


WORKDIR /app


COPY requirements.txt .


RUN python -m pip install -r requirements.txt


COPY . /app
EXPOSE 3000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0","--port", "3000"]