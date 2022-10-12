import pandas as pd
import sys

sys.path.insert(0,'MentorSkool/Mod5/M')

def Filter_Block(df,col,condition,value):
    df2=pd.DataFrame()
    if condition=='>':
        df2 = df[df[col.capitalize()]>value]
    elif condition=='<':
        df2 = df[df[col.capitalize()]<value]
    elif condition =='=':
        df2 = df[df[col.capitalize()]==value]
    elif condition == ('<=' or '=<'):
        df2 = df[df[col.capitalize()]<=value]
    elif condition == ('>=' or '=>'):
        df2 = df[df[col.capitalize()]>=value]
    return df2
