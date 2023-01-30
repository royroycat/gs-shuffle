FROM python:3
WORKDIR /root/app
COPY requirements.txt ./
COPY service_account.json /root/.config/gspread/
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]