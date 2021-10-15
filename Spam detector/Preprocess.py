from parsivar import FindStems, Tokenizer, Normalizer, normalizer
import re
from read_contents import read_contents, Counter
from sklearn.feature_selection import chi2, SelectKBest

file = open('StopWords', 'r', encoding='UTF-8')
lines = file.readlines()
stop_words_list = []
for line in lines:
    stop_words_list.append(line.rstrip('\n'))
badChars = ['.', '!', '?', ':', ';', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E',
            'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
            'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '&', '<', '>', '=', '-',
            ]
emails1 = "Spam-Filtering-For-Persian-master/emails/spamtraining"
emails2 = "Spam-Filtering-For-Persian-master/emails/hamtraining"

transformer = SelectKBest().fit()
# def preprocess_words(address, index):
#     email = read_contents(address, index)
#     string = ""
#     l = []
#     for i in email:
#         if i != '' and i != '\n':
#             string = string + i
#             l.append(i)
#     for sentence in l:
#         sentence.replace("/", "")
#     string.replace("/", "")
#     pattern = '[' + ''.join(badChars) + ']'
#     string = re.sub(pattern, '', string)
#     my_normalizer = Normalizer()
#     my_tokenizer = Tokenizer()
#     words = my_tokenizer.tokenize_words(my_normalizer.normalize(string))
#     return l
