#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn import svm

clf = svm.SVC(C=10000., kernel='rbf')

t0 = time()
clf.fit(features_train, labels_train)
print 'linear train time:'+str(time()-t0)+'s'

t0 = time()
pred = clf.predict(features_test)
print '10:'+str(pred[10])
print '26:'+str(pred[26])
print '50:'+str(pred[50])
print '1 size:'+str(sum(pred))
#print clf.score(features_test, labels_test)
print 'linear test time:'+str(time()-t0)+'s'
print 'linear test score:'+str(clf.score(features_test, labels_test))
#########################################################

### test GridSearchCV

from sklearn.model_selection import GridSearchCV
svm = svm.SVC()
parameters = {'kernel':('linear', 'rbf'), 'C':[1, 10]}
clf = GridSearchCV(svm, parameters)
t0 = time()
clf.fit(features_train, labels_train)
print 'Opt train time:'+str(time()-t0)+'s'
print 'Opt linear test score:'+str(clf.score(features_test, labels_test))
