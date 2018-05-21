from pandas import Series
from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot as plt

# date-time parsing function for loading the dataset
def parser(x):
	return datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
# create a differenced series
def difference(dataset, interval=1):
	diff = list()
	for i in range(interval, len(dataset)):
		value = dataset[i] - dataset[i - interval]
		diff.append(value)
	return Series(diff)
# invert differenced value
def inverse_difference(history, yhat, interval=1):
	return yhat + history[-interval]
# load dataset
series = read_csv('pm25_content_nj.csv', header=0, 
parse_dates=[0], index_col=0, squeeze=True, 
date_parser=parser)
print(series.head())
# transform data to be stationary
differenced = difference(series, 1)
print(differenced.head())
#invert transform
inverted = list()
for i in range(len(differenced)):
	value = inverse_difference(series, 
	differenced[i], len(serues) - i)
	invetsed.append(value)
inverted = Series(inverted)
print(inverted.head())
differenced.plot()
