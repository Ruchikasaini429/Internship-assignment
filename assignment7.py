
import pandas as pd
# create pandasseries from dictionary

student_marks = {
    "Riya": 85,
    "Aman": 90,
    "Neha": 78,
    "Rahul": 88
}

series_dict = pd.Series(student_marks)

print("Series from Dictionary:")
print(series_dict)

# 2. Create Pandas Series from List

numbers = [10, 20, 30, 40, 50]

series_list = pd.Series(numbers)

print("\nSeries from List:")
print(series_list)

# 3. Access Elements of a Series

print("\nAccess Elements:")

print("First Element:", series_list[0])

print("Marks of Aman:", series_dict["Aman"])

print("\nFirst 3 Elements:")
print(series_list[0:3])