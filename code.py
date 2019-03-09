#import packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression 
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

#arrays containing names of the roads and their respective ranks in proper order.
road_names = np.array(['bsnl_rd', 'ccd_rd', 'dmart_rd', 'hs_rd', 
                       'isbr_rd', 'ayyappa_temple_rd', 'otera_rd', 
                       'parantha_rd', 'velhankani_main_rd', 'velhankani_market_rd', 'seimens_rd', 'wipro_avenue', 'wipro_village'])

road_ranks = np.array([9, 8, 8.5, 7, 8.5, 5, 10, 7, 7, 3, 6.5, 8, 6.5])

#read data
data = pd.read_csv('data/' + road_names[0] + '/accelerometer.csv')

#count peaks
count_arr = []
for i in range(len(road_names)):
    data = pd.read_csv('data/' + road_names[i] + '/accelerometer.csv')
    data['magmean'] = np.sqrt(np.square(data.x) + np.square(data.y) + np.square(data.z)) - np.mean(np.sqrt(np.square(data.x) + np.square(data.y) + np.square(data.z)))
    data = data[['x', 'y', 'z', 'magmean']]
    plt.figure(figsize = (10, 5))
    rolling = data.magmean.rolling(window = 10)
    rolling_mean = rolling.mean()
    plt.plot( data.magmean)
    plt.plot(rolling_mean, color = 'red')
    count = 0
    for i in range(len(rolling_mean.iloc[9:])):
        if (rolling_mean.iloc[i] >= rolling_mean.max()/2 or rolling_mean.iloc[i] <= rolling_mean.min()/2):
            count += 1
    count = count
    count_arr.append(count)
plt.title('distribution of disturbances in roads')
plt.xlabel('different roads')
plt.ylabel('no of peaks')
plt.plot(count_arr)
plt.show()
plt.figure(figsize = (10, 5))
plt.title('road ranks for different roads')
plt.xlabel('different roads')
plt.ylabel('ranks for roads')
plt.plot(10 - road_ranks)
plt.show()
print(count_arr)
print(road_ranks)
ml_data = pd.DataFrame()
ml_data['road_names'] = road_names
ml_data['no_peaks'] = count_arr
ml_data['road_ranks'] = road_ranks

#fit linear regression
features = ['no_peaks']
labels = ['road_ranks']
lr_clf = LinearRegression()
train_dat, test_dat = train_test_split(ml_data, test_size = 0.2)
lr_clf.fit(train_dat[features], train_dat[labels])
predictions = lr_clf.predict(test_dat[features])
print(mean_absolute_error(test_dat[labels], predictions))