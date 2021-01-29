FROM python:3

ADD sentimentAnalysis.py /

RUN pip install textblob
RUN pip install pymongo
RUN pip install nltk
RUN pip install psycopg2
RUN python -m nltk.downloader punkt
RUN python -m nltk.downloader averaged_perceptron_tagger
RUN python -m nltk.downloader brown

CMD [ "python3", "./sentimentAnalysis.py" ]
