import requests
from bs4 import BeautifulSoup

def internshala_jobs():
    url = "https://internshala.com/internships/full-stack-development-internship"
    r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(r.text, "html.parser")
    jobs = []

    for div in soup.select(".individual_internship"):
        try:
            title_el = div.select_one(".heading_4_5")
            company_el = div.select_one(".company_name")
            loc_el = div.select_one(".location_link")
            link_el = div.select_one("a.view_detail_button")

            if not title_el or not company_el or not link_el:
                continue

            jobs.append({
                "title": title_el.get_text(strip=True),
                "company": company_el.get_text(strip=True),
                "location": loc_el.get_text(strip=True) if loc_el else "—",
                "link": "https://internshala.com" + link_el["href"],
                "source": "Internshala",
            })
        except:
            continue
    return jobs
