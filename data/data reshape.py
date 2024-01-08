import pandas as pd

# 读取CSV文件
df = pd.read_csv('xianmen.csv')

# 删除 "STATION" 和 "NAME" 列
df = df.drop(columns=["STATION"])

# 保存修改后的数据到同一文件
df.to_csv('xianmen.csv', index=False)
