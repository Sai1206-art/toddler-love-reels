# 🧸 Toddler Love Reels — Prompt Generator

Automatically generates a **daily reel script** for toddler love story reels — the wholesome, viral-style content featuring two cute toddler characters (Aarav & Anaya) in heartwarming situations.

Each generated script includes:
- ✅ **Full scene-by-scene breakdown** (visuals, camera angles, character actions, mood, duration)
- ✅ **Hindi narration/voiceover script** (Devanagari)
- ✅ **Hindi dialogues** and a catchy hook line
- ✅ **Hashtags** for social media

---

## ✨ Features

- **30-day rotating content calendar** — each day has a pre-planned theme, setting, mood, emotional arc, and vibe
- **Consistent characters** — Aarav (boy) & Anaya (girl), same look every reel
- **Gemini 2.0 Flash** — free, creative, fast
- **GitHub Actions automation** — runs daily at 10:30 AM IST, or trigger manually
- **Plain text output** — ready to feed into your video pipeline
- **$0 cost** — entirely free tier

---

## 📂 Project Structure

```
toddler-love-reels/
├── config.py              # Content calendar (30 days), character templates, LLM config
├── generate_prompt.py     # Main script — calls Gemini, generates script, saves output
├── daily_generate.yml     # GitHub Actions workflow (move to .github/workflows/ — see Setup)
├── requirements.txt       # Python dependencies (just `requests`)
├── README.md              # This file
└── output/                # Generated scripts land here
```

---

## 🚀 Setup

### 1. Get a free Gemini API key
1. Go to [Google AI Studio](https://aistudio.google.com/apikey)
2. Click "Create API key"
3. Copy the key

### 2. Clone the repo
```bash
git clone https://github.com/Sai1206-art/toddler-love-reels.git
cd toddler-love-reels
```

### 3. Set your Gemini API key
```bash
# Option A: Environment variable
export GEMINI_API_KEY="your-api-key-here"

# Option B: Save to file
echo "your-api-key-here" > .gemini_api_key
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Run it
```bash
# Generate today's script
python generate_prompt.py

# Generate for a specific day (1-30)
python generate_prompt.py --day 1

# Generate for a specific date
python generate_prompt.py --date 2026-07-22
```

Output is saved to `output/YYYY-MM-DD_dayN_theme.txt`

---

## ⚙️ Enable GitHub Actions (Daily Automation)

The workflow file `daily_generate.yml` is in the repo root (couldn't be pushed to `.github/workflows/` via API due to token scope limitations). To activate:

1. On GitHub, create a new file at `.github/workflows/daily_generate.yml`
2. Copy the content from `daily_generate.yml` in the repo root
3. Delete the root copy (optional)
4. Go to **Settings → Secrets and variables → Actions**
5. Add a new repository secret:
   - Name: `GEMINI_API_KEY`
   - Value: your Gemini API key
6. The workflow runs daily at 10:30 AM IST automatically
7. You can also trigger it manually: **Actions tab → Daily Reel Script Generator → Run workflow**

---

## 📅 Content Calendar (30 Days)

| Day | Theme | Mood |
|-----|-------|------|
| 1 | First Meeting | Curious, shy, heartwarming |
| 2 | Sharing Snacks | Generous, cute |
| 3 | Rain Dance | Playful, romantic |
| 4 | Tiny Promise | Emotional, hopeful |
| 5 | Playground Chase | Energetic, fun |
| 6 | Flower for You | Sweet, tender |
| 7 | Matching Outfits | Funny, adorable |
| 8 | Birthday Surprise | Joyful, surprised |
| 9 | Hide and Seek | Mischievous, giggly |
| 10 | First Fight & Makeup | Emotional, heartwarming |
| 11 | Drawing Together | Creative, wholesome |
| 12 | Tiny Dance | Rhythmic, joyful |
| 13 | Lost & Found | Anxious → relieved, emotional |
| 14 | Sharing Umbrella | Cozy, protective |
| 15 | Sandcastle Promise | Dreamy, hopeful |
| 16 | Diwali Together | Festive, bright |
| 17 | Feeding Puppies | Compassionate, cute |
| 18 | Tiny Letter | Nostalgic, innocent |
| 19 | School Play | Nervous → proud, heartwarming |
| 20 | Star Gazing | Wonder, dreamy |
| 21 | Booped Nose | Giggly, cute |
| 22 | Tiny Picnic | Wholesome, peaceful |
| 23 | First Snow | Wonder, playful |
| 24 | Magic Show | Surprised, delighted |
| 25 | Helping Hand | Caring, sweet |
| 26 | Music Class | Rhythmic, fun |
| 27 | Lost Tooth | Funny, emotional |
| 28 | Color Fight | Chaotic-fun, colorful |
| 29 | Lullaby Goodnight | Tender, sleepy, protective |
| 30 | Graduation Day Hug | Proud, emotional, hopeful |

The calendar cycles every 30 days — on day 31, it starts back at day 1.

---

## 🎬 What Each Script Contains

Every generated script follows this structure:

```
🎬 REEL SCRIPT: [Theme Name]
📅 Day X | Date: YYYY-MM-DD
⏱ Total Duration: ~32 seconds (4 scenes × 8s)
📱 Platform: YouTube Shorts / Instagram Reels

--- SCENE 1 (0-8s) ---
🎥 Camera: [angle, movement]
🎭 Mood: [emotion]
📍 Setting: [location description]
👶 Action: [what Aarav and Anaya do, step by step]
💬 Dialogue: [Hindi dialogue in Devanagari]
🗣 Narration: [Hindi voiceover in Devanagari]

--- SCENE 2 (8-16s) ---
[...same structure...]

--- SCENE 3 (16-24s) ---
[...same structure...]

--- SCENE 4 (24-32s) ---
[...same structure...]

--- METADATA ---
📢 Hook Line: [Hindi hook]
#️⃣ Hashtags: [relevant hashtags]
🎨 Visual Style: [animation description]
🎵 Music Suggestion: [mood/type of background music]
```

---

## 🔧 Customization

### Change the characters
Edit `config.py` → `CHARACTERS` dict. Update names, descriptions, outfits, personalities.

### Add/modify calendar themes
Edit `config.py` → `CONTENT_CALENDAR` list. Each entry needs:
- `day`: number
- `theme`: short name
- `setting`: location/scene description
- `mood`: emotional tone
- `emotional_arc`: step-by-step story progression
- `vibe`: 3-4 word summary

### Change the AI model
Edit `config.py` → `GEMINI_MODEL`. Options:
- `gemini-2.0-flash` (default, recommended)
- `gemini-2.5-flash` (newer, check availability)

---

## 💰 Cost

**$0.00** — Gemini 2.0 Flash free tier covers 1,500 requests/day. You use 1 per day. GitHub Actions is free for public repos (2,000 min/month for private repos — this uses ~1 min/run).
