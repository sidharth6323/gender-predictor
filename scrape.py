
# To scrape the database of modernindianbabynames.com to get male and female names

import urllib
from bs4 import BeautifulSoup as bs

#scrape male database and store in male.txt
file1=open("male.txt","w")
count=0
for i in range(1,415):
	url="http://www.modernindianbabynames.com/modern_baby_name/starting_with/ANY/M/ANY/10755/"+str(i)
	res=urllib.urlopen(url)
	html=res.read()
	soup=bs(html,"html5lib")
	table=soup.find("table").find_next("tbody")
	tr=table.find_all("tr")
	for j in tr:
		if tr.index(j)==0:
			continue
		td=j.find("td").find_next("td")
		name=td.get_text().strip()
		try:
			file1.write(name+"\n")
			print "written " +str(count) +" names"
			count=count+1
		except:
			pass
file1.close()

#scrape female database and store in female.txt
file2=open("female.txt","w")
count=0
for i in range(1,415):
	url="http://www.modernindianbabynames.com/modern_baby_name/starting_with/ANY/F/ANY/10755/11395"+str(i)
	res=urllib.urlopen(url)
	html=res.read()
	soup=bs(html,"html5lib")
	table=soup.find("table").find_next("tbody")
	tr=table.find_all("tr")
	for j in tr:
		if tr.index(j)==0:
			continue
		td=j.find("td").find_next("td")
		name=td.get_text().strip()
		try:
			file2.write(name+"\n")
			print "written " +str(count) +" name"
			count=count+1
		except:
			pass
file2.close()

#11394 girls  10747 boys