from keybert import KeyBERT

model = KeyBERT(model='all-MiniLM-L6-v2')

def extract_tags(text: str, top_n: int = 5):
    keywords = model.extract_keywords(text, stop_words='english', top_n=top_n)
    return [kw[0] for kw in keywords]
