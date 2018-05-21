from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot as plt
def parser(x):
    return datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
series = read_csv('pm25_content_nj.csv',
                 header=0,parse_dates=[0],index_col=0,
                  squeeze=True, date_parser=parser)
print(series.head())
series.plot()
plt.show()

