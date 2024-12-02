import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

data=pd.read_csv('bike.csv')
data=data.drop('id',axis=1)
shanghai_data=data[data['city']==1]
shanghai_data=shanghai_data.drop('city',axis=1)
def simplify_hour(hour):
    if 6<=hour<=18:
        return 1
    else:
        return 0
shanghai_data['hour']=shanghai_data['hour'].apply(simplify_hour)
y=shanghai_data['y'].to_numpy().reshape(-1,1)
#提取y列
shanghai_data=shanghai_data.drop('y',axis=1)
x=shanghai_data.to_numpy()

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
scaler_x = MinMaxScaler()
scaler_y = MinMaxScaler()
x_train_normalized=scaler_x.fit_transform(x_train)
#x训练集归一化
x_test_normalized=scaler_x.fit_transform(x_test)
#x数据集归一化
y_train_normalized=scaler_y.fit_transform(y_train)
#y训练集归一化
y_test_normalized=scaler_y.fit_transform(y_test)
#y数据集归一化

linear_model = LinearRegression()
#创建线性回归模型对象
linear_model.fit(x_test_normalized,y_test_normalized)
#使用训练集数据和标签进行训练
y_pred = linear_model.predict(x_test_normalized)
# 计算均方误差（MSE）
mse = mean_squared_error(y_test_normalized, y_pred)

# 计算决定系数（R²）
r2 = r2_score(y_test_normalized, y_pred)

#计算均方根误差
rmse=np.sqrt(mse)

print('均方误差:',mse)
print('决定系数:',r2)
print("均方根误差:",rmse)
