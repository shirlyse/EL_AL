import pandas as pd
import math

#data from authority file
df1 = pd.read_excel("Rashut.xlsx")
df = pd.read_excel("Calculation.xlsx")
df = df.assign(Flight_id=df1["Flight_ID"], Plane_id=df1["Plane_id"], Aparking_time=df1["Parking_Time"],
              Adeparture_Time=df1["Departure_Time"])
#df["Flight_id"].update(df1["Flight_ID"])
df["Aparking_days"] = df["Aparking_time"].apply(lambda x: math.ceil(x / 24))
print(df)

#data from authority file
df2 = pd.read_excel("elal.xlsx") #or Elal
 #df = df.merge(df2[["Flight_ID","Adeparture_Time", "Departure_pit"]], on=["Flight_ID","Adeparture_Time"], how="left")
merged_df = pd.merge(df, df2, left_on=['Flight_id', 'Adeparture_Time'], right_on=['Flight_id2','Departure_date'])


df.loc[:, 'Earrival'] = df2.loc[:, 'Arrival_date']
df.loc[:, 'EArrival_time'] = df2.loc[:, 'Arrival_time']
df.loc[:, 'Edeparture'] = df2.loc[:, 'Departure_date']
df.loc[:, 'EDeparture_time'] = df2.loc[:, 'Departure_time']
df.loc[:, 'Eparking_time'] = df2.loc[:, 'Parking_time']
#TODO	Earrival_london	Edeparture_london		Eparking_day
#change: convert london reshut hour to israeli reshut hour
df['Earrival'] = pd.to_datetime(df['Earrival'], format='%Y-%m-%d %H:%M:%S')
#df['Date'] = df['Date'].dt.date
df["Earrival_london"] = df["Earrival"].apply(lambda x: x-3)

#df= df.assign(Earrival=df2["Flight_ID"], Plane_id=df2["Plane_id"], Aparking_time=df2["Parking_Time"],
            #  Adeparture_Time=df2["Departure_Time"])
#df["Flight_id"].update(df1["Flight_ID"])
#df["Aparking_days"] = df["Aparking_time"].apply(lambda x: math.ceil(x / 24))

df["Departure_time"] = pd.to_datetime(df["Departure_time"], format='%d %H:%M')
df["Departure_time"] = df["Departure_time"].dt.time
df['Departure_time'] = df['Departure_time'].astype(str)
df['Departure'] = df['Departure_date'] + ' ' + df['Departure_time']
df['Departure'] = pd.to_datetime(df['Departure'], format='%d/%m/%Y %H:%M:%S')

#data from ELAL file
df2 = pd.read_excel("elal.xlsx") #or Elal if changes
 #df = df.merge(df2[["Flight_ID","Adeparture_Time", "Departure_pit"]], on=["Flight_ID","Adeparture_Time"], how="left")
merged_df = pd.merge(df, df2, left_on=['Flight_id', 'Adeparture_Time'], right_on=['Flight_id2','Departure_date'])

df = pd.merge(df,df2, on=["Flight_id", "Departure_Time"] ,how="inner")
#df = df.merge(df1.drop_duplicates(), left_on='id'right_on='iso', how='left')
#df = df.merge(df2.drop_duplicates(), left_on='id',
           #     right_on='iso', how='left').drop('iso', 1)
#rajoutter les column de time ds new excel le file de calculation ds le bon ordre
df.loc[:, 'Earrival'] = df2.loc[:, 'Arrival']
df.loc[:, 'Edeparture'] = df2.loc[:, 'Departure']
df.loc[:, 'Eparking_time'] = df2.loc[:, 'Parking_time']

df['Earrival_london'] = df['Earrival'] - pd.DateOffset(hours=3)
df['Edeparture_london'] = df['Edeparture'] - pd.DateOffset(hours=3)


#convert to excel
writer = pd.ExcelWriter(r'Calculation.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1', index=False)
writer.close()
reader = pd.read_excel(r'Calculation.xlsx')
print(reader)