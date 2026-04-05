"""imports or reads your raw dataset; if you scraped, include scraper here"""
import json, os
from google_play_scraper import reviews, Sort

def collect_reviews(app_id='com.getsomeheadspace.android', count=1500):
    print(f"Collecting reviews for {app_id}...")
    result, _ = reviews(app_id, lang='en', country='us', sort=Sort.NEWEST, count=count)
    os.makedirs('data', exist_ok=True)
    with open('data/reviews_raw.jsonl', 'w', encoding='utf-8') as f:
        for r in result:
            json.dump({'id': f"rev_{r['reviewId']}", 'content': r['content'], 'score': r['score']}, f)
            f.write('\n')
    print("Collection complete.")

if __name__ == "__main__":
    collect_reviews()
