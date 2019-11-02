import pandas as pd
dt = pd.read_csv('austin_weather.csv')
rows,columns=dt.shape
dt['TempHighF'].max()
dt.describe()
dt[dt.TempHighF==dt.TempHighF.max()]