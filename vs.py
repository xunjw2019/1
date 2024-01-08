import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# 读取数据集
df1 = pd.read_csv(r'C:\Users\11943\Desktop\pythonProject3\data\qingdao.csv')
df2 = pd.read_csv(r'C:\Users\11943\Desktop\pythonProject3\data\nanchang.csv')
df3 = pd.read_csv(r'C:\Users\11943\Desktop\pythonProject3\data\xianmen.csv')

# 将日期列解析为日期对象
df1['DATE'] = pd.to_datetime(df1['DATE'])
df2['DATE'] = pd.to_datetime(df2['DATE'])
df3['DATE'] = pd.to_datetime(df3['DATE'])

# 对比气温
plt.figure(figsize=(10, 6))
plt.plot(df1['DATE'], df1['TAVG'], label='qingdao')
plt.plot(df2['DATE'], df2['TAVG'], label='nanchang')
plt.plot(df3['DATE'], df3['TAVG'], label='xianmen')

plt.title('Temperature Comparison')
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.legend()

# 调整日期刻度为每月一次
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.gcf().autofmt_xdate()

plt.show()

# 对比降水
plt.figure(figsize=(10, 6))
plt.plot(df1['DATE'], df1['PRCP'], label='qingdao')
plt.plot(df2['DATE'], df2['PRCP'], label='nanchang')
plt.plot(df3['DATE'], df3['PRCP'], label='xianmen')

plt.title('Precipitation Comparison')
plt.xlabel('Date')
plt.ylabel('Precipitation')
plt.legend()

# 调整日期刻度为每月一次
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.gcf().autofmt_xdate()

plt.show()
