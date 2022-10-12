import pandas as pd
import requests
import md5hash
import sys
import time

sys.path.insert(0,'MentorSkool/Mod5/M')

def Starting_Letter_FilterBlock(private_key,public_key,hash,nameStartsWithArgs):
    print("Retriving Characters whose name start with:",nameStartsWithArgs.upper())
    list_2_Pandas1=[]
    paramsf = dict(
        apikey = public_key,
        ts = ts,
        hash = md5hash(private_key,ts,public_key),
        offset = 0, 
        nameStartsWith = nameStartsWithArgs.upper(),
        limit = '100'
         )
    headers = {'Content-Type':'application/json'}
    response = requests.get(address,params=paramsf,headers=headers)
    res = response.json()
    temp = []
    for i in res['data']['results']:
        temp.append(i['id'])
        temp.append(i['name'])
        temp.append(i['comics']['available'])
        temp.append(i['series']["available"])
        temp.append(i["stories"]["available"])
        temp.append(i["events"]["available"])
        temp.append(i['description'])

        list_2_Pandas1.append(temp)
        temp=[]
    df2 = pd.DataFrame(list_2_Pandas1,columns=['id','Character_Name','Events','Comics','Series','Stories','Description'])
    return(df2)

def Activity_3_Block(*args):
    try:
        if len(args)==4:
            print('Sufficient Arguements passed')
            return(Starting_Letter_FilterBlock(private_key,public_key,hash,Character1))
        else:
            print('''
Not enough Arguements passed \n 
Function needs all 4 Following Parameters
    { 
    Private_key
    Public_key
    Hash
    One Letter
    }''')
    except ValueError as abk:
        print("Invalid Character is inserted")
    