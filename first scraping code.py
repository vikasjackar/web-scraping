import requests
from bs4 import BeautifulSoup
from pathlib import Path
import pandas as pd
url="https://www.sportskeeda.com/team/india-national-cricket-team"
r=requests.get(url)
#print(r)
soup = BeautifulSoup(r.text,"html.parser")
#print(soup)
table = soup.find("table",class_="stats-table team-table")
#print(table)
title=table.find_all("th")
#print(titile)
header=[]
for i in title:
    name=i.text
    header.append(name)

df=pd.DataFrame(columns=header)
#print(df)

rows=table.find_all("tr")
for i in rows[1:]:
    first_td=i.find_all("td")[0].find("a").text.strip()
    data = i.find_all("td")[1:]
    row =[tr.text for tr in data]
    row.insert(0,first_td)
    l =len(df)
    df.loc[l]=row 
print(df)
#print(row)


#df.to_excel("inningstar.xlsx")
df.to_csv(r'C:\Users\Surya Pratap Singh\python vs code\gui_of_python.py\vikas\inning.csv', index=False)