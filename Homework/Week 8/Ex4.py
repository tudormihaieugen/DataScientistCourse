import pandas as pd

students = {
    "Michael": {"Math": 7, "Biology": 9, "Physics": 7, "Chemistry": 10, "History": 5},
    "Chuck": {"Math": 5, "Biology": 6, "Physics": 10, "Chemistry": 8, "History": 9},
    "Edward": {"Math": 10, "Biology": 9, "Physics": 8, "Chemistry": 7, "History": 6},
    "Sandra": {"Math": 8, "Biology": 8, "Physics": 9, "Chemistry": 8, "History": 7},
    "Alexander": {"Math": 6, "Biology": 10, "Physics": 6, "Chemistry": 6, "History": 10}
}

data = pd.DataFrame(students)
print(data)
data.to_csv("Ex4.csv")

df = pd.read_csv("Ex4.csv")
df["Mean"] = df.mean(axis=1)
print(df)
