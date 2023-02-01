FROM python:3
WORKDIR /root/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uwsgi", "wsgi.ini"]