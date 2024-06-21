import pandas as pd
import numpy as np
# data ={"Name":["John","Peter", "Lisa" ],
#          "Age":[25,28,31],
#         "Salary":[300000,450000,250000]  }

# # # ***************creation of data frame

# df =pd.DataFrame(data)
# print(df) 
# read csv files named comapny.csv 
# if not in the same folder just give it file location to read

# print(data)

# data=pd.read_excel("project.xlsx")
# print(data)

# ***************Exploring data in pandas

# print(data.head(50))
# print(data.tail(50)) 
# print(data.info())
# print(data.describe())
# print(data.isnull())
# print(data.isnull().sum())


# *********Dealing with Duplicate values in Pandas(error diraxa)
# data=pd.read_csv("company1.csv")
# print(data["ID"].duplicated())
# print(data.drop_duplicates('ID'))
# print(data["ID"].duplicated().sum())



# ************working with missing data in pandas
# data=pd.read_csv("company1.csv")
# print(data)
# print(data.isnull())
# print(data.dropna())
# print(data.replace(np.nan,"hello i was NaN before"))
# data["Name"]=data ["Name"].replace(np.nan,"Utkarsh")
# print(data)
# print(data["Salary"].mean())
# print(data.fillna(method="bfill"))  #fills as its lower data in place of NaN
# print(data.fillna(method="ffill"))    #fills as its above data in place of NaN


# ********Columns transformation in pandas
# data=pd.read_excel("project.xlsx")
# data.loc[(data["Progress"] ==0),"Improvements"]="no progress"
# data.loc[(data["Progress"]>0),"Improvements"]="improved"
# print(data.head(10))

# data=pd.read_csv("company1.csv")
# print(data)

# data["FullName"]=data["First Name"]+" "+data["Last Name"]
# print(data)

# we can use this to capitalize first alphabets of the word
# data["FullName"]=data["First Name"].str.capitalize()+" "+data["Last Name"]
# print(data)

# data=pd.read_excel("account.xlsx")
# data["Bonus"]=(data["Balance"]/100)*20
# print(data)
# data={"Months":["January","February","March" ,"April"]}
# a=pd.DataFrame(data)
# print(a)
# def extract(value):
#     return value[0:3]
# a["short_month"]=a["Months"].map(extract)
# print(a)

# *************Group by Function in pandas
# data=pd.read_excel("accounts.xlsx")
# # print(data)
# gp=data.groupby(["Department","Gender"]).agg({"Gender":"count"})
# print(gp)


# # ***********Merge , join and concatenate in pandas
# data1={"Emp ID":["E01","E02","E03","E04","E05","E06"],
#        "Names":["Ram","Shyam","Krishna","Vishnu","hanuman","Laxmi"],
#        "Age":[20,21,34,45,12,23]}

# data2={"Emp ID":["E01","E02","E03","E04","E05","E06"],
#        "salary":[12000,23000,34000,21000,7800,32000,]}
# df1=pd.DataFrame(data1)
# df2=pd.DataFrame(data2)

# print(df1)
# print()
# print(df2)

# print(pd.merge(df1,df2, on="Emp ID"))
# print(pd.join()) no join attribute in pandas

# data1={"Emp ID":["E01","E02","E03","E04","E05","E06"],
#        "Names":["Ram","Shyam","Krishna","Vishnu","hanuman","Laxmi"],
#        "Age":[20,21,34,45,12,23]}

# data2={"Emp ID":["E01","E02","E03","E04","E08","E06"],
#        "salary":[12000,23000,34000,21000,7800,32000,]}
# df1=pd.DataFrame(data1)
# df2=pd.DataFrame(data2)
# print(pd.merge(df1,df2, on="Emp ID",how = "left"))
# print(pd.merge(df1,df2, on="Emp ID",how = "right"))


# data1={"Emp ID":["E01","E02","E03","E04","E05","E06"],
#        "Names":["Ram","Shyam","Krishna","Vishnu","hanuman","Laxmi"],
#        "Age":[20,21,34,45,12,23]}

# data2={"Emp ID":["E07","E08","E09","E010","E011","E012"],
#        "Names":["utkarsha","Sriyanka","Priyanshee","Satvik","Dad","Mom"],
#        "Age":[20,21,34,45,12,23]}
# df1=pd.DataFrame(data1)
# df2=pd.DataFrame(data2)

# print(pd.concat([df1,df2]))


# *************Pandas| COmpare Dataframe

# dict={"fruits":["Mango","Apples","Banana","Papaya"],
#       "Price":[100,150,200,400],
#       "Quantity":[15,10,10,3]}
# df1=pd.DataFrame(dict)
# # print(df1)

# df2=df1.copy()

# df2.loc[0,"Price"]=120
# df2.loc[1,"Price"]=120
# df2.loc[2,"Price"]=205
# df2.loc[0,"Quantity"]=17
# df2.loc[1,"Quantity"]=9
# df2.loc[2,"Quantity"]=11
# print(df2)
# print(df1.compare(df2))
# to align
# print(df1.compare(df2,align_axis=0))
# print(df1.compare(df2,keep_equal=True))
# print(df1.compare(df2,keep_shape=True))



# ********Pandas - pivoting and Melting Dataframes

# dict={"Keys":["k1","k2","k1","k2"],
#       "Names":["Ram","Shyam","Krishna","Hari"],
#       "Houses":["Green","Blue","Red","Red"],
#       "Grades":["3rd","4th","5th","6th"]}
# df=pd.DataFrame(dict)
# print(df)
# print(df.pivot(index="Keys",columns="Names",values=["Houses","Grades"]))

dict={"Names":["Ram","Shyam","Krishna","Hari"],
      "Houses":["Green","Blue","Red","Red"],
      "Grades":["3rd","4th","5th","6th"]}
df=pd.DataFrame(dict)
# print(df)
# print(pd.melt(df,id_vars=["Names"],value_vars=["Houses","Grades"]))
print(pd.melt(df,id_vars=["Names"],value_vars=["Houses","Grades"],var_name="Utkarsha",value_name="tiktak"))






 












