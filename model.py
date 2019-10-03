#import numpy as np
import re
import pickle
from nltk.corpus import stopwords
from sklearn.datasets import load_files

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
#from sklearn.metrics import accuracy_score, SCORERS, roc_auc_score, f1_score

reviews = load_files('Functionalties')

x,y = reviews.data , reviews.target

with open('x.pickle','wb') as f:
    pickle.dump(x,f)
    
with open('y.pickle','wb') as f:
    pickle.dump(y,f)
    
corpus = []
for i in range(0, len(x)):
    review = re.sub(r'\W',' ',str(x[i]))
    review = review.lower()
    review = re.sub(r'\s+[a-z]\s+',' ',review)
    review = re.sub(r'^[a-z]\s+','', review)
    review = re.sub(r'\s+', ' ', review)
  
    corpus.append(review)

vectorizer = TfidfVectorizer(max_features=100, min_df=3,max_df=0.8,stop_words=stopwords.words('english'))

X_train, X_test, Y_train, Y_test = train_test_split(corpus, y, test_size=0.3, random_state=42)

X_train = vectorizer.fit_transform(X_train).toarray()
X_test = vectorizer.transform(X_test).toarray()

classifier = LogisticRegression(random_state=42, solver='newton-cg', max_iter=1000, multi_class='multinomial', n_jobs=-1)
classifier.fit(X_train, Y_train)

"""print("Solver = 'newton-cg'")
print("Accuracy : ", accuracy_score(Y_test, classifier.predict(X_test)))
print("F1 Score : ", f1_score(Y_test, classifier.predict(X_test),average='macro'))
print("AUC : ", roc_auc_score(Y_test,  classifier.predict(X_test)))
print()

classifier = LogisticRegression(random_state=42, solver='lbfgs', max_iter=1000, multi_class='multinomial', n_jobs=-1)
classifier.fit(X_train, Y_train)

print("Solver = 'lbfgs'")
print("Accuracy : ", accuracy_score(Y_test, classifier.predict(X_test)))
print("F1 Score : ", f1_score(Y_test,classifier.predict(X_test),average='macro'))
print("AUC : ", roc_auc_score(Y_test,  classifier.predict(X_test),average='macro'))
print()

classifier = LogisticRegression(random_state=42, solver='sag', max_iter=1000, multi_class='multinomial', n_jobs=-1)
classifier.fit(X_train, Y_train)

print("Solver = 'sag'")
print("Accuracy : ", accuracy_score(Y_test, classifier.predict(X_test)))
print("F1 Score : ", f1_score(Y_test, classifier.predict(X_test),average='macro'))
print("AUC : ", roc_auc_score(Y_test,  classifier.predict(X_test),average='macro'))
print()

classifier = LogisticRegression(random_state=42, solver='saga', max_iter=1000, multi_class='multinomial', n_jobs=-1)
classifier.fit(X_train, Y_train)

print("Solver = 'saga'")
print("Accuracy : ", accuracy_score(Y_test, classifier.predict(X_test)))
print("F1 Score : ", f1_score(Y_test, classifier.predict(X_test),average='macro'))
print("AUC : ", roc_auc_score(Y_test,  classifier.predict(X_test),average='macro'))
print()"""
