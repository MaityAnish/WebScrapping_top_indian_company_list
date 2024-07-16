#!/usr/bin/env python
# coding: utf-8

# In[85]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[86]:


url="https://www.ambitionbox.com/list-of-companies?campaign=desktop_nav"


# In[87]:


Headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'}


# In[88]:


webpage=requests.get(url,headers=Headers)


# In[89]:


webpage.text


# In[90]:


webpage_content = webpage.content


# In[91]:


soup=BeautifulSoup(webpage_content,'lxml')


# In[92]:


print(soup.prettify())


# In[93]:


soup.find_all('h1')[0].text


# In[94]:


soup.find_all('h2')


# In[95]:


for i in soup.find_all('h2'):
    print(i.text.strip())


# In[96]:


for i in soup.find_all('p'):
    print(i.text.strip())


# In[97]:


soup.find_all('span',class_='companyCardWrapper__companyRatingValue')


# In[98]:


company_ratings = soup.find_all('span', class_='companyCardWrapper__companyRatingValue')
for rating in company_ratings:
  # Access the text content of each element in the list
  print(rating.text)


# In[99]:


company=soup.find_all('div',class_='companyCardWrapper')


# In[100]:


len(company)


# In[101]:


#company_info=soup.find_all('div',class_='companyCardWrapper__tertiaryInformation')


# In[121]:


company[0].find_all('span',class_='companyCardWrapper__ActionCount')[3].text.strip()


# In[102]:


#len(company_info)


# In[124]:


name=[]
rating=[]
reviews=[]
ctype=[]
#hq=[]
#old=[]
#employees=[]
salaries=[]
interviews=[]
job=[]

for i in company:
    name.append(i.find('h2').text.strip())
    rating.append(i.find('span',class_='companyCardWrapper__companyRatingValue').text.strip())
    reviews.append(i.find_all('span', class_='companyCardWrapper__ActionCount')[0].text.strip())
    ctype.append(i.find('span',class_='companyCardWrapper__interLinking').text.strip())
    salaries.append(i.find_all('span',class_='companyCardWrapper__ActionCount')[1].text.strip())
    interviews.append(i.find_all('span',class_='companyCardWrapper__ActionCount')[3].text.strip())
    job.append(i.find_all('span',class_='companyCardWrapper__ActionCount')[4].text.strip())

d={'Name':name,'Rating':rating,'Reviews':reviews,'Company_Type':ctype,'Salaries':salaries,'Interviews':interviews,'Job':job}
df=pd.DataFrame(d)
df


# #soup.find_all('span',class_='companyCardWrapper__ActionCount')

# In[126]:


df


# In[130]:


df.to_csv(r'D:\Data Analyst\Project\AmbitionBox Data\AmbitionBox.csv',index=False)


# In[ ]:




