FROM python

RUN mkdir /app

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
ENV PYTHONUNBUFFERED=1

COPY . .

CMD ["python", "test_app.py"]