# DataFrames
# Make a Pandas DataFrame with a two-dimensional Python list 
# Create DataFrame from Python dict 
# Create Pandas dataframe using list of lists 
# Create a Pandas dataframe using list of tuples 
# Create a Pandas DataFrame from List of Dicts
# Import pandas
import pandas as pd

data_2d = [
    [101, "Riya", 85],
    [102, "Aman", 90],
    [103, "Neha", 78]
]

df1 = pd.DataFrame(data_2d)

print("DataFrame from 2D List:")
print(df1)

data_dict = {
    "Name": ["Riya", "Aman", "Neha"],
    "Age": [20, 21, 19],
    "Marks": [85, 90, 78]
}

df2 = pd.DataFrame(data_dict)

print("\nDataFrame from Dictionary:")
print(df2)

list_of_lists = [
    ["Riya", 20, "Delhi"],
    ["Aman", 21, "Mumbai"],
    ["Neha", 19, "Jaipur"]
]

df3 = pd.DataFrame(list_of_lists,
                   columns=["Name", "Age", "City"])

print("\nDataFrame from List of Lists:")
print(df3)

list_of_tuples = [
    ("Riya", 85),
    ("Aman", 90),
    ("Neha", 78)
]

df4 = pd.DataFrame(list_of_tuples,
                   columns=["Name", "Marks"])

print("\nDataFrame from List of Tuples:")
print(df4)

list_of_dicts = [
    {"Name": "Riya", "Age": 20},
    {"Name": "Aman", "Age": 21},
    {"Name": "Neha", "Age": 19}
]

df5 = pd.DataFrame(list_of_dicts)

print("\nDataFrame from List of Dictionaries:")
print(df5)