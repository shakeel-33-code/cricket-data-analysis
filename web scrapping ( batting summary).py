#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import json

with open("C:/Users/shake/OneDrive/Documents/t20_wc1.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

table = soup.find("table")
if not table:
    print("❌ Table not found. Make sure you pasted full table HTML.")
else:
    rows = table.find_all("tr")[1:]  

    batting_summary = []

    for row in rows:
        cols = row.find_all("td")
        if len(cols) >= 15:
            player = {
                "Player": cols[0].text.strip(),
                "Team": cols[1].text.strip(),
                "Mat": cols[2].text.strip(),
                "Inns": cols[3].text.strip(),
                "NO": cols[4].text.strip(),
                "Runs": cols[5].text.strip(),
                "HS": cols[6].text.strip(),
                "Ave": cols[7].text.strip(),
                "BF": cols[8].text.strip(),
                "SR": cols[9].text.strip(),
                "100": cols[10].text.strip(),
                "50": cols[11].text.strip(),
                "0": cols[12].text.strip(),
                "4s": cols[13].text.strip(),
                "6s": cols[14].text.strip()
            }
            batting_summary.append(player)

    with open("t20_wc_batting_summary.json", "w", encoding="utf-8") as json_file:
        json.dump(batting_summary, json_file, indent=4)

    print("✅ Data extracted and saved to t20_wc_batting_summary.json")



# In[ ]:




