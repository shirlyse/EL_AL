import pandas as pd

#import file, after conversion to csv
df = pd.read_csv(r'C:\Users\sshir\OneDrive\Documents\EL AL PROJECT\original\PitsReport-22_09_01-22_09_16.CSV', error_bad_lines=False, sep="\;", engine="python")

#df = pd.read_excel("pit.xlsx")
# Drop the first 22 rows of the DataFrame
df.drop(df.index[:21], inplace=True)
df = df.reset_index(drop=False)


#KEEP RELEVANT COLOUMNS - see if remove 3 4 9 19 (pits and arrive info
df = df.drop(df.columns.difference(df.columns[[1, 3, 4, 6,  9, 12, 13, 16, 19, 21]]), axis=1)
df.columns = ["Plane_id", "Flight_arrival", "Arrival_date", "Arrival_time", "arrival_pit", "Flight_id", "Departure_date", "Departure_time", "Departure_pit", "Parking_time"]

#Arrival
df["Arrival_time"] = pd.to_datetime(df["Arrival_time"], format='%d %H:%M')
df["Arrival_time"] = df["Arrival_time"].dt.time
df['Arrival_time'] = df['Arrival_time'].astype(str)
df['Arrival'] = df['Arrival_date'] + ' ' + df['Arrival_time']
df['Arrival'] = pd.to_datetime(df['Arrival'], format='%d/%m/%Y %H:%M:%S')

#Departure
df["Departure_time"] = pd.to_datetime(df["Departure_time"], format='%d %H:%M')
df["Departure_time"] = df["Departure_time"].dt.time
df['Departure_time'] = df['Departure_time'].astype(str)
df['Departure'] = df['Departure_date'] + ' ' + df['Departure_time']
df['Departure'] = pd.to_datetime(df['Departure'], format='%d/%m/%Y %H:%M:%S')

print(df)

#make as an excel file -create a function for that taking the df and wanted name of file
writer = pd.ExcelWriter(r'Elal.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1', index=False)
# Close the Pandas Excel writer and output the Excel file.
writer.close()
reader = pd.read_excel(r'Elal.xlsx')
