import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# 读取数据集
data = pd.read_csv('github_bot_processed_data.csv')

# 设置pandas显示选项，以便查看更多行和列
pd.set_option('display.max_rows', 100)  # 可根据需要调整显示的最大行数
pd.set_option('display.max_columns', None)  # 显示所有列
# 使用head()方法查看数据的前几行（默认前5行）
print(data.head())

# 使用info()方法查看每列的数据类型等信息
print(data.info())

# 使用describe()方法生成数据的描述性统计信息
print(data.describe())
# 假设数据集中有日期列名为'date_column'，将其格式化为指定格式（比如'%Y-%m-%d'）
data['created_at'] = pd.to_datetime(data['created_at']).dt.strftime('%Y-%m-%d')
# 假设数据集中有日期列名为'date_column'，将其格式化为指定格式（比如'%Y-%m-%d'）
data['updated_at'] = pd.to_datetime(data['updated_at']).dt.strftime('%Y-%m-%d')
import numpy as np
# 对public_repos、public_gists、followers、following等列进行对数变换（为避免出现负数或0取对数的情况，可先进行适当处理，比如加个小正数）
data['log_public_repos'] = np.log(data['public_repos'] + 1)
data['log_public_gists'] = np.log(data['public_gists'] + 1)
data['log_followers'] = np.log(data['followers'] + 1)
data['log_following'] = np.log(data['following'] + 1)
plt.figure(figsize=(10, 6))
data['label'].value_counts().plot(kind='bar')
plt.xlabel('Label')
plt.ylabel('Count')
plt.title('Category Distribution of Label')
plt.show()
# 假设布尔特征列名为['site_admin', 'company']等，这里需要根据实际数据集调整列名
boolean_columns = ['site_admin', 'company']
data[boolean_columns].sum().plot(kind='bar', stacked=True)
plt.xlabel('Features')
plt.ylabel('Count')
plt.title('Distribution of Boolean Features')
plt.show()
plt.figure(figsize=(10, 6))
plt.hist(data['log_public_repos'], bins=30)
plt.xlabel('log_public_repos')
plt.ylabel('Frequency')
plt.title('Distribution of log_public_repos')
plt.show()
plt.figure(figsize=(10, 6))
plt.scatter(data['public_repos'], data['followers'])
plt.xlabel('public_repos')
plt.ylabel('followers')
plt.title('Relationship between public_repos and followers')
plt.show()
from pandas.plotting import scatter_matrix
# 选择要展示的数值型特征列，这里假设是['public_repos', 'public_gists', 'followers', 'following']等，根据实际调整
numeric_columns = ['public_repos', 'public_gists', 'followers', 'following']
scatter_matrix(data[numeric_columns], figsize=(12, 12))
plt.show()
plt.figure(figsize=(10, 6))
sns.boxplot(x='label', y='log_followers', data=data)
plt.xlabel('Label')
plt.ylabel('log_followers')
plt.title('Distribution of log_followers by Label')
plt.show()
# 选择要展示的特征列，同样根据实际情况调整
feature_columns = ['public_repos', 'public_gists', 'followers', 'following']
sns.pairplot(data, vars=feature_columns, hue='label')
plt.show()
corr_matrix = data[['log_public_repos', 'log_public_gists', 'log_followers', 'log_following']].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()
plt.figure(figsize=(10, 6))
sns.violinplot(x='label', y='log_followers', data=data)
plt.xlabel('Label')
plt.ylabel('log_followers')
plt.title('Distribution Difference between Label and log_followers')
plt.show()
