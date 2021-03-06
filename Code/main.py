import os
import csv
import string
import numpy as np
from data import load_data
from data import load_image_for_test_set
from model import Resnet50_model

dataset_path = 'benchmark_dataset.csv'



#************************************************** load data *********************************************#
dataset = []
with open(dataset_path,'r') as f:
	reader = csv.reader(f)
	for row in reader:
		#print('hhhh',row[2])
		label = int(row[2])
		new_row = [row[0],row[1],label]

		dataset.append(new_row)
f.close()
print('dataset length: ',len(dataset) )



five_fold = []
for i in range(5):
	five_fold.append(dataset[int(i*len(dataset)/5):int((i+1)*len(dataset)/5)])


#******************************************************* 5-fold cross-validation **********************************#
outcome = np.zeros((5,2))
for i in range(1):
	print('Round '+str(i+1)+' starts now!')
	test_set = five_fold[i]
	train_all_set = []
	for j in range(5):
		if j==i:
			continue
		train_all_set += five_fold[j][:]
	train_set = train_all_set[0:len(train_all_set)*9/10]
	valid_set = train_all_set[len(train_all_set)*9/10:len(train_all_set)]
	#print(len(train_all_set),len(train_set),len(valid_set))
	train_data, train_label, valid_data, valid_label, test_data, test_label = load_data(train_set, valid_set, test_set)
	outcome[i,:] = Resnet50_model(train_data, train_label, valid_data, valid_label, test_data, test_label)

print('test_acc	test_f1')
for row in outcome:
	print(str(row[0])+'\t'+str(row[1])+'\t'+str(row[2]))
average_out = np.mean(outcome,axis=0)
print('average test accuracy: ',average_out[0],' average test f1: ', average_out[1])#, ' average GTS acc: ', average_out[2])'''

#********************************************************* save the results ******************************************#
with open('outcome.txt','w') as f:
	f.write('test_acc	test_f1	GTS_acc\n')
	for row in outcome:
		f.write(str(row[0])+'\t'+str(row[1])+'\n')
f.close()


