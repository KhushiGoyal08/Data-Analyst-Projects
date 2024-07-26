from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests

url ='https://en.wikipedia.org/wiki/List_of_largest_companies_in_India'

page =requests.get(url)
soup=BeautifulSoup(page.text,features="html.parser")
table =soup.find_all('table')[0]
table_titles = table.find_all("th")
# print(table_titles)
table_title=[titles.text.strip() for titles in table_titles]
# print(table_title)
df = pd.DataFrame(columns=table_title)

table_data =table.find_all("tr")
# print(table_data)

for data in table_data[1:]:
    individual_table_data =[info.text.strip() for info in data ]
    individual_table_data =[inf for inf in individual_table_data if inf !='']
    # print(individual_table_data)
    length = len(df)
    df.loc[length]=individual_table_data

df.to_csv(r'E:/Data Analyst Projects/TopCompany_scrapping_data/Companies.csv',index=False)
df.to_json(r'E:/Data Analyst Projects/TopCompany_scrapping_data/Companies_data.json',index=False)
