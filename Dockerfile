FROM topiaruss/cassclientbase:latest

COPY . /app
WORKDIR /app

RUN find . -name \*.pyc -delete

RUN devpi use --set-cfg http://dp.topia.com:3141/russ/dev
RUN devpi login russ --password='dpdp'

RUN pip install --trusted-host dp.topia.com -r requirements.txt

