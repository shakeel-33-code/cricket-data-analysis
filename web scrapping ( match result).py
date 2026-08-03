#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[1]:


from bs4 import BeautifulSoup
import json
with open("C:/Users/shake/OneDrive/Documents/t20_wc3.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")
table = soup.find("table")
if not table:
    print("❌ Table not found. Make sure you saved the full HTML table correctly.")
    exit()
rows = table.find_all("tr")[1:]
match_summary = []
for row in rows:
    cols = row.find_all("td")
    if len(cols) >= 7:
        match = {
            "team1": cols[0].text.strip(),
            "team2": cols[1].text.strip(),
            "winner": cols[2].text.strip(),
            "margin": cols[3].text.strip(),
            "ground": cols[4].text.strip(),
            "matchDate": cols[5].text.strip(),
            "scorecard": cols[6].text.strip()
        }
        match_summary.append(match)
with open("t20_wc_match_results.json", "w", encoding="utf-8") as json_file:
    json.dump({"matchSummary": match_summary}, json_file, indent=4)
print("✅ JSON saved as t20_wc_match_results.json")


# In[ ]:




