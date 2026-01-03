import pandas as pd
import numpy as np
from src.config import *

def clean_hwf_data(file_path):

    print(f"Loading {file_path}...")
    df = pd.read_csv(file_path)
    
    cols_to_drop = [
        'Exercise', 'Menstrual', 'Meditation', 'Water (cups)', 
        'Caffeine (mg)', 'Alcoholic Drinks', 'Notes', 'Reflections', 'Takeaways'
    ]
    df = df.drop(columns=cols_to_drop, errors='ignore')

 
    rename_map = {
        'Date': 'timestamp',
        'Mood': 'mood_label',
        'Tags (People)': 'people',
        'Tags (Places)': 'location_label',
        'Tags (Events)': 'activity',
        'Sleep': 'sleep_hours',
        'Steps': 'step_count',
        'Weather': 'weather_desc',
        'Temperature (F)': 'temp_f'
    }
    df = df.rename(columns=rename_map)

  
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    

    df['date_only'] = df['timestamp'].dt.date
    df['hour'] = df['timestamp'].dt.hour
    df['day_name'] = df['timestamp'].dt.day_name()
    

    if 'temp_f' in df.columns:
        df['temp_c'] = (df['temp_f'] - 32) * 5/9
        df['temp_c'] = df['temp_c'].round(1)
        df.drop(columns=['temp_f'], inplace=True)


    if df['sleep_hours'].mean() > 24:
        df['sleep_hours'] = (df['sleep_hours'] / 60).round(2)

    return df

def classify_quadrant(mood):
    """
    Maps a mood string to a psychological quadrant.
    Logic extracted from HWFProj3.ipynb
    """
    if pd.isna(mood): return "Unknown"
    m = mood.lower()
    

    if any(w in m for w in HIGH_ENERGY_WORDS): energy = "high"
    elif any(w in m for w in LOW_ENERGY_WORDS): energy = "low"
    else: energy = "unknown"
    
  
    if any(w in m for w in PLEASANT_WORDS): pleasant = "pleasant"
    elif any(w in m for w in UNPLEASANT_WORDS): pleasant = "unpleasant"
    else: pleasant = "unknown"
    
   
    if pleasant == "pleasant" and energy == "high": return "High Energy Pleasant"
    if pleasant == "pleasant" and energy == "low": return "Low Energy Pleasant"
    if pleasant == "unpleasant" and energy == "high": return "High Energy Unpleasant"
    if pleasant == "unpleasant" and energy == "low": return "Low Energy Unpleasant"
    
    return "Unclassified"

def run_pipeline():
    # Example usage
    raw_path = os.path.join(DATA_RAW, 'how_we_feel.csv')
    df = clean_hwf_data(raw_path)
    df['quadrant'] = df['mood_label'].apply(classify_quadrant)
    
    out_path = os.path.join(DATA_PROCESSED, 'master_dataset.csv')
    df.to_csv(out_path, index=False)
    print(f"Pipeline complete. Saved to {out_path}")

if __name__ == "__main__":
    run_pipeline()
