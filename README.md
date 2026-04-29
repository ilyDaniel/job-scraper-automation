# Job Scraper Automation

A Python-based automation tool that scrapes job listings from a careers website, cleans and processes the data, stores it in a CSV file, and sends email notifications when new roles are detected.

This project is currently a work in progress and being actively improved.

---

## Features

- Web scraping using Selenium
- Multi-page navigation support
- Job data extraction (title, location, link)
- Data cleaning and Unicode normalization
- Deduplication to avoid duplicate job entries across runs
- CSV storage for job history tracking
- Email notifications for newly detected job listings
- Environment variable support for secure credential handling

---

## How it works

1. Loads a careers page using Selenium
2. Extracts job title, location, and URL from job cards
3. Navigates across multiple pages of listings
4. Cleans and normalises scraped text data
5. Compares scraped jobs against previously stored data
6. Stores only new jobs in a CSV file
7. Sends email alerts when new jobs are found

---

## Tech Stack

- Python
- Selenium
- Pandas
- SMTP (email notifications)
- python-dotenv (environment variables)

---

## Current Scope

This project currently works with the BAE Systems careers website.

The scraper is specifically designed around the structure of this site and may require modification to work with other job boards or career pages.

Future updates will aim to make the scraper more generic and configurable for multiple job sources.

---

## Security

Sensitive credentials such as email passwords are stored using environment variables and are excluded from version control.
The .env file should never be pushed to GitHub.

## Project Status

This project is actively being developed. Planned improvements include:
- Scheduling automation (daily runs)
- Support for multiple job websites
- Database storage (SQLite)
- Advanced filtering (keywords, location, job type)
- Integration with Discord or Slack notifications
- Improved scraping resilience for dynamic websites

---

## Notes

This project was built for learning purposes to demonstrate skills in:
- Web scraping
- Automation
- Data processing pipelines
- Basic backend system design