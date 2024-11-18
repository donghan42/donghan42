import pandas as pd
import numpy as np
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
raw_data = pd.read_csv('github_bot_raw_data.csv') 
#列字段解读
columns = [
    'actor_id',  # GitHub用户的ID (示例值: 1081405)
    'label',  # 用户标签（"Human"或"Bot"） (示例值: Human)
    'login',  # GitHub用户的登录名 (示例值: dlazesz)
    'id',  # 用户的GitHub ID (示例值: 1081405)
    'node_id',  # 用户的GitHub节点ID (示例值: MDQ6VXNlcjEwODE0MDU=)
    'avatar_url',  # GitHub头像URL (示例值: https://avatars.githubusercontent.com/u/1081405?v=4)
    'gravatar_id',  # Gravatar ID (示例值: None)
    'url',  # GitHub用户的URL (示例值: https://api.github.com/users/dlazesz)
    'html_url',  # GitHub用户的HTML URL (示例值: https://github.com/dlazesz)
    'followers_url',  # GitHub用户的粉丝URL (示例值: https://api.github.com/users/dlazesz/followers)
    'following_url',  # GitHub用户的关注URL (示例值: https://api.github.com/users/dlazesz/following{/other_user})
    'gists_url',  # 用户的GitHub Gists URL (示例值: https://api.github.com/users/dlazesz/gists{/gist_id})
    'starred_url',  # 用户的GitHub Starred URL (示例值: https://api.github.com/users/dlazesz/starred{/owner}{/repo})
    'subscriptions_url',  # 用户的GitHub订阅URL (示例值: https://api.github.com/users/dlazesz/subscriptions)
    'organizations_url',  # 用户的GitHub组织URL (示例值: https://api.github.com/users/dlazesz/orgs)
    'repos_url',  # 用户的GitHub仓库URL (示例值: https://api.github.com/users/dlazesz/repos)
    'events_url',  # 用户的GitHub事件URL (示例值: https://api.github.com/users/dlazesz/events{/privacy})
    'received_events_url',  # 用户的GitHub接收事件URL (示例值: https://api.github.com/users/dlazesz/received_events)
    'type',  # 用户类型，通常为"User" (示例值: User)
    'site_admin',  # 表示用户是否是GitHub网站管理员的标志 (示例值: False)
    'name',  # 用户的姓名 (示例值: Indig Balázs)
    'company',  # 用户所在公司 (示例值: None)
    'blog',  # 用户的博客 (示例值: None)
    'location',  # 用户的位置 (示例值: None)
    'email',  # 用户的电子邮件 (示例值: None)
    'hireable',  # 表示用户是否愿意被雇佣的标志 (示例值: None)
    'bio',  # 用户在其GitHub资料中提供的自我介绍或个人简介 (示例值: None)
    'twitter_username',  # 用户的Twitter用户名 (示例值: None)
    'public_repos',  # 用户在GitHub上的公共代码仓库数量 (示例值: 26)
    'public_gists',  # 用户的公共Gists数量 (示例值: 1)
    'followers',  # 关注该用户的其他GitHub用户数量 (示例值: 5)
    'following',  # 该用户关注的其他GitHub用户数量 (示例值: 1)
    'created_at',  # 用户的GitHub帐户创建日期 (示例值: 2011-09-26T17:27:03Z)
    'updated_at',  # 用户的GitHub帐户最后更新日期 (示例值: 2023-10-13T11:21:10Z)
]
data = raw_data[columns]
print('去重前数据量:',data.shape[0])
data.drop_duplicates(inplace=True) # 删除重复值
print('去重后数据量:',data.shape[0])

data=data.drop('gravatar_id',axis=1)#axis=1表示按列操作，=0表示按行操作
print('缺失值数量:',data.isnull().sum())#isnull用于判断是否有缺失值，再求和

bool_columns=['name','company','blog','location','email','hireable','bio','twitter_username']
for col in bool_columns:
    data[col]=data[col].astype('bool')
print('缺失值数量:',data.isnull().sum())

# 先将日期时间列转换为pandas的datetime类型（确保数据格式正确解析）
data['created_at'] = pd.to_datetime(data['created_at'])
data['updated_at'] = pd.to_datetime(data['updated_at'])

# 再将datetime类型转换为时间戳（以秒为单位，从1970年1月1日0时0分0秒开始计算）
data['created_at'] = data['created_at'].astype('int64') // 1000000000
data['updated_at'] = data['updated_at'].astype('int64') // 1000000000
print(data[['created_at', 'updated_at']])
import pandas as pd
import matplotlib.pyplot as plt

# 统计bot和human类型（现通过label列）对应的数量（这里简单以计数为例，可根据实际情况调整统计指标）
label_counts = data['label'].value_counts()

# 绘制柱状图
plt.bar(label_counts.index, label_counts.values)

# 添加标题、坐标轴标签
plt.title('Distribution of Bot and Human Accounts')
plt.xlabel('Account Label')
plt.ylabel('Number of Accounts')

# 展示图表
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

# 筛选出bot类型的账号数据（根据label列筛选）
bot_data = data[data['label'] == 'bot']

# 获取创建时间数据
created_at_values = bot_data['created_at']

# 绘制折线图
plt.plot(created_at_values)

# 添加标题、坐标轴标签
plt.title('Creation Time Trend of Bot Accounts')
plt.xlabel('Index')
plt.ylabel('Creation Time')

# 设置x轴刻度为合适的格式（这里简单设置为让其自动适应）
plt.xticks(rotation=45)

# 展示图表
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# 筛选出human类型的账号数据（依据label列判断）
human_data = data[data['label'] == 'human']

# 获取创建时间数据
created_at_values = human_data['created_at']

# 绘制折线图
plt.plot(created_at_values)

# 添加标题、坐标轴标签
plt.title('Creation Time Trend of Human Accounts')
plt.xlabel('Index')
plt.ylabel('Creation Time')

# 设置x轴刻度为合适的格式（这里简单设置为让其自动适应）
plt.xticks(rotation=45)

# 展示图表
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

# 筛选出bot类型的账号数据（按照label列来筛选）
bot_data = data[data['label'] == 'bot']

# 获取粉丝数量和关注数量数据
followers = bot_data['followers']
following = bot_data['following']

# 绘制散点图
plt.scatter(following, followers)

# 添加标题、坐标轴标签
plt.title('Followers vs Following of Bot Accounts')
plt.xlabel('Following')
plt.ylabel('Followers')

# 展示图表
plt.show()