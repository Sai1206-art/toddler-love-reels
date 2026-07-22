# 🧸 Toddler Love Reels — Prompt Generator

Automatically generates a **daily reel script** for toddler love story reels — the wholesome, viral-style content featuring two cute toddler characters (Aarav & Anaya) in heartwarming situations.

Each generated script includes:
- ✅ **Full scene-by-scene breakdown** (visuals, camera angles, character actions, mood, duration)
- ✅ **Hindi narration/voiceover script** (Devanagari)
- ✅ **Hindi dialogues** and a catchy hook line
- ✅ **Hashtags** for social media

---

## ✨ Features

- **30-day rotating content calendar** — each day has a pre-planned theme, setting, mood, and emotional arc
- **Consistent characters** — Aarav (the mini businessman boy) and Anaya (the pink dress girl) in every reel
- **Powered by Google Gemini 2.0 Flash** — 100% free (1,500 requests/day free tier, you use 1/day)
- **Automated via GitHub Actions** — runs daily at 10:30 AM IST, commits the script to the repo automatically
- **Manual trigger** — generate any day's script on-demand
- **Plain text output** — easy to read, easy to feed into your video pipeline

---

## 📂 Project Structure

```
toddler_love_reels/
├── config.py                          # Content calendar, characters, reel specs
├── generate_prompt.py                 # Main script — calls Gemini, generates script
├── output/                            # Generated scripts land here
├── .gemini_api_key                    # Your API key (gitignored, not committed)
├── .github/
│   └── workflows/
│       └── daily_generate.yml         # GitHub Actions — daily auto-run
├── requirements.txt                   # Python deps
├── .gitignore
└── README.md
```

---

## 🚀 Quick Start

### 1. Get a free Gemini API key
1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Click **Create API Key**
3. Copy the key

### 2. Install
```bash
git clone <your-repo-url>
cd toddler_love_reels
pip install -r requirements.txt
```

### 3. Set your API key
```bash
# Option A: Environment variable
export GEMINI_API_KEY="your-key-here"

# Option B: Save to file
echo "your-key-here" > .gemini_api_key
```

### 4. Generate today's script
```bash
python generate_prompt.py
```

The script will be saved to `output/YYYY-MM-DD_dayNN_reel_script.txt`

---

## 📅 Content Calendar

The 30-day calendar is defined in `config.py`. Each day has:
- **Theme** (e.g., "First Meeting", "Rain Dance", "Boop the Nose")
- **Setting** (e.g., "Sunny park playground", "Monsoon courtyard")
- **Mood** (e2.g., "Curious, shy, heartwarming")
- **Emotional Arc** (e.g., "Strangers → shy glances → first smile → holding hands")
- **Vibe** (short creative direction)

### Generate a specific day
```bash
python generate_prompt.py --day 4    # Generate Day 4 (Boop the Nose)
python generate_prompt.py --day 15   # Generate Day 15 (Puppy Love)
```

### Generate for a specific date
```bash
python generate_prompt.py --date 2025-02-14
```

---

## ⚙️ GitHub Actions Automation

The repo includes a GitHub Actions workflow (`.github/workflows/daily_generate.yml`) that:
1. Runs daily at **10:30 AM IST**
2. Calls the generator script
3. Auto-commits the new script to the repo

### Setup:
1. Push this repo to GitHub
2. Go to **Repo Settings → Secrets and Variables → Actions**
3. Add a secret named `GEMINI_API_KEY` with your API key value
4. Done! Scripts will auto-generate daily

To trigger manually: **Actions tab → Daily Reel Script Generator → Run workflow**

---

## 🎬 Reel Specs

| Spec | Value |
|------|-------|
| Duration | 32 seconds (4 × 8s scenes) |
| Aspect Ratio | 9:16 vertical (720×1280) |
| Platform | YouTube Shorts / Instagram Reels |
| Animation Style | High-quality 3D CGI, Pixar/Disney-like |

---

## 🔧 Customization

### Add a new theme to the calendar
Edit `config.py` → `CONTENT_CALENDAR` list. Add a new entry:
```python
{
    "day": 31,
    "theme": "Your New Theme",
    "setting": "Where it happens",
    "mood": "mood words",
    "emotional_arc": "start → middle → end",
    "vibe": "short creative direction"
}
```

### Change characters
Edit `config.py` → `CHARACTERS` dict.

### Change the AI model
Edit `config.py` → `GEMINI_MODEL`. Options:
- `gemini-2.0-flash` (default, recommended)
- `gemini-2.5-flash` (newer, check availability)

---

## 💰 Cost

**$0.00** — Gemini 2.0 Flash free tier covers 1,500 requests/day. You use 1 per day. GitHub Actions is free for public repos (2,000 min/month for private repos — this uses ~1 min/run).
