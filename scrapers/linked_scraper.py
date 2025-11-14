import requests, os

def linkedin_jobs():
    key = os.getenv("SERP_API_KEY") or ""
    url = "https://serpapi.com/search.json"
    params = {
        "engine": "google_jobs",
        "q": "entry level full stack developer OR internship",
        "location": "India",
        "api_key": key,
    }
    data = requests.get(url, params=params).json()
    jobs = []
    for job in data.get("jobs_results", []):
        jobs.append({
            "title": job.get("title"),
            "company": job.get("company_name"),
            "location": job.get("location"),
            "link": job.get("apply_link"),
            "source": "LinkedIn/Google Jobs",
        })
    return jobs
