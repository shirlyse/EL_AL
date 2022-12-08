import pandas as pd
#create file with relevant columns
df = pd.read_excel(r'C:\Users\sshir\OneDrive\Documents\EL AL PROJECT\original\survey_18576_3112022_065100.xlsx')
df = df.drop(df.columns.difference(df.columns[[9, 5, 6, 10, 11, 24]]), axis=1)
df.columns = ["Arrival_Time", "Date", "Plane_id", "pit1", "pit2", "Parking_Time" ]
#date and time format
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
df['Date'] = df['Date'].dt.date
df['Parking_Time'] = pd.to_datetime(df['Parking_Time'], format='%H:%M')
df['Parking_Time'] = df['Parking_Time'].dt.time
df['Arrival_Time'] = pd.to_datetime(df['Arrival_Time'], format='%H:%M')
df['Arrival_Time'] = df['Arrival_Time'].dt.time
#plane format
df['Plane_id'] = df['Plane_id'].str.slice(0, 3)
print(df)
print(df.dtypes)
#make as an excel file -create a function for that taking the df and wanted name of file
writer = pd.ExcelWriter(r'Towing.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1', index=False)
# Close the Pandas Excel writer and output the Excel file.
writer.close()
reader = pd.read_excel(r'Towing.xlsx')