import nltk
nltk.download("stopwords")

import pandas as pd

from nltk.corpus import stopwords
from pymystem3 import Mystem
from string import punctuation

#Create lemmatizer and stopwords list
mystem = Mystem()
russian_stopwords = stopwords.words("russian")

bad_words = []
filter_out = []
filter_identifier = []
checked = []

f = open('ru_profane_words.txt', encoding=('utf-8'))
f1 = f.read().split('\n')
#print(f1)
for line in f1:
    #rint(line)
    bad_words.append(line.strip('\n'))
f.close()
def preprocess_text(text):
    label = 0
    found_bad_words = []
    tokens = mystem.lemmatize(str(text).lower())
    #print(tokens, type(tokens))
    tokens = [token for token in tokens if token not in russian_stopwords\
        and token != " " \
        and token.strip() not in punctuation]

    text = " ".join(tokens)
    #print(tokens, type(tokens))
    for token in tokens:
        if token in bad_words:
            found_bad_words.append(token)
            label = 1

    return text, found_bad_words, label

file = pd.read_excel('C:/Users/Ejik/Desktop/negative/Разбитые файлы/Users_янв(101695)/разобранный_файл_0_10000.xlsx')  #Простые комментарии(1000)
                      #C:\Users\Ejik\Desktop\negative\Разбитые файлы\Users_янв(101695)
lines_MesID = file['MessageID']
lines_ChatID = file['ChatID']
lines_SenUID = file['SenderUID']
lines_PerLastName = file['PERSON_LAST_NAME']
lines_date_time = file['CreationDateTime']
lines_text = file['Text']

#print(type(lines_date_time))
#print(lines_date_time)

#print(lines)
count = 0
for line in lines_text:   
  count += 1
  print(count)
  #print(line, type(line))
  #print(preprocess_text(line), type(preprocess_text(line)))
  a = preprocess_text(line)
  #print(a[0], a[1], a[2])
  filter_out.append(a[1])
  filter_identifier.append(a[2])

checked = list(zip(lines_MesID, lines_ChatID, lines_SenUID, lines_PerLastName, lines_date_time, lines_text, filter_out, filter_identifier))

df = pd.DataFrame(checked, columns=['MessageID', 'ChatID', 'SenderUID', 'PERSON_LAST_NAME', 'CreationDateTime', 'Text', 'Filter_out', 'Identifier'])
df.to_excel('вывод_фильтра_mini.xlsx')
print('!!!_____ЧЕКАЙ______!!!')






