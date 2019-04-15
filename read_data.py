import pandas as pd
import os
import numpy as np
import sys
import json
def readcsv(filename):
    pf = pd.read_csv(filename)
    js = pf.to_json(orient='columns')
    print(type(js))

def readtxt(filename):
#    text_file = open(filename, "r")
#    lines = text_file.read()
#    j = json.loads(lines)
#    print(j)
    a = np.loadtxt(filename,dtype=str)
    b = a.tolist()
    j = json.dumps(b)
#    J = json.dumps(a, ensure_ascii=False)
    print(j)


def readjson(filename):
    with open(filename, 'r') as f:
        temp = json.loads(f.read())
        print(temp)

#filename = 'datatest.xls'
#sheetname = 'datatest'
#readxlsx(filename,sheetname)

#filename = 'datatest.csv'
#readcsv(filename)

filename = 'countries.json'
readjson(filename)
#def readdata(filename):
#    with codecs.open(filename, 'r', 'utf-8') as f:
#        print(f)
