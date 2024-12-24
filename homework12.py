import pandas as pd
from collections import defaultdict
from datetime import datetime
import pytz


def get_timezone_based_on_hours(hours):
    """
    简单的启发式函数，根据一天内的活跃小时数（0 - 23）推断可能的时区
    :param hours: 一天内的活跃小时列表
    :return: 推断的时区
    """
    # 这里是一个简单的规则示例，实际可以根据更复杂的业务逻辑调整
    if all(7 <= h <= 17 for h in hours):  # 例如，活跃时间集中在工作时间（7 - 17）
        return 'America/New_York'
    elif all(8 <= h <= 18 for h in hours):
        return 'Europe/London'
    elif all(9 <= h <= 19 for h in hours):
        return 'Asia/Shanghai'
    else:
        return None


def analyze_timezone_distribution_by_activity(data):
    """
    根据用户的活跃时间推断其可能所属的时区，了解用户的时区分布，分析不同地区用户的协作时间模式
    :param data: 包含用户信息的数据框（包含'event_time'列）
    :return: 按时区分布的统计结果和不同时区的协作时间模式（简单示例为每个时区的平均提交时间）
    """
    data['event_time'] = pd.to_datetime(data['event_time'])
    data['hour'] = data['event_time'].dt.hour
    user_hours_dict = defaultdict(list)
    
    for user_id, group in data.groupby('user_id'):
        user_hours = group['hour'].tolist()
        inferred_timezone = get_timezone_based_on_hours(user_hours)
        if inferred_timezone:
            user_hours_dict[inferred_timezone].append(user_id)
    
    # 统计每个推断出的时区的用户数量（作为时区分布）
    timezone_distribution = pd.Series({tz: len(users) for tz, users in user_hours_dict.items()})
    # 简单示例：计算每个推断出的时区的平均提交时间
    result_dict = {}
    for tz, user_list in user_hours_dict.items():
        user_group = data[data['user_id'].isin(user_list)]
        avg_time = user_group['event_time'].mean()
        result_dict[tz] = avg_time
    timezone_collaboration = pd.Series(result_dict)
    
    return timezone_distribution, timezone_collaboration

def analyze_region_distribution(data):
    """
    统计用户所在国家和地区的分布，并识别主要的开发者集中地
    :param data: 包含用户信息的数据框
    :return: 按国家和地区分布的统计结果和主要集中地
    """
    region_distribution = data['country'].value_counts()
    main_concentration = region_distribution.idxmax()
    return region_distribution, main_concentration


def analyze_city_density(data):
    """
    分析主要城市的开发者密度，发现技术热点区域
    :param data: 包含用户信息的数据框
    :return: 按城市分布的统计结果和技术热点区域（前若干个城市）
    """
    city_distribution = data['location'].value_counts()
    # 例如，选取开发者密度最高的前5个城市作为技术热点区域
    hotspots = city_distribution.nlargest(5, keep='all').index.tolist()
    return city_distribution, hotspots


def main():
        # 读取 CSV 文件
        data = pd.read_csv('users_combined_info_500.csv')
        
        # 时区分析
        timezone_dist, timezone_collab = analyze_timezone_distribution_by_activity(data)
        region_distribution, main_region = analyze_region_distribution(data)
        print("国家和地区分布：")
        print(region_distribution)
        print(f"主要开发者集中地: {main_region}")
        
        # 城市级别分布分析
        city_distribution, hotspots = analyze_city_density(data)
        print("\n城市分布：")
        print(city_distribution)
        print(f"技术热点区域: {hotspots}")
        
        
        # 输出结果
        print("时区分布：")
        print(timezone_dist)
        print("不同时区的协作时间模式（平均提交时间）：")
        print(timezone_collab)

if __name__ == "__main__":
    main()
def analyze_submission_frequency(data):
    # 统计每个用户的提交次数
    submission_counts = data.groupby('user_id')['event_type'].count().reset_index(name='submission_count')

    # 按照提交次数降序排序
    sorted_submission_counts = submission_counts.sort_values(by='submission_count', ascending=False)

    # 取提交次数最高的前五名用户
    high_active_users = sorted_submission_counts.head(5)

    # 取提交次数最低的前五名用户
    low_active_users = sorted_submission_counts.tail(5)

    return high_active_users, low_active_users


# 读取数据
data = pd.read_csv('users_combined_info_500.csv')

# 调用函数进行分析
high_active, low_active = analyze_submission_frequency(data)

print("最高活跃度的前五名用户:")
print(high_active)
print("最低活跃度的前五名用户:")
print(low_active)