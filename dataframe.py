import pandas as pd

# First DataFrame
df1 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['vansh', 'Riya', 'Karan', 'Priya']
})

# Second DataFrame
df2 = pd.DataFrame({
    'ID': [2, 3, 4, 5],
    'City': ['jaipur', 'sikar', 'Pune', 'indore']
})

print("DataFrame df1:")
print(df1)

print("\nDataFrame df2:")
print(df2)

#inner merge
inner_merge = pd.merge(df1, df2, on='ID', how='inner')

print("Inner Merge:")
print(inner_merge)

#left join on ID
left_join = pd.merge(df1, df2, on='ID', how='left')

print("Left Join:")
print(left_join)

#right join using  pd.merge
right_join = pd.merge(df1, df2, on='ID', how='right')

print("Right Join:")
print(right_join)

#index based  join using df.join
# Setting ID as index
df1_index = df1.set_index('ID')
df2_index = df2.set_index('ID')

# Join based on index
index_join = df1_index.join(df2_index)

print("Index-Based Join:")
print(index_join)

#merging with multiple keys
df3 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Department': ['HR', 'IT', 'IT', 'Sales'],
    'Salary': [30000, 40000, 45000, 35000]
})

df4 = pd.DataFrame({
    'ID': [2, 3, 4, 5],
    'Department': ['IT', 'IT', 'Sales', 'HR'],
    'Bonus': [5000, 6000, 7000, 4000]
})

# Merge on multiple keys
multiple_merge = pd.merge(
    df3,
    df4,
    on=['ID', 'Department'],
    how='inner'
)

print("Merge with Multiple Keys:")
print(multiple_merge)