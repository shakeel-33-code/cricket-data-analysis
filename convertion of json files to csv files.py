#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import csv
import os
def json_to_csv(json_file, csv_file, key=None):
    try:
        with open(json_file, "r", encoding="utf-8") as jf:
            data = json.load(jf)
            if key and isinstance(data, dict):
                data = data.get(key, [])
            elif isinstance(data, list):
                pass  # data is already the list
            else:
                print(f"⚠️ Unsupported data format in {json_file}")
                return
            if not data:
                print(f"⚠️ No data found in {json_file}")
                return
            with open(csv_file, "w", newline='', encoding="utf-8") as cf:
                writer = csv.DictWriter(cf, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
            print(f"✅ Converted {json_file} → {csv_file}")
    except Exception as e:
        print(f"❌ Error processing {json_file}: {e}")
json_to_csv("t20_wc_batting_summary.json", "t20_wc_batting_summary.csv")
json_to_csv("t20_wc_bowling_summary.json", "t20_wc_bowling_summary.csv")
json_to_csv("t20_wc_match_results.json", "t20_wc_match_results.csv", key="matchSummary")
json_to_csv("t20_wc_player_info.json", "t20_wc_player_info.csv") 



# In[ ]:




