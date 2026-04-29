import pandas as pd
import os

# project root-safe path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

# ensure folder exists
os.makedirs(DATA_DIR, exist_ok=True)

CSV_PATH = os.path.join(DATA_DIR, "job_listings2.csv")


def format_jobs_for_csv(jobs):
    cleaned = []

    for job in jobs:
        title = str(job.get("title") or job.get("Title") or "").strip()
        location = str(job.get("location") or job.get("Location") or "").strip()
        link = str(job.get("link") or job.get("url") or "").strip()

        if title and link:
            cleaned.append({
                "title": title,
                "location": location,
                "link": link
            })


    return cleaned


def save_jobs_to_csv(jobs):
    """
    Save or append jobs to CSV in /data folder
    """

    df = pd.DataFrame(jobs)

    if os.path.exists(CSV_PATH):
        df.to_csv(CSV_PATH, mode="a", index=False, header=False)
    else:
        df.to_csv(CSV_PATH, index=False)


    print("ROWS BEING WRITTEN:", len(jobs))
    print(f"Saved to: {CSV_PATH}")




def get_existing_links(csv_path):
    if not os.path.exists(csv_path):
        return set()

    df = pd.read_csv(csv_path)
    return set(df["link"].tolist())