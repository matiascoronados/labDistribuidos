FROM python:3

ADD consumer.py /

RUN pip install kafka-python
RUN pip install pymongo
RUN pip install langdetect
RUN pip install nltk
RUN pip install praw

CMD [ "python", "./consumer.py" ]