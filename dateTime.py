import pandas as pd

# Create a sample DataFrame with datetime data
data = {
    'date': ['2023-01-01', '2023-01-02', '2023-01-03'],
    'value': [1, 2, 3]
}

df = pd.DataFrame(data)

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Extract year, month, and day
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day

print("Original DataFrame:")
print(df)

# Filter data based on date
df_filtered = df[df['date'] == '2023-01-02']

print("\nFiltered Data:")
print(df_filtered)

# Add day of week column
df['day_of_week'] = df['date'].dt.day_name()

print("\nDataFrame with Day Name:")
print(df)

# Set date as index
df.set_index('date', inplace=True)

# Resample monthly and sum only numeric columns
df_resampled = df.resample('M').sum(numeric_only=True)

print("\nResampled Data:")
print(df_resampled)