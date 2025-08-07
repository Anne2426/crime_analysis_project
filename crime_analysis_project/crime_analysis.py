import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("crime_rate_data.csv")
print("📊 Crime Data Preview:")
print(df.head())

# Total crimes per city over all years
df["Total_Crime"] = df[["Theft", "Murder", "Assault", "Burglary"]].sum(axis=1)
total_by_city = df.groupby("City")["Total_Crime"].sum().sort_values(ascending=False)

# Plot: Total crimes per city
plt.figure(figsize=(10, 6))
sns.barplot(x=total_by_city.values, y=total_by_city.index, palette="Reds")
plt.title("Total Reported Crimes by City (2018–2020)")
plt.xlabel("Total Crimes")
plt.tight_layout()
plt.savefig("total_crimes_by_city.png")
plt.show()

# Plot: Crime trends over years for each crime type in Delhi
delhi_data = df[df["City"] == "Delhi"]

plt.figure(figsize=(10, 6))
plt.plot(delhi_data["Year"], delhi_data["Theft"], label="Theft", marker="o")
plt.plot(delhi_data["Year"], delhi_data["Murder"], label="Murder", marker="o")
plt.plot(delhi_data["Year"], delhi_data["Assault"], label="Assault", marker="o")
plt.plot(delhi_data["Year"], delhi_data["Burglary"], label="Burglary", marker="o")
plt.title("Delhi Crime Trends (2018–2020)")
plt.xlabel("Year")
plt.ylabel("Number of Cases")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("delhi_crime_trends.png")
plt.show()
