import pandas as pd

data=pd.read_csv("car.data")
# print(data.info)
# print(data.shape)
# print(data.head(10))
# print(data.tail(10))

people = {
    "first": ["Corey", 'Jane', 'John'],
    "last": ["Schafer", 'Doe', 'Doe'],
    "email": ["CoreyMSchafer@gmail.com", 'JaneDoe@email.com', 'JohnDoe@email.com']
}

df=pd.DataFrame(people)

# print(df["email"][0])

# print(df.email)

#print(type(df[["email","last"]]))
#print(df[["email","last"]])
#print(df.columns)

# print(df.iloc[[0,1],2])
# print(df.loc[[0,1],["last","email"]])
# print(data["persons"].value_counts())

#print(data.loc[2]["door"])
# print(data.loc[5:12,"maint":"lug_boot"])

# print(data.set_index("maint",inplace=True))
# data.set_index("maint",inplace=True)
# print(data.index)
# print(data.loc["low"])

