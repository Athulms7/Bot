from scrapers.linked_scraper import linkedin_jobs
from scrapers.intern_scraper import internshala_jobs
from scrapers.well_scraper import wellfound_jobs
from scrapers.yc_scraper import yc_jobs
from scrapers.indeed_scraper import indeed_jobs
from email_sender import send_email, filter_jobs

if __name__ == "__main__":
    print("Fetching job listings...")
    all_jobs = []
    for fn in [linkedin_jobs, internshala_jobs, wellfound_jobs, yc_jobs, indeed_jobs]:
        try:
            all_jobs += fn()
        except Exception as e:
            print(f"Error in {fn.__name__}: {e}")

    filtered = filter_jobs(all_jobs)
    send_email(filtered)
    print(f"✅ Sent {len(filtered)} jobs to your inbox.")
