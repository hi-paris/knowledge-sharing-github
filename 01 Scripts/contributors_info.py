import time
# scrapping github
import os
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import json
from typing import List, Any
from datetime import datetime
from urllib.request import Request, urlopen
import urllib
pd.set_option('display.max_rows', 500)


df_url = pd.read_csv('df_github_url_top_14677.csv')

df_url = df_url.loc[:, ~df_url.columns.str.contains('^Unnamed')]

print(len(df_url["Url Repositories"]))

list_package_name = list(df_url["Url Repositories"])

list_contributor_login_final = []
list_contributor_id_final = []
list_contributor_contributions_final = []
list_master_package_name = []

for j in range(9270,len(list_package_name)):

    list_contributor_login = []
    list_contributor_id = []
    list_contributor_contributions = []
    print(j)
    print(list_package_name[j])

    package_specific = "/".join(list_package_name[j].split("/")[3:5])
    req = Request(f"https://api.github.com/repos/{package_specific}/contributors", headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    webpage = webpage.decode('utf-8')
    soup = BeautifulSoup(webpage, 'html.parser')
    list_tag_graph = soup.findAll("user")
    list_contributors_to_repo = json.loads(str(soup))
        for i in range(0,len(list_contributors_to_repo)):
            list_contributor_login.append(list_contributors_to_repo[i].get("login"))
            list_contributor_id.append(list_contributors_to_repo[i].get("id"))
            list_contributor_contributions.append(list_contributors_to_repo[i].get("contributions"))

        list_contributor_login_final.append(list_contributor_login)
        list_contributor_id_final.append(list_contributor_id)
        list_contributor_contributions_final.append(list_contributor_contributions)
        list_master_package_name.append(list_package_name[j])
    


df_contribution = pd.DataFrame(
    {
     'Package': list_master_package_name,
     'Login':list_contributor_login_final,
     'Id':list_contributor_id_final,
     'Contributions':list_contributor_contributions_final,
    })
df_contribution.to_csv(f"df_contribution_{str(j-1)}.csv",index=False)