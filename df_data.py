import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random

# load our data frame
df = pd.read_csv("pennData.csv")
pennData = pd.DataFrame(df)
print("-_"*20)
print("Head of the Dataframe") 
print(pennData.head())


print("-_"*20)
print("Tail of the Dataframe") 
print(pennData.tail())


print("-_"*20)
print("Summary of the Dataframe") 
print(pennData.info())


print("-_"*20)
print("Statistiics") 
print(round(pennData.describe()))


print("-_"*20)
print("Count of students in Pathways") 
print(pennData['Pathway'].value_counts())


print("-_"*20)
print("average GPA per Year") 
print(pennData.groupby('Year')['GPA'].mean())


print("-_"*20)
print("Top 3 Students by GPA") 
print(pennData.sort_values(by='GPA', ascending=False).head(3))


print("-_"*20)
print("Students with GPA greater than 3.5") 
print(pennData[pennData['GPA']>3.5])


print("-_"*20)
print("First Student Data") 
print(pennData.iloc[0] )


print(pennData.groupby("Year")["GPA"].mean())

pennData.groupby("Year")["GPA"].mean().plot(kind="bar", color="red")
plt.title("average GPA per year")
plt.xlabel("Year")
plt.ylabel("GPA")
plt.show()

pennData["GPA"].plot(kind="hist", bins=5)
plt.title("GPA Distribution")
plt.xlabel("GPA")
plt.ylabel("Number of Students")
plt.show()

# plt.scatter(pennData("Credits Completed"), pennData["GPA"])
# plt.title("GPA Distribution")
# plt.xlabel("GPA")
# plt.ylabel("Number of Students")
# plt.show()