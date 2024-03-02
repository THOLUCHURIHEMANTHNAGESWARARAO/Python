import requests
import pandas as pd
from bs4 import BeautifulSoup

response=requests.get("https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy,4io&otracker=nmenu_sub_Electronics_0_Mi")
print(response)
soup=BeautifulSoup(response.content,'html.parser')
print(soup)
names=soup.find_all('div',class_="_4rR01T")
print(names)
name=[]
for i in names[0:20]:
  d=i,get_text()
  name.append(d)
print(name)
prices=soup.find_all('div',class_="_30jeq3 _1_WHN1")
price=[]
for i in price[0:20]:
  d=i.get_text()
  price.append(d)
print(price)
rates=soup.find_all('div',class_="_3LWZlK")
rate=[]
for i in rate[0:20]:
  d=i,get_text()
  rate.append(float(d))
print(rate)
images=soup.find_all('div',class_="_396cs4")
image=[]
for i in image[0:20]:
  d=i['src']
  image.append(d)
print(image)
links=soup.find_all('div',class_="_4rR01T")
link=[]
for i in link[0:20]:
  d="https://www.flipkart.com"+i['href']
  link.append(d)
print(link)
df=pd.DataFrame()
print(df)
