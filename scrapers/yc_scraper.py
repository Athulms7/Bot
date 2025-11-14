import requests

def yc_jobs():
    url = "https://www.ycombinator.com/jobs/api"
    data = requests.get(url).json()
    jobs = []
    for j in data.get("jobs", []):
        if "full stack" in j["role"].lower():
            jobs.append({
                "title": j["role"],
                "company": j["company_name"],
                "location": j.get("location", "Remote"),
                "link": j["job_post_url"],
                "source": "YC Jobs",
            })
    return jobs
