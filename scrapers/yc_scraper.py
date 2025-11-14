import requests, json

def yc_jobs():
    url = "https://www.ycombinator.com/jobs/api"
    try:
        r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        data = json.loads(r.text)
    except:
        return []

    jobs = []
    for j in data.get("jobs", []):
        if "full stack" in j.get("role", "").lower():
            jobs.append({
                "title": j["role"],
                "company": j["company_name"],
                "location": j.get("location", "Remote"),
                "link": j["job_post_url"],
                "source": "YC Jobs",
            })
    return jobs
