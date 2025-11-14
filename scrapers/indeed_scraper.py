import requests
from bs4 import BeautifulSoup

def indeed_jobs():
    url = "https://in.indeed.com/jobs?q=full+stack+developer+internship"
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    jobs = []
    for div in soup.select("td.resultContent"):
        title = div.select_one("h2 span").get_text(strip=True)
        company = div.select_one("span.companyName")
        company = company.get_text(strip=True) if company else "—"
        link = "https://in.indeed.com" + div.find("a")["href"]
        jobs.append({
            "title": title,
            "company": company,
            "location": "—",
            "link": link,
            "source": "Indeed",
        })
    return jobs
