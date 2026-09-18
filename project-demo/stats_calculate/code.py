import numpy as np

# Sample data (marks of 10 students)
marks = [56, 78, 90, 45, 67, 89, 34, 72, 88, 60]

data = np.array(marks)

mean_val = np.mean(data)
median_val = np.median(data)
std_val = np.std(data)
var_val = np.var(data)
min_val = np.min(data)
max_val = np.max(data)

print("Data:", marks)
print("Mean:", mean_val)
print("Median:", median_val)
print("Standard Deviation:", round(std_val, 2))
print("Variance:", round(var_val, 2))
print("Min:", min_val)
print("Max:", max_val)

# Students above average
above_avg = data[data > mean_val]
print("\nStudents scoring above average:", above_avg)

# Sorted data
print("Sorted Data:", np.sort(data))