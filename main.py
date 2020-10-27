import pandas as pd

melburne_file_path = 'D:\Pobrane\melb_data\melb_data.csv'

melburne_data = pd.read_csv(melburne_file_path)

rooms = melburne_data.Rooms.mean()

print(melburne_data.columns)

print(melburne_data.Price.mean())
