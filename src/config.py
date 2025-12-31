import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_RAW = os.path.join(BASE_DIR, 'data', 'raw')
DATA_PROCESSED = os.path.join(BASE_DIR, 'data', 'processed')

HIGH_ENERGY_WORDS = [
    "angry", "annoyed", "anxious", "eager", "energized", "engaged", "enthusiastic",
    "ecstatic", "elated", "determined", "excited", "stressed", "furious", "worried",
    "overwhelmed", "panicked", "alert", "hyped"
]

LOW_ENERGY_WORDS = [
    "tired", "down", "bored", "depressed", "apathetic", "disengaged", "disheartened",
    "calm", "relaxed", "peaceful", "chill", "at ease", "content", "balanced",
    "comfortable", "connected", "accepted"
]

PLEASANT_WORDS = [
    "happy", "calm", "peaceful", "content", "balanced", "grateful", "confident",
    "appreciated", "carefree", "cheerful", "chill", "connected", "delighted",
    "ecstatic", "elated", "enthusiastic", "engaged", "alive", "amazed", "awe",
    "energized", "curious", "determined", "eager", "blessed", "empathetic"
]

UNPLEASANT_WORDS = [
    "angry", "annoyed", "anxious", "ashamed", "alienated", "apprehensive",
    "concerned", "confused", "depressed", "despair", "disappointed",
    "disengaged", "disgusted", "discouraged", "disheartened", "disconnected",
    "down", "embarrassed", "stressed", "worried", "overwhelmed", "panicked"
]
