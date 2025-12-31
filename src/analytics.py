import pandas as pd
import numpy as np
from scipy.stats import pearsonr

class AnalyticsBrain:
    def __init__(self, data_path):
        self.df = pd.read_csv(data_path)
        self.df['timestamp'] = pd.to_datetime(self.df['timestamp'])
        
    def get_baseline_probs(self):
        """Calculates baseline probability of being in each quadrant."""
        counts = self.df['quadrant'].value_counts(normalize=True)
        return counts.to_dict()

    def get_correlations(self, target_metric='sleep_hours'):

 
        numeric_df = self.df.select_dtypes(include=[np.number])
        if target_metric not in numeric_df.columns:
            return {}
            
        corrs = {}
        for col in numeric_df.columns:
            if col != target_metric:
         
                valid_data = numeric_df[[target_metric, col]].dropna()
                if len(valid_data) > 10:
                    r, _ = pearsonr(valid_data[target_metric], valid_data[col])
                    corrs[col] = round(r, 3)
        
        return dict(sorted(corrs.items(), key=lambda item: abs(item[1]), reverse=True))

    def simulate_day(self, sleep_hours, steps):
    

        score = 0
        if sleep_hours > 7: score += 20
        if sleep_hours < 5: score -= 30
        if steps > 8000: score += 15
        
        if score > 10: return "Likely High Energy Pleasant"
        if score < -10: return "Risk of Low Energy Unpleasant"
        return "Neutral / Baseline"
