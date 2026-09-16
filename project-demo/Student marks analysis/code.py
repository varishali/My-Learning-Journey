import pandas as pd

# Sample data (no external file needed)
data = {
    "Name": ["Aman", "Riya", "Karan", "Sneha", "Vikas"],
    "Math": [85, 92, 78, 65, 90],
    "Science": [80, 88, 75, 70, 95],
    "English": [90, 85, 82, 60, 88]
}

df = pd.DataFrame(data)

# Total and Average marks
df["Total"] = df["Math"] + df["Science"] + df["English"]
df["Average"] = df["Total"] / 3

# Pass/Fail (passing marks = 40 in each subject)
df["Result"] = df[["Math", "Science", "English"]].min(axis=1).apply(
    lambda x: "Pass" if x >= 40 else "Fail"
)

# Sort by Total marks (highest first)
df = df.sort_values(by="Total", ascending=False)

print(df)

# Class average
print("\nClass Average:", round(df["Average"].mean(), 2))

# Topper
topper = df.iloc[0]
print(f"Topper: {topper['Name']} with {topper['Total']} marks")