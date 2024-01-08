import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 读取CSV文件
df = pd.read_csv(r'C:\Users\11943\Desktop\pythonProject3\data\xianmen.csv')

# 转换日期列为datetime类型
df['DATE'] = pd.to_datetime(df['DATE'])

# 提取月份信息
df['Month'] = df['DATE'].dt.month_name()

# 提取季节信息
seasons = {
    1: 'Winter',
    2: 'Winter',
    3: 'Spring',
    4: 'Spring',
    5: 'Spring',
    6: 'Summer',
    7: 'Summer',
    8: 'Summer',
    9: 'Fall',
    10: 'Fall',
    11: 'Fall',
    12: 'Winter'
}

df['Season'] = df['DATE'].dt.month.map(seasons)

# 设置图形样式
sns.set(style="whitegrid")

# 绘制降水量(PRCP)的柱状图
plt.figure(figsize=(12, 6))
sns.barplot(x='Month', y='PRCP', hue='Season', data=df, ci=None)
plt.title('Monthly Precipitation by Season')
plt.xlabel('Month')
plt.ylabel('Precipitation (mm)')
plt.legend(title='Season')
plt.show()



# 绘制平均气温(TAVG)的折线图
plt.figure(figsize=(12, 6))
sns.lineplot(x='DATE', y='TAVG', data=df, marker='o', color='r')
plt.title('Daily Average Temperature')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.show()

# 绘制最高温度(TMAX)和最低温度(TMIN)的折线图
plt.figure(figsize=(12, 6))
sns.lineplot(x='DATE', y='TMAX', data=df, marker='o', color='g', label='TMAX')
sns.lineplot(x='DATE', y='TMIN', data=df, marker='o', color='orange', label='TMIN')
plt.title('Daily Maximum and Minimum Temperatures')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.show()

# 绘制季节性平均温度的柱状图
plt.figure(figsize=(12, 6))
sns.barplot(x='Season', y='TAVG', data=df, ci=None)
plt.title('Seasonal Average Temperature')
plt.xlabel('Season')
plt.ylabel('Temperature (°C)')
plt.show()

# 绘制月均值温度趋势的折线图
plt.figure(figsize=(12, 6))
sns.lineplot(x='Month', y='TAVG', data=df, marker='o', color='b')
plt.title('Monthly Average Temperature Trend')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.show()

# 绘制温度和降水关系的散点图
plt.figure(figsize=(10, 6))
sns.scatterplot(x='TAVG', y='PRCP', data=df, hue='Season')
plt.title('Temperature vs Precipitation')
plt.xlabel('Temperature (°C)')
plt.ylabel('Precipitation (mm)')
plt.legend(title='Season')
plt.show()


# 数据分析：基本统计信息
summary_stats = df[['PRCP', 'TAVG', 'TMAX', 'TMIN']].describe()

# 设置图形样式
sns.set(style="whitegrid")

# 绘制柱状图
plt.figure(figsize=(12, 6))
sns.barplot(x=summary_stats.columns, y='mean', data=summary_stats.T.reset_index(), palette='viridis')
plt.title('Mean Values of Meteorological Variables')
plt.xlabel('Variable')
plt.ylabel('Mean Value')
plt.show()

# 数据分析：相关性矩阵
correlation_matrix = df[['PRCP','TAVG', 'TMAX', 'TMIN']].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Correlation Matrix')
plt.show()
