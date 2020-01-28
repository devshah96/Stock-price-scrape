import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import os
cwd = os.getcwd()
print(cwd)

start_time = time.time()

def t(col):
    l= []
    for i in col:
        if i[0] == '-':
            l.append(0-float(i[1:-1]))
        else:
            l.append(float(i[1:-1]))
    return(l)

consumer_defensive = requests.get("https://www.stockmonitor.com/sector/consumer-defensive/")
basic_materials = requests.get("https://www.stockmonitor.com/sector/basic-materials/")
communication = requests.get("https://www.stockmonitor.com/sector/communication-services/")
consumer_cyclical = requests.get("https://www.stockmonitor.com/sector/consumer-cyclical/")
consumer_defensive = requests.get("https://www.stockmonitor.com/sector/consumer-defensive/")
energy = requests.get("https://www.stockmonitor.com/sector/energy/")
financial_services = requests.get("https://www.stockmonitor.com/sector/financial-services/")
healthcare = requests.get("https://www.stockmonitor.com/sector/healthcare/")
industrials = requests.get("https://www.stockmonitor.com/sector/industrials/")
technology = requests.get("https://www.stockmonitor.com/sector/technology/")
utilities = requests.get("https://www.stockmonitor.com/sector/utilities/")

d = {consumer_defensive:"consumer-defensive",
	 basic_materials:"basic-materials",
	 communication:"communication",
	 consumer_cyclical:"consumer_cyclical",
	 consumer_defensive:"consumer_defensive",
	 energy:"energy",
	 financial_services:"financial-services",
	 healthcare : "healthcare",
	 industrials : "industrials",
	 technology:"technology",
	 utilities:"utilities"
}

categories = [consumer_defensive,
	basic_materials,
	communication,
	consumer_cyclical,
	consumer_defensive,
	energy,
	financial_services,
	healthcare,
	industrials,
	technology,
	utilities]
df= pd.DataFrame(columns = ["change","symbol","name","price","volume","high","low","sector"])
 

for i in categories:
	soup = BeautifulSoup(i.content,"html.parser")
	l=[]
	for row in soup.table.find_all('tr')[1:]:
		a = row.find_all('td')
		f=[]
		for j in a:
			temp = j.text.replace("\n","")
			f.append(temp.replace(" ",""))
		f.append(d[i])
		l.append(f)
	ty = pd.DataFrame(data = l,columns = ["change","symbol","name","price","volume","high","low","sector"])
	df = df.append(ty)

df['change'] = df['change'].map(lambda x: str(x)[1:])
df['high'] = df['high'].str.replace(',',"")
df['low'] = df['low'].str.replace(',',"")
df['price'] = df['price'].str.replace(',',"")

df['change'] = t(df['change'])
df['high'] = df['high'].astype('float')
df['low'] = df['low'].astype('float')
df['price'] = df['price'].astype('float')
# df1 = pd.read_csv('sector.csv')
# print(df1)
df.to_csv('sector.csv')
print(df)
end_time = time.time()

print(end_time -start_time)


