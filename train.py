import pickle

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import mean_squared_error


# parameters

n_estimators=35, 
max_depth=12, 
min_samples_leaf=3
output_file = 'model_rf.bin'


# DATA PREPARATION

df = pd.read_csv('C:\\Rodolfo\\ML Zoomcamp\\Capstone2\\taxi_fare\\train.csv')

df.drop_duplicates(inplace=True) # Removing duplicate entries

df = df[df['fare']!=0] # Removing where fare = 0, cause it seems wrong

#Removing oddly high travel distance to make a better model
max_num = df[df["distance_traveled"] == df["distance_traveled"].max()].index
df.drop([197339], axis=0, inplace=True)

# As total_fare is directly dependent of fare, I'll remove total fare column
df.drop(['total_fare'], axis=1, inplace=True)



# TRAINING 

df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)
df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=1)

df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

y_train = df_train.fare.values
y_val = df_val.fare.values
y_test = df_test.fare.values

del df_train['fare']
del df_val['fare']
del df_test['fare']

train_dicts = df_train.to_dict(orient='records')
val_dicts = df_val.to_dict(orient='records')

dv = DictVectorizer(sparse=False)
X_train = dv.fit_transform(train_dicts)
X_val = dv.transform(val_dicts)

test_dicts = df_test.to_dict(orient='records')
X_test = dv.transform(test_dicts)

rf = RandomForestRegressor(n_estimators=35, max_depth=12, min_samples_leaf=3, random_state=1, n_jobs=-1, warm_start=True)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_val)
rmse_rf = np.sqrt(mean_squared_error(y_val, y_pred))

print(f'RMSE of train data is {rmse_rf}')


#Computing Final RMSE

y_pred = rf.predict(X_test)

rmse_rf_test = np.sqrt(mean_squared_error(y_test, y_pred))
print(f'RMSE of test data is {rmse_rf_test}')


# Save the model

with open(output_file, 'wb') as f_out:
    pickle.dump((dv, rf), f_out)

print(f'the model is saved to {output_file}')