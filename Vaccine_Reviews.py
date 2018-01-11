
# coding: utf-8

# In[4]:


from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
chrome_path="C:\Users\Purva Sawant\Desktop\chromedriver_\chromedriver.exe"
driver=webdriver.Chrome(chrome_path)

driver.execute_script("window.scrollTo(0, document.body.scrollheight)")
driver.get('https://www.rxlist.com/script/main/rxlist_view_comments.asp?drug=pneumovax%2023&questionid=fdb5546_pem')
soup=BeautifulSoup(driver.page_source,'lxml')
#print(soup.prettify())
#hospital_names=soup.find_all('p',attrs={'class':'comment'})#using BS I got 40 rows
#hospital_names = [div for div in soup.find_all('div',class_='hospital-name')]
#print (hospital_names)
#k=driver.find_elements_by_xpath("//")#using selenium command also I got 40 rows
#print k
#products = [div for div in hospital_names]

#for product in products:
 #   print(product)
    
hosp_name=soup.find_all('div',attrs={'class':'patComment'})
for i in range(0,len(hosp_name)):
    hosp_name[i]=hosp_name[i].p.contents
hosp_name
    
  
    


# In[12]:


hosp_name[0].contents[0].span.contents


# In[15]:


hosp_name=soup.find_all('div',attrs={'class':'user-comment'})
for i in range(0,len(hosp_name)):
       hosp_name[0].contents[0].span.contents


# In[16]:


hosp_name


# In[17]:


hosp_name=soup.find_all('div',attrs={'class':'user-comment'})
for i in range(0,len(hosp_name)):
       hosp_name[0].contents[0].span.contents
hosp_name


# In[23]:


hosp_name=soup.find_all('div',attrs={'class':'user-comment'})
for i in range(0,len(hosp_name)):
    hosp_name[i]=hosp_name[i].contents[0].span.contents
hosp_name


# In[21]:


hosp_name

