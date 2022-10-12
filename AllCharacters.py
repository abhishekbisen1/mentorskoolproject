import pandas as pd
import requests
import md5hash
import sys
import time

sys.path.insert(0,'MentorSkool/Mod5/M')


address ="http://gateway.marvel.com/v1/public/characters"


for j in [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600] :
  paramsf = dict(
    apikey = public_key,
    ts = ts,
    hash = md5hash(private_key,ts,public_key),
    offset = j, 
    #nameStartsWith is useless
    limit = '100'
  )
  headers = {'Content-Type':'application/json'}
  response = requests.get(address,params=paramsf,headers=headers)
  res = response.json()
  for i in res['data']['results']:
    temp.append(i['id'])
    temp.append(i['name'])
    temp.append(i['comics']['available'])
    temp.append(i['series']["available"])
    temp.append(i["stories"]["available"])
    temp.append(i["events"]["available"])
    temp.append(i['description'])

    list_2_Pandas.append(temp)
    temp=[]

  
df = pd.DataFrame(list_2_Pandas,columns=['id','Character_Name','Events','Comics','Series','Stories','Description'])

hash = md5hash(private_key,ts,public_key)
