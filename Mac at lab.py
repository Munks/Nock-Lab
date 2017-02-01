import pandas as pd
import numpy as np
import glob

path = r"Users/matthewnock/Desktop/ProbRevCode/csv_data_copy"
files = glob.glob(path + r"*.csv")
frames = []
for filename in files:
    print(filename)
    df = pd.read_csv(filename)
    frames.append(df)
frame = pd.concat(frames)
frame.to_csv(path + r'\output\compiled.csv')