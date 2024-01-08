import pandas as pd

# 读取CSV文件
df = pd.read_csv('xianmen.csv')

# 将温度列从华氏度转换为摄氏度
df['TAVG'] = (df['TAVG'].astype(float) - 32) * 5/9
df['TMAX'] = (df['TMAX'].astype(float) - 32) * 5/9
df['TMIN'] = (df['TMIN'].astype(float) - 32) * 5/9

# 保存修改后的数据到同一文件
df.to_csv('xianmen.csv', index=False)
