import json
import sys
import requests
from bs4 import BeautifulSoup

USERNAME = "Vaibhavgithub21"

def fetch_contributions():
    url = f"https://github.com/users/{USERNAME}/contributions"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Error fetching contributions: {response.status_code}")
        sys.exit(1)
        
    soup = BeautifulSoup(response.text, "html.parser")
    days_data = []
    
    for td in soup.find_all("td", class_="ContributionCalendar-day"):
        date = td.get("data-date")
        level = td.get("data-level", "0")
        if date:
            days_data.append({
                "date": date,
                "level": int(level)
            })
            
    with open("data/contributions.json", "w") as f:
        json.dump(days_data, f, indent=2)
    print(f"Fetched {len(days_data)} contribution days for {USERNAME}.")

if __name__ == "__main__":
    fetch_contributions()
