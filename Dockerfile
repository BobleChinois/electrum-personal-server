FROM python:3.7-alpine

WORKDIR /electrum-personal-server/

COPY . /electrum-personal-server/

#WORKDIR /electrum-personal-server/

RUN ["pip3", "install", "--trusted-host", "pypi.python.org", "-r", "requirements.txt"] 
RUN ["pip3", "install", "."] 

EXPOSE 50002

CMD ["electrum-personal-server", "config.ini"]
