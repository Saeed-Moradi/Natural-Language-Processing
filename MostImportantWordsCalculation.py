from read_contents import Counter
from parsivar import FindStems, Tokenizer, Normalizer
from Preprocess import preprocess_words, stop_words_list
from sklearn.feature_selection import chi2, SelectKBest
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

emails1 = "Spam-Filtering-For-Persian-master/emails/spamtraining"
emails1 = "Spam-Filtering-For-Persian-master/emails/spamtesting"
y_train = []
for i in range(Counter(emails1)):
    spam = ['spam']
    y_train.append(spam)


def chi_square():
    my_normalizer = Normalizer()
    my_tokenizer = Tokenizer()
    vectorizer = CountVectorizer(stop_words=stop_words_list, tokenizer=my_tokenizer.tokenize_words, max_features=5000,
                                 ngram_range=(1, 1), min_df=5, preprocessor=preprocess_words)
    vectorizer.fit(preprocess_words)
    x_train = vectorizer.transform(preprocess_words).toarray()
    x_test = preprocess_words()
    # x_test.vectorizer


chi_square()
