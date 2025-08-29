# 📰 News Scraper

## 📌 Overview
This project is a **web scraping tool** built with [Scrapy](https://scrapy.org/).  
It extracts the latest **news headlines, links, publication dates, and summaries** from CNN's RSS Feed:  
[Top Stories RSS Feed](http://rss.cnn.com/rss/cnn_topstories.rss).

The scraped data is stored in a clean **JSON file** for analysis, reporting, or portfolio projects.

---

## ⚙️ Technologies Used
- **Python 3.x**
- **Scrapy Framework**
- **XPath Selectors**
- **JSON Output**

---

## 🚀 How it Works
1. The Scrapy spider sends a request to the CNN RSS Feed.  
2. It parses each **item** in the feed.  
3. Extracts:
   - 📰 **Title**
   - 🔗 **Link**
   - 📅 **Publication Date**
   - 📝 **Description / Summary**
4. Saves the extracted data to a **JSON file**.

---

## 📂 Project Structure
news_scraper/
│
├── news_scraper/ # Scrapy project folder
│ ├── spiders/ # Contains the spider file
│ │ └── news_spider.py
│ ├── items.py
│ ├── pipelines.py
│ └── settings.py
│
├── news.json # Final scraped data
└── README.md # Project documentation

---

## 📊 Example Output
```json
[
  {
    "title": "Some on-air claims about Dominion Voting Systems were false...",
    "link": "https://www.cnn.com/business/live-news/fox-news-dominion-trial-04-18-23/index.html",
    "pubDate": "Wed, 19 Apr 2023 12:44:51 GMT",
    "description": "• Some brief summary here..."
  },
  {
    "title": "Dominion still has pending lawsuits against election deniers...",
    "link": "https://www.cnn.com/business/live-news/fox-news-dominion-trial-04-18-23/h_8d51e3ae2714edaa0dace837305d03b8",
    "pubDate": null,
    "description": null
  }
]


📎 How to Run
1.Clone the repository:

git clone https://github.com/your-username/news_scraper.git


2.Navigate into the project folder:

cd news_scraper


3.Run the spider:

scrapy crawl news_spider -o news.json


⭐ Future Improvements
*Fetch images from the news article pages.

*Add categories / tags for each news item.

*Save data in a database (SQLite / MongoDB).

*Visualize trends or top headlines.

👤 Author:
    Tendo

📧 Email: 
    tendooza123@gmail.com

🔗 GitHub:
    TendoOZA
