FROM python:3

ADD sentimentAnalysis.py /

RUN pip install textblob
RUN pip install pymongo
RUN pip install nltk
RUN pip install kafka-python
RUN pip install praw
RUN pip install langdetect

CMD [ "python", "./sentimentAnalysis.py" ]