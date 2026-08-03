#!/usr/bin/env python
# coding: utf-8

# BATTING SUMMARY ANALYSIS
# 

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


batting_df = pd.read_csv("t20_wc_batting_summary.csv")
batting_df.head()


# In[3]:


batting_df.info()
batting_df.isnull().sum()


# In[5]:


batting_df["Runs"] = pd.to_numeric(batting_df["Runs"], errors="coerce")
batting_df["SR"] = pd.to_numeric(batting_df["SR"], errors="coerce")
batting_df["Ave"] = pd.to_numeric(batting_df["Ave"], errors="coerce")
batting_df["4s"] = pd.to_numeric(batting_df["4s"], errors="coerce")
batting_df["6s"] = pd.to_numeric(batting_df["6s"], errors="coerce")


# In[6]:


top_run_scorers = batting_df.sort_values(by="Runs", ascending=False).head(10)
top_run_scorers[["Player", "Team", "Runs"]]


# In[7]:


top_avg = batting_df.sort_values(by="Ave", ascending=False).head(10)
top_avg[["Player", "Ave", "Runs", "Inns"]]


# In[8]:


top_avg = batting_df.sort_values(by="Ave", ascending=False).head(10)
top_avg[["Player", "Ave", "Runs", "Inns"]]



# In[9]:


batting_df["BF"] = pd.to_numeric(batting_df["BF"], errors="coerce")
qualified = batting_df[batting_df["BF"] >= 50]
qualified.sort_values("SR", ascending=False).head(10)[["Player", "SR", "BF", "Runs"]]


# In[10]:


batting_df["100"] = pd.to_numeric(batting_df["100"], errors="coerce")
batting_df[batting_df["100"] > 0][["Player", "Team", "100", "Runs"]]


# In[11]:


batting_df["50"] = pd.to_numeric(batting_df["50"], errors="coerce")
batting_df[batting_df["50"] > 0][["Player", "Team", "50", "Runs"]]


# In[12]:


plt.figure(figsize=(10, 5))
sns.histplot(batting_df["Runs"], bins=20, kde=True)
plt.title("Distribution of Runs")
plt.xlabel("Runs")
plt.ylabel("Frequency")
plt.grid()
plt.show()


# In[13]:


plt.figure(figsize=(10, 5))
sns.histplot(batting_df["SR"], bins=20, color='orange')
plt.title("Distribution of Strike Rate")
plt.xlabel("Strike Rate")
plt.ylabel("Frequency")
plt.grid()
plt.show()


# In[14]:


team_runs = batting_df.groupby("Team")["Runs"].sum().sort_values(ascending=False)
team_runs.plot(kind="bar", figsize=(12, 5), title="Total Runs by Team", color="green")
plt.ylabel("Runs")
plt.grid()
plt.show()


# In[15]:


team_sixes = batting_df.groupby("Team")["6s"].sum().sort_values(ascending=False)
team_sixes.plot(kind="bar", figsize=(12, 5), title="Total Sixes by Team", color="red")
plt.ylabel("6s")
plt.grid()
plt.show()


# In[16]:


batting_df["HS"] = batting_df["HS"].str.replace("*", "", regex=False)
batting_df["HS"] = pd.to_numeric(batting_df["HS"], errors="coerce")
batting_df.sort_values(by="HS", ascending=False).head(10)[["Player", "HS", "Team"]]


# In[17]:


batting_df["0"] = pd.to_numeric(batting_df["0"], errors="coerce")
batting_df.sort_values(by="0", ascending=False).head(10)[["Player", "0", "Team"]]


# In[18]:


batting_df.sort_values(by="BF", ascending=False).head(10)[["Player", "BF", "Runs"]]


# In[19]:


