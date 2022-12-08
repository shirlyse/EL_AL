import pandas as pd

#Create df
df = pd.DataFrame({})
#add columns
df[['Flight_id','Plane_id','Adeparture_Time', 'Adeparture_Date'
    ,'Aparking_time','Aparking_days', 'CPD','cost','Earrival','Edeparture','EDeparture_time' ,
    'Earrival_london', 'Edeparture_london','Eparking_time','Eparking_day','check_days','Transfer_time']] = ''

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter(r'Calculation.xlsx', engine='xlsxwriter')
# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1', index=False)
#Close the Pandas Excel writer and output the Excel file.
writer.close()
reader = pd.read_excel(r'Calculation.xlsx')
print(reader)
