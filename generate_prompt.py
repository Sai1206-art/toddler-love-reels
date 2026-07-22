"""
Prompt Generator for Toddler Love Reels.

Uses Google Gemini 2.5 Flash (free tier) to generate a full scene-by-scene
breakdown + Hindi dialogue/narration script for a daily toddler love story reel.

Output: Plain text file saved to output/ directory.
"""

import os
import sys
import json
import datetime
import argparse
import requests
from pathlib import Path
from config import (
    GEMINI_MODEL,
    GEMINI_API_URL,
    CHARACTERS,
    CONTENT_CALENDAR,
    REEL_SPECS,
)


# ──────────────────────────────────────────────────────────
# HELPERS
# ──────────────────────────────────────────────────────────

def get_api_key():
    """Read Gemini API key from env var or local file."""
    key = os.environ.get("GEMINI_API_KEY")
    if key:
        return key.strip()

    key_file = Path(__file__).parent / ".gemini_api_key"
    if key_file.exists():
        return key_file.read_text().strip()

    print("ERROR: No Gemini API key found.")
    print("Set GEMINI_API_KEY env var, or save it to .gemini_api_key file.")
    sys.exit(1)


def get_day_slot(date=None):
    """Determine which calendar slot to use for a given date.

    Cycles through the 30-day content calendar starting from the project
    start date (2025-01-01). If today is beyond day 30, it loops back.
    """
    if date is None:
        date = datetime.date.today()

    start_date = datetime.date(2025, 1, 1)
    delta = (date - start_date).days
    slot_index = delta % len(CONTENT_CALENDAR)  # cycles 0..29
    return CONTENT_CALENDAR[slot_index], slot_index + 1


def build_system_prompt():
    """Build the system prompt that defines the AI's role and constraints."""
    boy = CHARACTERS["boy"]
    girl = CHARACTERS["girl"]

    return f"""You are an expert creative scriptwriter for viral social media reels featuring toddler love stories. You specialize in wholesome, heartwarming, and highly shareable content.

## CHARACTERS (use these consistently)
- **Boy ({boy['name']})**: {boy['description']}. Personality: {boy['personality']}
- **Girl ({girl['name']})**: {girl['description']}. Personality: {girl['personality']}

## REEL SPECIFICATIONS
- Duration: {REEL_SPECS['duration_seconds']} seconds total
- {REEL_SPECS['num_scenes']} scenes, each ~{REEL_SPECS['scene_duration_seconds']} seconds
- Aspect ratio: {REEL_SPECS['aspect_ratio']}
- Platform: {REEL_SPECS['platform']}
- Animation style: {REEL_SPECS['animation_style']}

## YOUR TASK
Given a theme, setting, mood, and emotional arc, generate a complete reel script with:

1. FULL SCENE-BY-SCENE BREAKDOWN:
   - Scene number (1-4)
   - Visual description of what happens (detailed enough to generate video from)
   - Camera angle and movement (e.g., wide shot, close-up, tracking shot, low angle)
   - Character actions and expressions (be specific about body language)
   - Mood/atmosphere of the scene
   - Duration (seconds)

2. HINDI DIALOGUE/NARRATION SCRIPT:
   - Background narration in Hindi (voiceover style, like the video has)
   - Any character dialogues in Hindi (keep minimal and age-appropriate — toddlers don't talk much, mostly expressions)
   - Include a catchy Hindi hook/title line for the reel

## OUTPUT FORMAT
Output plain text with clear section headers. Use this exact structure:

=== REEL TITLE ===
[catchy Hindi title line]

=== THEME ===
[theme name]

=== SCENE BREAKDOWN ===

--- Scene 1 ---
Visual: [detailed visual description]
Camera: [camera angle and movement]
Characters: [what Aarav and Anaya are doing, expressions, body language]
Mood: [mood/atmosphere]
Duration: 8 seconds

--- Scene 2 ---
[... same structure ...]

--- Scene 3 ---
[... same structure ...]

--- Scene 4 ---
[... same structure ...]

=== HINDI NARRATION SCRIPT ===
Voiceover (Hindi): [Full narration voiceover in Hindi]
Dialogues (if any): [Any character dialogues in Hindi]
Hook Line (Hindi): [Catchy opening line for the reel caption/title]

=== HASHTAGS ===
[10 relevant Hindi and English hashtags for the reel]

## RULES
- The story must be WHOLESOME, INNOCENT, and EMOTIONAL
- The story must be RELATABLE and highly SHAREABLE (think viral potential)
- Use Hindi (Devanagari script) for all narration and dialogue
- Keep toddler expressions authentic — giggles, shy looks, wide eyes, hugs
- Each scene should flow naturally into the next as one continuous story
- The emotional arc must be clearly visible across the 4 scenes
- Include small, relatable details that make viewers go "awww"
- Avoid any content that isn't child-appropriate
- The boy (Aarav) should always be the one initiating sweet gestures
- The girl (Anaya) should respond with cute, expressive reactions
"""


