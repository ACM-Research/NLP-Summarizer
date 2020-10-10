# test
import spacy
from collections import Counter
import os

pres = input("File Name: ")
file_path = os.path.join("Dataset/Kaggle Speech Dataset/sotu", "{}.txt".format(pres))

with open(file_path, "r") as file:
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(file.read())

    pos_list = []
    pronouns = []
    for token in doc:
        pos_list.append((token.text, token.pos_))
        #if token.pos_ == "PRON":
            #pronouns.append(token.text)

    pos_tags = [token.pos_ for token in doc]
    word_freq = Counter(pos_tags)
    print(word_freq)
    print(pronouns)
