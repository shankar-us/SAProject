class ProcessData:

import pandas as pd
combined_df = pd.DataFrame()

def __init__(self, datatype):
	self.load_data(datatype)

def load_data(datatype):
	import glob as gb
	import os

	for filename in gb.glob("static/data/" + datatype + "*.csv"):
		if os.path.isfile(filename) and os.path.getsize(filename) > 0:
			df = pd.read_csv(filename)
			df['filename'] = filename
			combined_df = combined_df.append(df, ignore_index=True)

	return combined_df

# def get_incident():
# return result_df

def get_count(column):
	return combined_df[column].count()