def build_user_prompt(day_slot, day_number):
    """Build the user prompt with today's theme/setting from the calendar."""
    return f"""Generate today's reel script.

## TODAY'S CREATIVE BRIEF
- Day {day_number} of content calendar
- Theme: {day_slot['theme']}
- Setting: {day_slot['setting']}
- Mood: {day_slot['mood']}
- Emotional Arc: {day_slot['emotional_arc']}
- Vibe: {day_slot['vibe']}

Write the full scene-by-scene breakdown and Hindi narration script following the format specified. Make it go viral."""


def build_custom_idea_prompt(idea):
    """Build a user prompt from a free-form custom idea."""
    return f"""Generate a reel script based on this custom idea:

## CUSTOM IDEA
{idea}

Use the characters Aarav and Anaya as defined. Create a wholesome, emotional toddler love story around this idea. If the idea specifies a setting, mood, or emotional arc, follow it. If not, invent appropriate ones that fit the idea.

Write the full scene-by-scene breakdown and Hindi narration script following the format specified. Make it go viral."""


def call_gemini(system_prompt, user_prompt, api_key):
    """Call Gemini 2.5 Flash API with automatic continuation if truncated."""
    url = GEMINI_API_URL.format(model=GEMINI_MODEL, api_key=api_key)

    headers = {"Content-Type": "application/json"}

    # Build conversation that can be extended for continuation
    contents = [{"role": "user", "parts": [{"text": user_prompt}]}]

    full_text = ""
    max_rounds = 3  # safety limit on continuations

    for round_num in range(max_rounds):
        payload = {
            "system_instruction": {"parts": [{"text": system_prompt}]},
            "contents": contents,
            "generationConfig": {
                "temperature": 0.9,
                "top_p": 0.95,
                "max_output_tokens": 8192,
            },
        }

        try:
            response = requests.post(url, json=payload, headers=headers, timeout=90)
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print(f"Gemini API error: {e}")
            if response.text:
                print(f"Response: {response.text[:500]}")
            sys.exit(1)
        except requests.exceptions.RequestException as e:
            print(f"Network error: {e}")
            sys.exit(1)

        data = response.json()

        try:
            text = data["candidates"][0]["content"]["parts"][0]["text"]
            finish_reason = data["candidates"][0].get("finishReason", "STOP")
        except (KeyError, IndexError):
            print(f"Unexpected API response: {json.dumps(data, indent=2)[:500]}")
            sys.exit(1)

        full_text += text

        # If generation finished normally, we are done
        if finish_reason != "MAX_TOKENS":
            break

        # Otherwise, continue the conversation
        print(f"   (continuing generation, round {round_num + 2}...)")
        contents.append({"role": "model", "parts": [{"text": text}]})
        contents.append({"role": "user", "parts": [{"text": "Continue exactly where you left off. Do not repeat anything. Just finish the script from where it was cut off."}]})

    return full_text


