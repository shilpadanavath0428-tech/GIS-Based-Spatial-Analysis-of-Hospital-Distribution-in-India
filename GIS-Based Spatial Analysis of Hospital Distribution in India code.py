import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("hospital_directory.csv", low_memory=False)

# Basic dataset information
print("Total number of hospitals:", len(df))
print("Total number of variables:", len(df.columns))
print("\nList of variables:\n", df.columns)

# Data cleaning
df = df.dropna(subset=["State"])

if "Total_Num_Beds" in df.columns:
    df["Total_Num_Beds"] = pd.to_numeric(df["Total_Num_Beds"], errors="coerce")

# State-wise hospital count
state_counts = df["State"].value_counts()

print("\nTop 10 States by Number of Hospitals:\n")
print(state_counts.head(10))

plt.figure()
state_counts.head(10).plot(kind="bar")
plt.title("Top 10 States by Number of Hospitals")
plt.xlabel("State")
plt.ylabel("Number of Hospitals")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Emergency service analysis
if "Emergency_Services" in df.columns:
    emergency_counts = df["Emergency_Services"].value_counts()

    print("\nEmergency Services Distribution:\n")
    print(emergency_counts)

    plt.figure()
    emergency_counts.plot(kind="bar")
    plt.title("Emergency Services Availability")
    plt.xlabel("Emergency Status")
    plt.ylabel("Number of Hospitals")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Bed capacity analysis
if "Total_Num_Beds" in df.columns:
    bed_by_state = df.groupby("State")["Total_Num_Beds"].sum().sort_values(ascending=False)

    print("\nTop 5 States by Total Bed Capacity:\n")
    print(bed_by_state.head(5))

    plt.figure()
    bed_by_state.head(5).plot(kind="bar")
    plt.title("Top 5 States by Total Bed Capacity")
    plt.xlabel("State")
    plt.ylabel("Total Number of Beds")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Hospital category distribution
if "Hospital_Category" in df.columns:
    category_counts = df["Hospital_Category"].value_counts()

    print("\nHospital Category Distribution:\n")
    print(category_counts)

    plt.figure()
    category_counts.plot(kind="bar")
    plt.title("Hospital Category Distribution")
    plt.xlabel("Category")
    plt.ylabel("Number of Hospitals")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

print("\nAnalysis completed successfully.")
