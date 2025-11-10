from job_scraper import get_jobs
from email_sender import send_email

if __name__ == "__main__":
    print("Fetching today's job listings...")
    jobs = get_jobs()
    send_email(jobs)
    print("✅ Job email sent successfully!")
