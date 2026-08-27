import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates

# قراءة البيانات
df = pd.read_csv("voice.csv")

# نسخ البيانات
df_norm = df.copy()

# تطبيق normalization (مع تجنب عمود label)
for col in df.columns[:-1]:
    df_norm[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())

# الرسم
parallel_coordinates(df_norm, 'label')
plt.title("After Normalization")
plt.show()