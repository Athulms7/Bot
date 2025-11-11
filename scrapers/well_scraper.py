import requests
from bs4 import BeautifulSoup

def wellfound_jobs():
    url = "https://wellfound.com/role/full-stack-developer"
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    jobs = []
    for job in soup.select("a[data-test='StartupResult']"):
        title = job.get_text(strip=True)
        link = "https://wellfound.com" + job.get("href")
        jobs.append({
            "title": title,
            "company": "Startup",
            "location": "—",
            "link": link,
            "source": "Wellfound",
        })
    return jobs
