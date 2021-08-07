FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-alpine3.10 as mt-python

LABEL maintainer="Jade <hmy940118@gmail.com>"

COPY requirements.txt /app/requirements.txt

ENV pypi https://pypi.douban.com/simple


RUN pip3 install --no-cache-dir -r /app/requirements.txt -i ${pypi}

COPY ./pyunit_time /app/pyunit_time

COPY ./main.py /app/main.py