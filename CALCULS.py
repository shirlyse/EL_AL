import pandas as pd
import math

#data from authority file
df1 = pd.read_excel("Rashut.xlsx")
df1['Departure_Time'] = pd.to_datetime(df1['Departure_Time'], format='%d/%m/%Y %H:%M:%S')
df = pd.read_excel("Calculation.xlsx")
df = df.assign(Flight_id=df1["Flight_ID"], Plane_id=df1["Plane_id"], Aparking_time=df1["Parking_Time"],
              Adeparture_Time=df1["Departure_Time"], Adeparture_Date=df1["Date"] )
df["Aparking_days"] = df["Aparking_time"].apply(lambda x: math.ceil(x / 24))

df['Adeparture_Date'] = df['Adeparture_Date'].astype(str)
df["Adeparture_Date"] = df["Adeparture_Date"].str[:4] + "/" + df["Adeparture_Date"].str[5:7]+ "/" + df["Adeparture_Date"].str[-2:]

#data from ELAL file
df2 = pd.read_excel("Elal.xlsx") #or Elal if changes
#plane
#merged_df = pd.merge(df, df2, left_on=['Plane_id', 'Adeparture_Date'], right_on=['Plane_id','Departure_date'], how='left')
merged_df = pd.merge(df, df2, left_on=['Plane_id','Departure_date'], right_on=['Plane_id', 'Adeparture_Date'], how='left')
print(merged_df)
#merged_df.head()
df.loc[:, 'Earrival'] = merged_df.loc[:, 'Arrival']
df.loc[:, 'Edeparture'] = df2.loc[:, 'Departure']
#df.loc[:, 'EDeparture_time'] = df2.loc[:, 'Departure_time']  #
df.loc[:, 'Eparking_time'] = df2.loc[:, 'Parking_time']

#CONVERT TO LONDON TIME
df['Earrival_london'] = df['Earrival'] - pd.DateOffset(hours=3)
df['Edeparture_london'] = df['Edeparture'] - pd.DateOffset(hours=3)

#convert to excel
writer = pd.ExcelWriter(r'Calculation.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1', index=False)
writer.close()
reader = pd.read_excel(r'Calculation.xlsx')
print(reader)
