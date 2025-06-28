# 🏏 Data-Driven Analysis and Squad Prediction for ICC Men's T20 World Cup 2022

This project focuses on end-to-end data analytics and predictive modeling for the ICC Men's T20 World Cup 2022. It involves scraping real match data from ESPN Cricinfo, processing and cleaning the data, analyzing performance statistics, generating dashboards in Power BI, and predicting the best possible playing XI using machine learning algorithms.

---

## 📌 Project Features

- ✅ Web scraping from ESPN Cricinfo (Batting, Bowling, Matches, Player Info)
- ✅ Data cleaning and conversion into structured JSON and CSV files
- ✅ Visual analytics using Power BI dashboards
- ✅ Machine learning-based prediction of best playing XI
- ✅ Web deployment support using HTML/CSS
- ✅ End-to-end automated pipeline for sports data analysis

---

## 🛠️ Tech Stack

- **Python** – Core scripting language for scraping and preprocessing  
- **BeautifulSoup & Requests** – Web scraping libraries  
- **Pandas** – Data manipulation and transformation  
- **Power BI** – Dashboard and report visualization  
- **Scikit-learn** – For implementing ML algorithms (Random Forest, Logistic Regression)  
- **HTML/CSS** – For basic website interface and deployment  
- **GitHub Pages / Wix / Lovable AI** – For deployment (optional choices)

---

## 📁 Folder Structure

project-root/
├── scraping/ # All Python scripts for web scraping
├── datasets/ # Cleaned CSV & JSON files
├── dashboard/ # Power BI PBIX files
├── notebooks/ # Jupyter Notebooks for analysis
├── prediction_model/ # ML model code and outputs
├── deployment/ # HTML/CSS files for website
└── README.md # Project documentation

yaml
Copy
Edit

---

## 📊 Power BI Dashboards

- **Batting Strike Rates**
- **Bowling Economy & Wicket Stats**
- **Match Results & Team Comparisons**
- **Player Consistency Trends**

> 📎 PBIX file is available in the `dashboard/` folder and can be viewed using Power BI Desktop.

---

## 🔍 Prediction Logic

- Players are ranked based on batting and bowling points
- Filters applied to ensure 1 wicketkeeper, 2 all-rounders, 4 bowlers, and 4 batsmen
- Feature selection includes: Runs, Wickets, SR, Economy, 4s, 6s, Dot Balls
- Machine learning model trained using `RandomForestClassifier` and validated using cross-validation

---

## 🚀 How to Run

1. Clone the repo  
   ```bash
   git clone https://github.com/your-username/icc-t20-squad-analysis.git
   cd icc-t20-squad-analysis
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run scraping scripts

bash
Copy
Edit
python scraping/scrape_batting.py
python scraping/scrape_bowling.py
Open Jupyter Notebook for analysis

bash
Copy
Edit
jupyter notebook
Launch Power BI and load the PBIX file from dashboard/

📌 Project Highlights
Analyzed over 1000+ player-level stats

Automated squad selection using ML

Designed interactive visual dashboards

Converted raw HTML data into structured formats

📚 Keywords
Web Scraping, T20 World Cup, Sports Analytics, Python, Power BI, Machine Learning, Cricket Statistics, Player Selection, Data Cleaning, Data Visualization

🧠 Future Enhancements
Integration with live APIs for real-time data

Fantasy league recommendation engine

Mobile app for on-the-go visualization

NLP for commentary-based sentiment analysis

👨‍💻 Author
Name: Shakeel Ahamed R

LinkedIn: linkedin.com/in/shakeel-ahamed-r-802802222

GitHub: github.com/shakeel-33-code


