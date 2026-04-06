from app.sentiment_analyzer import analyze_sentiment

def calculate_trust_score(reviews):
    if not reviews:
        return 0
    sentiments = [analyze_sentiment(review) for review in reviews]
    avg_sentiment = sum(sentiments) / len(sentiments)
    trust_score = round(((avg_sentiment + 1) / 2) * 100, 2)  # Scale 0-100
    return trust_score
