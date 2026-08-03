#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


from bs4 import BeautifulSoup
import json
with open("C:/Users/shake/OneDrive/Documents/t20_wc4.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")
player_cards = soup.select("div.ds-grid > div.ds-grow > a.ds-no-tap-higlight")
player_info = []
for card in player_cards:
    name_tag = card.find("span", class_="ds-text-title-s")
    role_tag = card.find("span", class_="ds-text-tight-s")
    name = name_tag.get_text(strip=True) if name_tag else ""
    role = role_tag.get_text(strip=True) if role_tag else ""
    if name:
        player_info.append({
            "name": name,
            "role": role
        })
with open("t20_wc_player_info.json", "w", encoding="utf-8") as f:
    json.dump({"playerInfo": player_info}, f, indent=4)
print("✅ Player info JSON saved successfully.")


# In[ ]:




