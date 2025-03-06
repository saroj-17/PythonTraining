#Let us create a python script that generate data in .csv and .xlsx format 

import pandas as pd
import numpy as np 

#random value 
np.random.seed(42)


#define location 
location = ["Lalitpur", "Bhaktapur", "Kathmandu"]

#generate synthetic dataset that gives 500 records 

data = {
    "id":range(1,501), 
    "area_sqft":np.random.randint(500, 5000,500), 
    "bedroom":np.random.randint(1,6,500), 
    "bathroom":np.random.randint(1,5,500), 
    "year_built":np.random.randint(1954, 2024, 500), 
    "garage":np.random.randint(1,3,500), 
    "location":np.random.choice(location,500),
    "price":np.random.randint(10000000, 50000000, 500)
}

#CREATE data frame 

df = pd.DataFrame(data)

#introduce some null value randomly 
for col in ["area_sqft","bedroom", "bathroom", "year_built","garage","location"]:
    df.loc[df.sample(frac=0.05).index,col] = np.nan #5% missing value in that column 


#define file name 
csv_filename = "sample1.csv"
excel_filename ="sample2.xlsx"

#export datas
df.to_csv(csv_filename, index=False)
df.to_excel(excel_filename, index = False)


print(f"Data sucessfully saved in '{csv_filename}' and '{excel_filename}' ")