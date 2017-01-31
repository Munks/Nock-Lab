import pandas as pd
import numpy as np
import glob

# df_1 = pd.read_csv(r"C:\Users\Christopher\Desktop\Data\EscapeTask_003_2016_Nov_17_1540trials.csv")
# df_2 = pd.read_csv(r"C:\Users\Christopher\Desktop\Data\EscapeTask_004_2016_Dec_05_1208trials.csv")
path = r"C:\Users\Christopher\Desktop\Data"
# files = glob.glob(path + r"\working_*.csv")
files = glob.glob(path + r"\working\*.csv")
frames = []
for filename in files:
    print(filename)
    df = pd.read_csv(filename)
    frames.append(df)
frame = pd.concat(frames)
frame.to_csv(path + r'\output\compiled.csv')

# to get a single column:
# column = df['Unnamed: 41']
# to get a single row in a column
# value = column[20]
# to get a single row
# row = df.iloc[50]
