import pandas as pd
data = pd.read_csv(r"Life Expectancy Data.csv", encoding = "utf-8")
data.describe()

developing = data[data["Status"]=="Developing"]
developed = data[data["Status"]=="Developed"]

developing_countries = developing.groupby("Country")
developed_countries = developed.groupby("Country")

mean_developing = developing_countries.mean()
mean_developed = developed_countries.mean()

mean_developing2 = mean_developing["Life expectancy "].mean()
mean_developed2 = mean_developed["Life expectancy "].mean()

std_developing = mean_developing["Life expectancy "].std()
std_developed = mean_developed["Life expectancy "].std()

print("Mean of Developing " +str(mean_developing2))
print("Mean of Developed " +str(mean_developed2))

print("Standard Deviation of Developing " +str(std_developing))
print("Standard Deviation of Developing " +str(std_developed))
