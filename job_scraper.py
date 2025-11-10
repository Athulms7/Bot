import requests
from bs4 import BeautifulSoup

def get_jobs():
    search_terms = [
        "entry level full stack developer jobs india",
        "full stack developer internships remote",
        "full stack developer jobs y combinator startups"
    ]
    jobs = []

    for term in search_terms:
        url = f"https://www.google.com/search?q={term.replace(' ', '+')}+site:wellfound.com+OR+site:linkedin.com+OR+site:ycombinator.com"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        for link in soup.find_all("a"):
            href = link.get("href", "")
            if "http" in href and "google.com" not in href:
                jobs.append(href.split("&")[0].replace("/url?q=", ""))

    # Remove duplicates
    return list(set(jobs))
