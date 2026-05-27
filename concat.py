#creating dataframes
import pandas as pd

# First DataFrame
df1 = pd.DataFrame({
    'ID': [1, 2],
    'Name': ['Aman', 'Riya']
})

# Second DataFrame
df2 = pd.DataFrame({
    'ID': [3, 4],
    'Name': ['Karan', 'Priya']
})

# Third DataFrame
df3 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'City': ['Delhi', 'Mumbai', 'Pune', 'Chennai']
})

print("DataFrame 1:")
print(df1)

print("\nDataFrame 2:")
print(df2)

print("\nDataFrame 3:")
print(df3)

#Vertically Concatenate df1 and df2 using pd.concat()
concat_df = pd.concat([df1, df2], ignore_index=True)

print("Concatenated DataFrame:")
print(concat_df)

#Merge the Result with Third DataFrame
merged_df = pd.merge(concat_df, df3, on='ID', how='inner')

print("Merged DataFrame:")
print(merged_df)




'''merge() and join() are both functions in Pandas used to combine two DataFrames, but they differ in their working and usage. The merge() function is mainly used for column-based joining and works similarly to SQL joins. It combines DataFrames using one or more common columns and supports different types of joins such as inner, left, right, and outer joins. It is more flexible and is commonly used when working with relational or database-like data.

On the other hand, the join() function is mainly used for index-based joining. By default, it joins DataFrames using their indexes rather than common columns. The syntax of join() is simpler and it is generally faster for index-related operations. It is useful when the DataFrames already have meaningful indexes and you want a quick combination of data.'''