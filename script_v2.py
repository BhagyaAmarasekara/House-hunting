# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 15:13:38 2018

@author: Bhagya Amarasekara

for getting domain listings
"""

import requests, json
import pandas as pd

df = pd.read_excel('C:/Users/Bhagya Amarasekara/Documents/Bhagya/perw/choose better/Station geo info.xlsx')
suburbs=df['Station address'].tolist()
u_suburbs=list(set(suburbs))

clientId = "****************"
cpassword = "************"

url = 'https://auth.domain.com.au/v1/connect/token'
payload = {"grant_type":"client_credentials","scope":"api_listings_write"}

r = requests.post(url,data=payload, auth =(clientId,cpassword))

tokens  =  json.loads(r.text)

access_token  =  tokens[ 'access_token' ]

api_call_headers  ={'Authorization':'Bearer '+  tokens['access_token'],'ContentType':"application/json",'X-Originating-Ip': '210.8.195.18'}

search_url='https://api.domain.com.au/v1/listings/residential/_search'

api_call_response  =  requests.get(search_url, headers = api_call_headers, params = {
  "listingType":"",
  "minBedrooms":-1,
  "maxBedrooms":-1,
  "minBathrooms":-1,
  "maxBathrooms":-1,
  "minCarspaces":"",
  "maxCarspaces":"",
  "minPrice":"",
  "maxPrice":"",
  "minLandArea":"",
  "maxLandArea":"",
  "locationTerms":"",
  "inspectionFrom":"",
  "inspectionTo":"",
  "auctionFrom":"",
  "auctionTo":"",
  "sort":{
    "sortKey":"",
    "proximityTo":{
      "lat":-1,
      "lon":-1
    }
  },
  "page":"",
  "pageSize":"",
  "geoWindow":{
    "box":{
      "topLeft":{
        "lat":-1,
        "lon":-1
      },
      "bottomRight":{
        "lat":-1,
        "lon":-1
      }
    },
    "circle":{
      "center":{
        "lat":-1,
        "lon":-1
      },
      "radiusInMeters":""
    },
    "polygon":{

    }
  }
} )
