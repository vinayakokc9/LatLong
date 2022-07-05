import requests
from bs4 import BeautifulSoup

from openpyxl.workbook import Workbook
from openpyxl import load_workbook

import re

def getLatLong(val):
    url = "https://www.travelmath.com/cities/" 
    
    #val = val.strip()
    
    if(val == "None"):
        return "", ""
    
    #removing multiple spaces
    #val = " ".join(val.split()) 
    
    val = val.split(',')
    if(len(val) != 2):
        return "", ""
    
  #  val[0] = re.sub(r"(\w)([A-Z])", r"\1 \2", val[0])
    val[0] = val[0].strip()
    val[0] = val[0].replace(" ", "+")
    
    val[1] = val[1].strip()
    val[1] = "+" + val[1]
    
    url = url + val[0] + "," + val[1] #creating complete url
    print(url)
    
    req = requests.get(url)

    soup = BeautifulSoup(req.content, "html.parser")

    s = soup.h3.get_text() 
    print(s)
    s = s.split("/")
    print(s)
    
    if(s == "Find a city map"):
        return "", ""
    
    #latLongDigits = [int(s) for s in re.findall(r'\d+', s)] 
    
    latVal = s[0][:-3]
    longVal = s[1][1:-2]
    print(latVal, longVal)
#     longVal = str(latLongDigits[3]) + ":" + str(latLongDigits[4]) + ":" + str(latLongDigits[5])


    return latVal, longVal
    #print(soup.h3.get_text())

wb = load_workbook('TestForageDataHubDatasheet_V15-AlfalfaNAL.xlsm', read_only=False, keep_vba=True)
ws = wb.active

for row in ws.iter_rows(min_row=2, min_col =2, max_col=2, max_row=10):
    for cell in row:
        if(cell.value is None):
            break
        s, k = getLatLong(cell.value)
        #print(f'{cell.row} {cell.column} {cell.value}')
        
        print(f'{cell.row} {cell.column} {cell.value} {s} {k}')
        ws.cell(row=cell.row, column=3, value=s)
        ws.cell(row=cell.row, column=4, value=k)
       
            

wb.save('TestForageDataHubDatasheet_V15-AlfalfaNAL.xlsm')
        
        
        
        
        
        
        
        
        
        
        
        