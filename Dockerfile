FROM python:3.9

WORKDIR /
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY run.py ./
CMD [ "python3","run.py"]