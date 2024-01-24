import pandas as pd

data_frame = pd.read_csv('ML Projects\example_dataset.csv')

data_frame.dropna()

data_frame.drop_duplicates()

print(data_frame.count())
data_frame.to_csv("Preprocessed Data2.csv")