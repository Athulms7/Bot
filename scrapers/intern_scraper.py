import requests
from bs4 import BeautifulSoup

def internshala_jobs():
    url = "https://internshala.com/internships/full-stack-development-internship"
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    jobs = []
    for div in soup.select(".individual_internship"):
        title = div.select_one(".heading_4_5").get_text(strip=True)
        company = div.select_one(".company_name").get_text(strip=True)
        link = "https://internshala.com" + div.select_one("a.view_detail_button")["href"]
        loc = div.select_one(".location_link").get_text(strip=True)
        jobs.append({
            "title": title,
            "company": company,
            "location": loc,
            "link": link,
            "source": "Internshala",
        })
    return jobs