plt.figure(figsize=(10, 6))
sns.heatmap(batting_df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Between Batting Stats")
plt.show()


# In[20]:


batting_df["Score"] = batting_df["Runs"] + batting_df["4s"]*1 + batting_df["6s"]*2 + batting_df["SR"]*0.5
batting_df.sort_values(by="Score", ascending=False).head(10)[["Player", "Runs", "4s", "6s", "SR", "Score"]]


# BOWLING ANALYSIS

# In[21]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[22]:


df_bowling = pd.read_csv("t20_wc_bowling_summary.csv")
df_bowling.head()


# In[23]:


df_bowling.info()


# In[24]:


df_bowling.isnull().sum()


# In[25]:


cols_to_numeric = ["Overs", "Maidens", "Runs", "Wickets", "Economy", "0s", "4s", "6s", "Wides", "No Balls"]
for col in cols_to_numeric:
    df_bowling[col] = pd.to_numeric(df_bowling[col], errors='coerce')


# In[26]:


top_wicket_takers = df_bowling.sort_values(by="Wickets", ascending=False).head(10)
top_wicket_takers[["Player", "Wickets"]]


# In[27]:


plt.figure(figsize=(10,6))
sns.barplot(data=top_wicket_takers, x="Wickets", y="Player", palette="coolwarm")
plt.title("Top 10 Wicket Takers")
plt.xlabel("Wickets")
plt.ylabel("Player")
plt.tight_layout()
plt.show()


# In[28]:


avg_economy = df_bowling["Economy"].mean()
avg_economy


# In[29]:


eco_bowlers = df_bowling[df_bowling["Economy"] < 6]
eco_bowlers[["Player", "Economy"]].sort_values(by="Economy")


# In[30]:


top_maiden = df_bowling.sort_values(by="Maidens", ascending=False).head(5)
plt.pie(top_maiden["Maidens"], labels=top_maiden["Player"], autopct='%1.1f%%')
plt.title("Top 5 Bowlers by Maidens")
plt.show()


# In[31]:


plt.figure(figsize=(10,6))
sns.heatmap(df_bowling[cols_to_numeric].corr(), annot=True, cmap="viridis")
plt.title("Correlation Matrix - Bowling Stats")
plt.show()


# In[32]:


df_bowling.groupby("Team")["Overs"].sum().sort_values(ascending=False)


# In[33]:


plt.figure(figsize=(8,6))
sns.histplot(df_bowling["Wickets"], bins=15, kde=True)
plt.title("Distribution of Wickets")
plt.xlabel("Wickets")
plt.ylabel("Number of Bowlers")
plt.show()


# In[34]:


df_bowling.sort_values(by="0s", ascending=False)[["Player", "0s"]].head()


# In[35]:


df_bowling[df_bowling["Overs"] > 5].sort_values(by="Economy", ascending=False)[["Player", "Economy"]].head()


# In[36]:


df_bowling.sort_values(by="4s", ascending=False)[["Player", "4s"]].head()


# In[37]:


df_bowling.sort_values(by="6s", ascending=False)[["Player", "6s"]].head()


# In[38]:


df_bowling.sort_values(by="Wides", ascending=False)[["Player", "Wides"]].head()


# In[39]:


df_bowling.groupby("Team")["No Balls"].sum().sort_values(ascending=False)


# In[40]:


df_bowling.to_csv("cleaned_t20_wc_bowling_summary.csv", index=False)
print("✅ Cleaned data saved.")


# MATCH SUMMARY
# 

# In[41]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[44]:


df_match = pd.read_csv("t20_wc_match_results.csv")
df_match.head()


# In[45]:


df_match.info()


# In[46]:


df_match.describe(include='all')


# In[47]:


df_match.isnull().sum()


# In[48]:


df_match.columns = df_match.columns.str.strip()
df_match['scorecard'] = df_match['scorecard'].str.strip()
df_match.head()


# In[49]:


df_match['ground'].nunique(), df_match['ground'].unique()


# In[50]:


df_match['matchDate'] = pd.to_datetime(df_match['matchDate'])
df_match.dtypes


# In[51]:


plt.figure(figsize=(10, 5))
sns.histplot(df_match['matchDate'], bins=10, kde=False)
plt.title("Match Frequency Over Time")
plt.xlabel("Date")
plt.ylabel("Number of Matches")
plt.xticks(rotation=45)
plt.show()


# In[52]:


df_match['ground'].value_counts().head(10)


# In[53]:


plt.figure(figsize=(8, 5))
df_match['ground'].value_counts().head(5).plot(kind='bar', color='purple')
plt.title("Top 5 Most Used Grounds")
plt.ylabel("Matches Played")
plt.xticks(rotation=45)
plt.show()


# In[54]:


df_match['winner'].value_counts().head(10)


# In[55]:


plt.figure(figsize=(8, 5))
sns.barplot(x=df_match['winner'].value_counts().head(5).values, 
            y=df_match['winner'].value_counts().head(5).index, palette="viridis")
plt.title("Top 5 Teams with Most Wins")
plt.xlabel("Number of Wins")
plt.ylabel("Team")
plt.show()


# In[56]:


team_counts = df_match['team1'].value_counts() + df_match['team2'].value_counts()
team_counts.sort_values(ascending=False).head(10)


# In[57]:


team_counts.head(5).plot(kind='bar', color='orange')
plt.title("Top 5 Teams by Match Count")
plt.ylabel("Total Matches")
plt.xticks(rotation=45)
plt.show()


# In[58]:


df_match['matchup'] = df_match[['team1', 'team2']].apply(lambda x: ' vs '.join(sorted(x)), axis=1)
df_match['matchup'].value_counts().head(10)


# In[59]:


df_match['margin_numeric'] = df_match['margin'].str.extract('(\d+)').astype(float)
sns.histplot(df_match['margin_numeric'].dropna(), bins=10)
plt.title("Distribution of Winning Margins")
plt.xlabel("Winning Margin")
plt.show()


# In[60]:


df_match['margin_numeric'].mean()


# In[61]:


df_match['matchDate'].value_counts().sort_index().plot(kind='bar', figsize=(15,4))
plt.title("Match Count by Date")
plt.xticks(rotation=90)
plt.show()


# In[62]:


df_match.to_csv("t20_wc_match_results_cleaned.csv", index=False)
print("✅ Cleaned data saved as t20_wc_match_results_cleaned.csv")


# PLAYER INFO ANALYSIS

# In[63]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")


# In[64]:


df_players = pd.read_csv("t20_wc_player_info.csv")
df_players.head()


# In[65]:


df_players.info()


# In[66]:


df_players.isnull().sum()


# In[67]:


df_players['team'].value_counts()


# In[68]:


plt.figure(figsize=(10,6))
sns.countplot(y='team', data=df_players, order=df_players['team'].value_counts().index, palette="coolwarm")
plt.title("Number of Players per Team")
plt.xlabel("Player Count")
plt.ylabel("Team")
plt.show()


# In[69]:


df_players[df_players.duplicated(subset=['name'], keep=False)]


# In[70]:


df_players = df_players.drop_duplicates(subset=['name'])


# In[75]:


df_players.columns




# In[76]:


df_players.columns = df_players.columns.str.strip().str.lower()
df_players.columns


# In[78]:


df_players['playingrole'].value_counts()


# In[80]:


df_players[df_players['playingrole'].str.contains("bowler", case=False)].groupby('team')['name'].count().sort_values(ascending=False).head(5)


# In[81]:


all_rounders = df_players[df_players['playingrole'].str.contains("allrounder", case=False)]
all_rounders['team'].value_counts()


# In[82]:


plt.figure(figsize=(8,5))
all_rounders['team'].value_counts().plot(kind='bar', color='skyblue')
plt.title("All-Rounders per Team")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()


# In[83]:


df_players[df_players['name'].str.contains("Virat", case=False)]


# In[84]:


pd.crosstab(df_players['team'], df_players['playingrole'])


# In[85]:


def categorize_role(role):
    role = role.lower()
    if "batsman" in role:
        return "Batsman"
    elif "bowler" in role:
        return "Bowler"
    elif "allrounder" in role:
        return "All-Rounder"
    elif "keeper" in role:
        return "Wicketkeeper"
    else:
        return "Other"

df_players['role_category'] = df_players['playingrole'].apply(categorize_role)
df_players.head()


# In[86]:


df_players.to_csv("t20_wc_player_info_cleaned.csv", index=False)
print("✅ Cleaned player info saved as t20_wc_player_info_cleaned.csv")


# In[ ]:




