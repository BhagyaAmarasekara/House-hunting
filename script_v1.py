# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 09:58:28 2018

@author: Bhagya Amarasekara

This script is for finding the best rental property which suits to our requirements:
    1. nearby to ststaions
    2. sutheastern suburbs
    3. price
    4. min, max bedrooms
    5. not flats or apartments
    
#getting prior informations - station lists and store in a dictionary

"""

import pandas as pd
from geopy.geocoders import Nominatim
import time

df = pd.read_excel('C:/Users/Bhagya Amarasekara/Documents/Bhagya/perw/choose better/train_stations.xlsx')


geolocator = Nominatim()

station_address=[]
station_loc =[]
station_name=[]
not_found=[]

for index,row in df.iterrows():
    place_string = row['Station_name']+" station Melbourne Australia"
    try:
        location = geolocator.geocode(place_string)
        station_address.append(location.address)
        station_loc.append((location.latitude, location.longitude))
        station_name.append(row['Station_name'])
    except:
        not_found.append(row['Station_name'])
        pass

not_found1=[]
for i in not_found:
    place_string = i+" station Melbourne Australia"
    try:
        location = geolocator.geocode(place_string)
        station_address.append(location.address)
        station_loc.append((location.latitude, location.longitude))
        station_name.append(i)
    except:
        not_found1.append(i)
        pass
    
df_station=pd.DataFrame()
df_station['Station']=pd.Series(station_name)
df_station['Station loc']=pd.Series(station_loc,index=df_station.index)
df_station['Station address']=pd.Series(station_address,index=df_station.index)
writer = pd.ExcelWriter('Station geo info.xlsx', engine='xlsxwriter')
# Convert the dataframe to an XlsxWriter Excel object.
df_station.to_excel(writer,index=False,sheet_name='records')
# Close the Pandas Excel writer and output the Excel file.
writer.save()