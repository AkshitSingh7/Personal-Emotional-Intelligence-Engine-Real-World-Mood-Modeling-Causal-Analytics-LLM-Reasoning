import pandas as pd
import numpy as np
import random
from datetime import timedelta, date

def generate_mock_dataset(num_days=100):
    print(f"Generating mock data for {num_days} days...")
    
    start_date = date(2024, 1, 1)
    data = []

    # --- LISTS FOR RANDOM CHOICES ---
    moods = [
        "Excited", "Anxious", "Tired", "Content", "Bored", 
        "Stressed", "Joyful", "Apathetic", "Focused", "Angry"
    ]
    activities = ["Coding", "Reading", "Commuting", "Gym", "Meeting", "Gaming"]
    people = ["Alone", "Partner", "Friends", "Colleagues", "Family"]
    locations = ["Home", "Office", "Cafe", "Gym", "Transit"]
    weather_types = ["Sunny", "Rainy", "Cloudy", "Clear", "Haze"]
    cities = ["New Delhi", "Mumbai", "Bangalore", "Pune"]

    for i in range(num_days):
        current_date = start_date + timedelta(days=i)
        is_weekend = current_date.weekday() >= 5
        
        # 1. CORE BEHAVIOR (How We Feel)
        row = {
            'timestamp': current_date,
            'mood_label': random.choice(moods),
            'sleep_hours': round(np.random.normal(7, 1.5), 2),  # Avg 7h sleep
            'step_count': int(np.random.normal(8000, 3000)),    # Avg 8k steps
            'people': random.choice(people),
            'location_label': random.choice(locations),
            'activity': random.choice(activities),
            'weather_desc': random.choice(weather_types),
            'temp_c': round(np.random.uniform(10, 40), 1),
            'date_only': current_date,
            'day_name': current_date.strftime("%A"),
            'hour': random.randint(8, 22)
        }

        # 2. MUSIC (Spotify)
        # Weekends = more music
        row['music_minutes'] = int(np.random.normal(120 if is_weekend else 60, 30))
        row['music_songs_count'] = int(row['music_minutes'] / 3.5) # Approx 3.5 min/song
        row['music_skip_count'] = int(row['music_songs_count'] * np.random.uniform(0.1, 0.5))
        row['music_skip_rate'] = round(row['music_skip_count'] / max(1, row['music_songs_count']), 2)
        row['top_artist'] = f"Artist_{random.randint(1, 50)}"

        # 3. FINANCE (Paytm)
        # Higher spend on weekends
        base_spend = 2000 if is_weekend else 500
        row['total_spend'] = round(abs(np.random.normal(base_spend, 1000)), 2)
        row['food_spend'] = round(row['total_spend'] * np.random.uniform(0.3, 0.6), 2)
        row['entertainment_spend'] = round(row['total_spend'] * np.random.uniform(0.1, 0.4), 2)
        row['txn_count'] = np.random.randint(1, 10)

        # 4. DIGITAL (Firefox)
        total_visits = np.random.randint(50, 300)
        prod_visits = int(total_visits * np.random.uniform(0.2, 0.8))
        row['total_visits'] = total_visits
        row['productive_visits'] = prod_visits
        row['distraction_visits'] = total_visits - prod_visits
        row['productivity_score'] = round(prod_visits / total_visits, 2)
        row['distraction_ratio'] = round((total_visits - prod_visits) / total_visits, 2)

        # 5. ENVIRONMENT (OpenAQ)
        # Worse air quality in winter (months 11, 12, 1, 2)
        if current_date.month in [11, 12, 1, 2]:
            row['pm2_5'] = int(np.random.normal(250, 50))
        else:
            row['pm2_5'] = int(np.random.normal(80, 30))
        row['location_city'] = random.choice(cities)

        # 6. MACRO CONTEXT (News Sentiment)
        # Float between -1 (Negative) and 1 (Positive)
        row['india_news_sentiment'] = round(np.random.uniform(-0.5, 0.5), 3)

        data.append(row)

    # Convert to DataFrame
    df = pd.DataFrame(data)
    
    # Save to mock folder
    output_path = 'data/mock_samples/master_dataset_mock.csv'
    df.to_csv(output_path, index=False)
    print(f"✅ Success! Mock dataset with {len(df.columns)} columns saved to {output_path}")
    print("Columns included:", list(df.columns))

if __name__ == "__main__":
    generate_mock_dataset()
