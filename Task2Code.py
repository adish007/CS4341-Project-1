
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


df_new = data.iloc[:, [0,2,3]]
df_new = df_new.reset_index()
#print(df_new)
#for i in range(len(df_new)):
   # print(i)
myList = []
for index, row in df_new.iterrows():
    if(row["Status"] == "Developed"):
        if ((row['Life expectancy '] > (mean_developed2 - std_developed)) and (row['Life expectancy '] < (mean_developed2 + std_developed))): #82.4208
            #print(row['Life expectancy '])
            myList.append("normal")
            #print("normal")
        else:
            if(row['Life expectancy '] < (mean_developed2 - std_developed)):
                #print(row['Life expectancy ']) 
                myList.append("short")
            else: # makes it long if over 82.42
                #print(row['Life expectancy '])
                myList.append("long")
    if(row["Status"] == "Developing"):
        if ((row['Life expectancy '] > (mean_developing2 - std_developing)) and (row['Life expectancy '] < (mean_developing2 + std_developing))):#58.4781, 75.74476
            myList.append("normal")
        else:
            if(row['Life expectancy '] < (mean_developing2 - std_developing)): #58.4781
                myList.append("short")
            else: # makes it long if over 82.42
                myList.append("long")

df_new["Label"] = myList
df_new

df_new.to_csv("true_label.csv",index = False, sep = ',')