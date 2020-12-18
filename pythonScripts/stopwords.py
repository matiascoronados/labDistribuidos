from nltk.corpus import stopwords
nltk_stopwords = set(stopwords.words('english'))
text = "The first time I saw Catherine she was wearing a vivid crimson dress and was nervously " \
       f"leafing through a magazine in my waiting room."
text_without_stopword = [word for word in text.split() if word.lower() not in nltk_stopwords]
print(f"Original Text : {text}")
print(f"Text without stopwords : {' '.join(text_without_stopword)}")
print(f"Total count of stopwords in NLTK is {len(nltk_stopwords)}")