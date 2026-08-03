#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import json
with open("C:/Users/shake/OneDrive/Documents/t20_wc2.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")
table = soup.find("table")
if not table:
    print("❌ Table not found. Double-check the HTML copy.")
    exit()
rows = table.find_all("tr")[1:]
bowling_summary = []
for row in rows:
    cols = row.find_all("td")
    if len(cols) >= 11:
        bowler = {
            "Player": cols[0].text.strip(),
            "Team": cols[1].text.strip() if len(cols) > 11 else "",  # Optional if available
            "Overs": cols[1].text.strip(),
            "Maidens": cols[2].text.strip(),
            "Runs": cols[3].text.strip(),
            "Wickets": cols[4].text.strip(),
            "Economy": cols[5].text.strip(),
            "0s": cols[6].text.strip(),
            "4s": cols[7].text.strip(),
            "6s": cols[8].text.strip(),
            "Wides": cols[9].text.strip(),
            "No Balls": cols[10].text.strip()
        }
        bowling_summary.append(bowler)
with open("t20_wc_bowling_summary.json", "w", encoding="utf-8") as json_file:
    json.dump(bowling_summary, json_file, indent=4)
print("✅ JSON saved as t20_wc_bowling_summary.json")


# In[ ]:




