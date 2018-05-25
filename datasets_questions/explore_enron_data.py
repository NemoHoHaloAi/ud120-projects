#!/usr/bin/python
# -*- coding:utf-8 -*-

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print 'data size:'+str(len(enron_data))

print 'data feature size:'+str(len(enron_data[enron_data.keys()[0]]))

print 'POI size:'+str(sum([enron_data[key]['poi'] for key in enron_data.keys() ]))

print 'All POI size:35'

print 'James Prentice info:'+str(enron_data['PRENTICE JAMES']) # total_stock_value特征表示该人所有股票的价值

print 'Wesley Colwell info:'+str(enron_data['COLWELL WESLEY']) # from_this_person_to_poi特征表示由该人向poi发出的邮件数量

for key in enron_data.keys():
    if enron_data[key]['poi']:#key.find('LAY')!=-1:
        print enron_data[key]['total_payments']

print 'Jeffrey Skilling info:'+str(enron_data['SKILLING JEFFREY K']) # from_this_person_to_poi特征表示由该人向poi发出的邮件数量

print 'Skilling total_payments:'+str(enron_data['SKILLING JEFFREY K']['total_payments'])
print 'Ken total_payments:'+str(enron_data['LAY KENNETH L']['total_payments'])
print 'Fastow total_payments:'+str(enron_data['FASTOW ANDREW S']['total_payments'])

print 'All Salary size:'+str(sum([1 if enron_data[key]['salary'] != 'NaN'  else 0 for key in enron_data.keys()]))
print 'All Email Address size:'+str(sum([1 if enron_data[key]['email_address'] != 'NaN'  else 0 for key in enron_data.keys()]))

print 'All total_payments is NaN size:'+str(sum([1 if enron_data[key]['total_payments'] == 'NaN'  else 0 for key in enron_data.keys()]))
print 'All total_payments is NaN proportion:'+str(sum([1 if enron_data[key]['total_payments'] == 'NaN'  else 0 for key in enron_data.keys()])*1./len(enron_data))
print 'All total_payments is NaN size with poi:'+str(sum([1 if enron_data[key]['total_payments'] == 'NaN' and enron_data[key]['poi']  else 0 for key in enron_data.keys()]))
print 'All total_payments is NaN proportion with POI:'+str(sum([1 if enron_data[key]['total_payments'] == 'NaN' and enron_data[key]['poi']  else 0 for key in enron_data.keys()])*1./len(enron_data))
