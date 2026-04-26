import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SETTINGS_FILE   = os.path.join(BASE_DIR, "settings.json")
LEADERBOARD_FILE = os.path.join(BASE_DIR, "leaderboard.json")

DEFAULT_SETTINGS = {
    "sound":       True,
    "difficulty":  "medium",   # easy / medium / hard
    "car_color":   "default",  # default (синяя) / red (красная)
    "music_track": 1           # 1 = background.wav, 2 = background_2.wav
}


def load_settings():
    if not os.path.exists(SETTINGS_FILE):
        save_settings(DEFAULT_SETTINGS)
        return DEFAULT_SETTINGS.copy()

    with open(SETTINGS_FILE, "r") as f:
        data = json.load(f)

    # Добавляем недостающие ключи если файл старый
    for key, val in DEFAULT_SETTINGS.items():
        if key not in data:
            data[key] = val

    return data


def save_settings(settings):
    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings, f, indent=4)


def load_leaderboard():
    if not os.path.exists(LEADERBOARD_FILE):
        return []

    with open(LEADERBOARD_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_score(name, score, distance):
    leaderboard = load_leaderboard()

    leaderboard.append({
        "name":     name,
        "score":    score,
        "distance": distance
    })

    leaderboard = sorted(leaderboard, key=lambda x: x["score"], reverse=True)[:10]

    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(leaderboard, f, indent=4)