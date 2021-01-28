FROM python:3

ADD producer.py /

RUN pip install pystrich
RUN pip install kafka-python
RUN pip install praw
RUN pip install langdetect

CMD [ "python", "./producer.py" ]