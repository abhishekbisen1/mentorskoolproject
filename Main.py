import pandas as pd
import requests
import json
import time
import sys
import Intersection as intersection
import FilterBlock as Filter_Block
sys.path.insert(0,'MentorSkool/Mod5/M')

import Keys

address = Keys.address
private_key = Keys.private_key
public_key = Keys.public_key
ts = str(time.time())
temp=[]
list_2_Pandas=[]

def choice():
    a = input("Enter the choice\n 1. All Character Names(Act1-2) \n 2.Characters whose name start with certain Letter(Act-3) \n 3.Query(Act4-5 ")
    return a
choice()
if choice()==1:
    for j in [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600] :
        paramsf = dict(
            apikey = Keys.public_key,
            ts = str(time.time()),
            hash = md5hash(Keys.private_key,ts,Keys.public_key),
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
    for i in df:
        print (i)
elif choice()== 2:
    import StartingLetterFilterBlock as slfb
    import md5ash 
    slfb.Activity_3_Block(Keys.private_key,Keys.public_key,md5ash(Keys.private_key,ts,Keys.public_key))
elif choice()==3:
    import FilterBlock as FB
    quer = input('Enter Query Like \n "Comics > 30"  or  " Events < 40" ')
    col_list = list(df.columns)+[x.lower() for x in list(df.columns)]
    op_list = ['>','<','=','>=','<='] 
    FB(df,
             intersection(input_statement.split(" "),col_list)[0] ,
             intersection(input_statement.split(" "),op_list)[0] ,
             [int(x) for x in input_statement.split(" ") if x.isdigit()][0] 

             )
    FB.Filter_Block(df,col,cond,val)





Character1 = 'fa'    
            

col_list = list(df.columns)+[x.lower() for x in list(df.columns)]
op_list = ['>','<','=','>=','<=']


input_statement = 'Characters starting with A and comics > 40'
ob = [x for x in input_statement.split(" ") if (x.isalpha()==1 and len(x)==1)]

Filter_Block(df,
             intersection(input_statement.split(" "),col_list)[0] ,
             intersection(input_statement.split(" "),op_list)[0] ,
             [int(x) for x in input_statement.split(" ") if x.isdigit()][0] 

             )
