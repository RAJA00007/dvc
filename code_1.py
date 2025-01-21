import pandas as pd
import os

#create dataframe
data = {'Name' : ['Alice','Bob','charlie',],
        'Age': [25,30,35],
        'city': ['new york', 'los angeles','chicago']}

df = pd.DataFrame(data)


#adding new row for versioon2

new_row_loc = {'Name':'gf1', 'Age':20, 'city':'newyork'}
df.loc[len(df.index)] = new_row_loc


# ensures that data exists at root level
#majes dirn for the csv file
data_dir = 'data'

os.makedirs(data_dir,exist_ok=True)


#define the file path
file_path = os.path.join(data_dir,'simple_data.csv')
#save the data frame as csv file
df.to_csv(file_path,index = False)

print(f"csv files saved to {file_path}")