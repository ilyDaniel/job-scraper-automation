from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from utils import CSV_PATH, format_jobs_for_csv, save_jobs_to_csv
from utils import get_existing_links
from emailer import send_email


URL = "https://jobsearch.baesystems.com/search-and-apply?_international_locations_checkboxes=united-kingdom&_location_checkboxes=leeds"


def scrape_jobs():
    driver = webdriver.Chrome()
    driver.get(URL)

    wait = WebDriverWait(driver, 15)

    all_jobs = []
    seen_links = set()

    MAX_PAGES = 10
    page_count = 0

    while page_count < MAX_PAGES:

        # Wait for job cards (IMPORTANT: correct selector)
        wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "div.job-card")
            )
        )

        cards = driver.find_elements(By.CSS_SELECTOR, "div.job-card")

        print(f"FOUND CARDS: {len(cards)}")

        for card in cards:
            try:
                title = card.find_element(By.TAG_NAME, "h3").text.strip()
                location = card.find_element(By.CSS_SELECTOR, ".job-card__location").text.strip()

                # link is on parent <a>
                link = card.find_element(By.XPATH, "./ancestor::a").get_attribute("href")

                if not title or not link:
                    continue

                if link in seen_links:
                    continue

                seen_links.add(link)

                all_jobs.append({
                    "title": title,
                    "location": location,
                    "link": link
                })

            except Exception as e:
                print("Card error:", e)
                continue

        # Pagination
        try:
            next_btn = driver.find_element(By.CSS_SELECTOR, "button.facetwp-page.next")

            if "disabled" in next_btn.get_attribute("class"):
                break

            driver.execute_script("arguments[0].click();", next_btn)

            time.sleep(3)
            page_count += 1

        except Exception:
            break

    driver.quit()
    return all_jobs


if __name__ == "__main__":
    print("Starting scraper...")

    jobs = scrape_jobs()
    print(f"Scraped {len(jobs)} jobs")

    # clean data
    clean_jobs = format_jobs_for_csv(jobs)

    # check existing jobs
    existing_links = get_existing_links(CSV_PATH)

    # find new jobs
    new_jobs = [job for job in clean_jobs if job["link"] not in existing_links]

    print("NEW JOBS FOUND:", len(new_jobs))

    if new_jobs:
        print("\nNEW JOBS:")
        for job in new_jobs:
            print(f"- {job['title']} ({job['location']})")

        # save once
        save_jobs_to_csv(new_jobs)

        # send notification
        send_email(new_jobs)

    else:
        print("No new jobs today.")

    print("RAW JOBS:", len(jobs))
    print("CLEAN JOBS:", len(clean_jobs))