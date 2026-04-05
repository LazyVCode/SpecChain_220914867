"""cleans raw data & make clean dataset"""
import json, re, string, nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

def clean_data():
    cleaned = []
    seen = set()
    lemmatizer = WordNetLemmatizer()
    stops = set(stopwords.words('english'))

    with open('data/reviews_raw.jsonl', 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line)
            txt = str(data.get('content', '')).lower()
            txt = re.sub(f'[{re.escape(string.punctuation)}]', '', txt)
            txt = re.sub(r'\d+', '', txt)
            txt = ' '.join([lemmatizer.lemmatize(w) for w in txt.split() if w not in stops])
            
            if len(txt.split()) >= 4 and txt not in seen:
                seen.add(txt)
                cleaned.append({'id': data['id'], 'clean_content': txt, 'original': data['content']})

    with open('data/reviews_clean.jsonl', 'w', encoding='utf-8') as f:
        for r in cleaned:
            json.dump(r, f)
            f.write('\n')
    print(f"Cleaned dataset saved: {len(cleaned)} reviews.")

if __name__ == "__main__":
    clean_data()
