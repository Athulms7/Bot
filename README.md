Automatically finds entry-level and internship software development jobs every day at 12 PM IST and emails them to you.
This bot searches multiple platforms, filters jobs using your resume skills, and sends a clean, readable email report.

daily-job-finder/
├── main.py
├── requirements.txt
├── scrapers/
│   ├── linkedin_scraper.py
│   ├── internshala_scraper.py
│   ├── wellfound_scraper.py
│   ├── yc_scraper.py
│   └── indeed_scraper.py
├── utils/
│   └── email_sender.py
└── .github/
    └── workflows/
        └── schedule.yml
        
git clone https://github.com/your-username/daily-job-finder.git
cd daily-job-finder

Your workflow file MUST be here:
.github/workflows/schedule.yml

🔥 Daily Full-Stack Job Updates

1. Full Stack Developer Intern — Zomentum
📍 Remote | 🌐 Source: Wellfound
Apply: https://wellfound.com/jobs/12345

2. Junior Software Engineer — Razorpay
📍 Bangalore | 🌐 Source: LinkedIn
Apply: https://linkedin.com/jobs/67890

Found 27 matching jobs today.
