from sklearn import tree
import json

data = 0
with open('./training_data/data.txt') as json_data:
    data = json.load(json_data)
	
targets = 0
with open('./training_data/targets.txt') as json_data:
    targets = json.load(json_data)

print(data)
clf = tree.DecisionTreeClassifier()
clf = clf.fit(data,targets)

print('Loaded model ...')
while(1):
	print('Enter data')
	mi = double(raw_input('Enter monthly income'))
	me = double(raw_input('Enter monthly expenditure'))
	ti = mi*12
	rcs = double(raw_input('Enter rate of change of savings'))
	age = double(raw_input('Enter age'))
	ta = double(raw_input('Enter monthly bank balance'))
	print('Predicting ...')
	print(clf.predict([[mi, me, ti, rcs, age, ta]]))
	
	

