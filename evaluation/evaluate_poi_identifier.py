#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score,recall_score

clf = DecisionTreeClassifier()
print 'Train...'
clf.fit(features, labels)
print 'All data train score:'+str(clf.score(features, labels))

### split data
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3, random_state=42)
print 'Test set POI size:'+str(sum(label for label in labels_test))
print 'Test set size:'+str(len(labels_test))
print 'All predict not poi,score is:'+str((1.*len(labels_test)-sum(label for label in labels_test))/len(labels_test))
print 'Retrain...'
clf.fit(features_train, labels_train)
print 'Split 30% test score:'+str(clf.score(features_test, labels_test))
pred = clf.predict(features_test)
print 'Split 30% test precision score:'+str(precision_score(pred, labels_test))
print 'Split 30% test recall score:'+str(recall_score(pred, labels_test))
print 'True positive size:'+str(sum([pred[i]*labels_test[i] for i in range(len(pred))]))

### little test for Mixed matrix
predicts = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
actuals = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0] 
true_in_predicts = sum(predicts)
print 'All true in predicts:'+str(true_in_predicts)
true_in_actuals = sum(actuals)
print 'All true in actuals:'+str(true_in_actuals)
true_positives = sum([predicts[i]*actuals[i] for i in range(len(predicts))]) # 1==1
print 'True positives:'+str(true_positives)
true_negatives = sum([1 if predicts[i]+actuals[i]==0 else 0 for i in range(len(predicts))]) # 0==0
print 'True negatives:'+str(true_negatives)
false_positives = sum([predicts[i]*(0 if actuals[i]==1 else 1) for i in range(len(predicts))]) # 0==1
print 'False positives:'+str(false_positives)
false_negatives = sum([(0 if predicts[i]==1 else 1)*actuals[i] for i in range(len(predicts))]) # 1==0
print 'False negatives:'+str(false_negatives)
print 'Precision:'+str(1.*true_positives/true_in_predicts)
print 'Recall:'+str(1.*true_positives/true_in_actuals)