def save_output(text, day_number, date_str):
    """Save the generated script to a text file."""
    output_dir = Path(__file__).parent / "output"
    output_dir.mkdir(exist_ok=True)

    filename = f"{date_str}_day{day_number:02d}_reel_script.txt"
    filepath = output_dir / filename

    filepath.write_text(text, encoding="utf-8")
    return filepath


# ──────────────────────────────────────────────────────────
# MAIN
# ──────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Generate a daily toddler love story reel script."
    )
    parser.add_argument(
        "--date",
        type=str,
        default=None,
        help="Date in YYYY-MM-DD format. Defaults to today.",
    )
    parser.add_argument(
        "--day",
        type=int,
        default=None,
        help="Force a specific calendar day (1-30). Overrides date-based selection.",
    )
    parser.add_argument(
        "--idea",
        type=str,
        default=None,
        help="Custom idea/prompt to generate a reel script from (bypasses the calendar).",
    )
    args = parser.parse_args()

    # Custom idea mode — bypass calendar entirely
    if args.idea:
        idea = args.idea.strip()
        if not idea:
            print("Error: --idea cannot be empty.")
            sys.exit(1)

        date_str = datetime.date.today().isoformat()

        print(f"📅 Date: {date_str}")
        print(f"💡 Custom Idea Mode")
        print(f"📝 Idea: {idea[:80]}{'...' if len(idea) > 80 else ''}")
        print("-" * 50)

        api_key = get_api_key()
        print("🔑 Using Gemini API key: " + api_key[:4] + "..." + api_key[-4:])

        system_prompt = build_system_prompt()
        user_prompt = build_custom_idea_prompt(idea)

        print("🤖 Generating script with Gemini 2.5 Flash...")
        script_text = call_gemini(system_prompt, user_prompt, api_key)

        # Save with a hash-based filename to avoid collisions
        import hashlib
        idea_hash = hashlib.md5(idea.encode()).hexdigest()[:8]
        date_str = datetime.date.today().isoformat()
        filepath = save_output(script_text, 0, f"{date_str}_custom_{idea_hash}")

        print(f"✅ Script saved to: {filepath}")
        print("-" * 50)
        print("\n" + script_text)
        return

    # Determine date
    if args.date:
        try:
            date = datetime.date.fromisoformat(args.date)
        except ValueError:
            print(f"Invalid date format: {args.date}. Use YYYY-MM-DD.")
            sys.exit(1)
    else:
        date = datetime.date.today()

    date_str = date.isoformat()

    # Determine calendar slot
    if args.day:
        day_number = args.day
        if day_number < 1 or day_number > len(CONTENT_CALENDAR):
            print(f"Day must be between 1 and {len(CONTENT_CALENDAR)}.")
            sys.exit(1)
        day_slot = CONTENT_CALENDAR[day_number - 1]
    else:
        day_slot, day_number = get_day_slot(date)

    print(f"📅 Date: {date_str}")
    print(f"📝 Calendar Day {day_number}/30")
    print(f"🎬 Theme: {day_slot['theme']}")
    print(f"🎭 Mood: {day_slot['mood']}")
    print(f"📍 Setting: {day_slot['setting']}")
    print(f"📈 Arc: {day_slot['emotional_arc']}")
    print("-" * 50)

    # Get API key
    api_key = get_api_key()
    print("🔑 Using Gemini API key: " + api_key[:4] + "..." + api_key[-4:])

    # Build prompts
    system_prompt = build_system_prompt()
    user_prompt = build_user_prompt(day_slot, day_number)

    # Generate
    print("🤖 Generating script with Gemini 2.5 Flash...")
    script_text = call_gemini(system_prompt, user_prompt, api_key)

    # Save
    filepath = save_output(script_text, day_number, date_str)
    print(f"✅ Script saved to: {filepath}")
    print("-" * 50)
    print("\n" + script_text)


if __name__ == "__main__":
    main()
