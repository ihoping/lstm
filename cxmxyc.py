from pandas import read_csv
from pandas import datetime
from sklearn.metrics import mean_squared_error
from math import sqrt
from matplotlib import pyplot
# load dataset
def parser(x):
  return datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
series = read_csv('xxx')
# split data into train and test
X = series.values
pre_len = round(len(X) * -0.3)
train, test = X[0:pre_len], X[pre_len:]
# walk-forward validation
history = [x for x in train]
predictions = list()
for i in range(len(test)):
  # make prediction
  predictions.append(history[-1])
  # observation
  history.append(test[i])
# report performance
rmse = sqrt(mean_squared_error(test, predictions))
print('RMSE: %.3f' % rmse)
# line plot of observed vs predicted
pyplot.plot(test)
pyplot.plot(predictions)
pyplot.show()
