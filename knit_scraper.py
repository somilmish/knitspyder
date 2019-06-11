'''
fetches results from knit.ac.in
mca and lateral results are not included
'''


import requests
import re
import operator
from bs4 import BeautifulSoup


def showResults(max_pages,branch,year,data):
    page = 1
    while page<max_pages:

        if page>= 10:
            url='http://knit.ac.in/coe/ODD_2016/btreg16xcdaz.asp?rollno='+str(year)+str(branch)+str(page)
        else:
            url = 'http://knit.ac.in/coe/ODD_2016/btreg16xcdaz.asp?rollno=' +str(year)+str(branch)+'0'+str(page)
        source_code=requests.get(url)
        plain_text=source_code.text
        soup=BeautifulSoup(plain_text)
        link=soup.get_text()
        if year is 15:
            location=link.find('Final Year')
            string = str(link[location + 12:location + 16])
        elif year is 16:
            location = link.find('Third Year')
            string = str(link[location + 11:location + 15])
        elif year is 17:
            location = link.find('Second Year')
            string = str(link[location + 11:location + 15])
        elif year is 18:
            location = link.find('First Year')
            string = str(link[location + 11:location + 15])
        nameLocation=link.find('Name:')+5
        nameEndLocation=link.find('Roll No:')-4
        name=str(link[nameLocation:nameEndLocation])
        if(re.search(r'\d', string)):
            marks = float(string)
            while marks in data.keys():
                marks=marks+.01


            data[marks]=name

        page+=1
    return data
data=dict()
branch=int(input("Enter Branch code[1,2,3...]"))
year=int(input("Enter Year [13/14/15/16/17/18/19]"))
updatedData=showResults(70,branch,year,data)
sorted_data = sorted(updatedData.items(), key=operator.itemgetter(0),reverse=True)
counter=0;
counter2=0;
prevval=-1
for k,v in sorted_data:
    counter2+=1
    if(prevval != int(k)):
        counter=counter2
    print("#",counter," ",v," ",int(k)," ",k/20)
    prevval=int(k)


print('Successfully completed')
