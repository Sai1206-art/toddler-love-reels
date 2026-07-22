"""
Configuration for the Toddler Love Reels Prompt Generator.
Defines the content calendar, character templates, and LLM settings.
"""

# ──────────────────────────────────────────────────────────
# LLM CONFIG
# ──────────────────────────────────────────────────────────
GEMINI_MODEL = "gemini-2.5-flash"
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"

# ──────────────────────────────────────────────────────────
# CHARACTER TEMPLATE (consistent across all reels)
# ──────────────────────────────────────────────────────────
CHARACTERS = {
    "boy": {
        "name": "Aarav",
        "description": "A 3-year-old toddler boy, chubby cheeks, wearing a tiny white shirt with a red mini-tie and a little briefcase — looks like a miniature businessman",
        "personality": "Confident, sweet, protective, expressive — always tries to impress the girl"
    },
    "girl": {
        "name": "Anaya",
        "description": "A 3-year-old toddler girl, rosy cheeks, wearing a cute pink dress with a tiny bow — dainty and adorable",
        "personality": "Curious, shy at first then playful, giggly, expressive — melts at sweet gestures"
    }
}

# ──────────────────────────────────────────────────────────
# CONTENT CALENDAR — Rotating themes & settings
# Each entry = one "day slot" that cycles every N days
# All themes are: happy, relatable, shareable, wholesome
# ──────────────────────────────────────────────────────────
CONTENT_CALENDAR = [
    {
        "day": 1,
        "theme": "First Meeting",
        "setting": "A sunny park playground with swings and flowers",
        "mood": "Curious, shy, heartwarming",
        "emotional_arc": "Strangers → shy glances → first smile → holding hands",
        "vibe": "innocent first crush energy"
    },
    {
        "day": 2,
        "theme": "Sharing Food",
        "setting": "A cozy home dining table with homemade parathas",
        "mood": "Playful, generous, cute",
        "emotional_arc": "Both eating → boy notices girl wants his paratha → shares it → she smiles sweetly",
        "vibe": "sharing is caring, food brings people together"
    },
    {
        "day": 3,
        "theme": "Rain Dance",
        "setting": "An open courtyard during light monsoon rain",
        "mood": "Joyful, carefree, romantic-comedy",
        "emotional_arc": "Rain starts → girl scared → boy holds umbrella over her → both splash in puddles laughing",
        "vibe": "childhood monsoon romance"
    },
    {
        "day": 4,
        "theme": "Boop the Nose",
        "setting": "A warm sunlit living room with soft cushions",
        "mood": "Adorable, cheeky, butterflies",
        "emotional_arc": "Boy walks up → gently boops her nose → she giggles hiding behind hands → both laugh hugging",
        "vibe": "the classic cute gesture that melts hearts"
    },
    {
        "day": 5,
        "theme": "Protecting Her",
        "setting": "A school corridor with big kids walking by",
        "mood": "Brave, protective, touching",
        "emotional_arc": "Big kids rush past → girl gets scared → boy stands in front of her like a shield → holds her hand tightly",
        "vibe": "tiny protector, big heart"
    },
    {
        "day": 6,
        "theme": "Flower Gift",
        "setting": "A garden full of marigolds and roses",
        "mood": "Sweet, bashful, charming",
        "emotional_arc": "Boy picks a flower → shyly walks to girl → gives it to her → she blushes and tucks it in her hair",
        "vibe": "first gift, first blush"
    },
    {
        "day": 7,
        "theme": "Drawing Together",
        "setting": "A preschool classroom with crayons and paper",
        "mood": "Creative, collaborative, wholesome",
        "emotional_arc": "Both drawing separately → boy draws a heart with both their names → shows her → she draws a smiley next to it",
        "vibe": "little artists, big feelings"
    },
    {
        "day": 8,
        "theme": "Hide and Seek",
        "setting": "A living room with sofas, curtains, and a big clock",
        "mood": "Playful, giggly, suspenseful-cute",
        "emotional_arc": "Boy counts → girl hides behind curtain giggling → he finds her → both burst out laughing → hug",
        "vibe": "playful childhood hide-and-seek love"
    },
    {
        "day": 9,
        "theme": "Festival Lights",
        "setting": "A decorated home during Diwali with diyas and fairy lights",
        "mood": "Magical, festive, warm",
        "emotional_arc": "Girl holds a diya carefully → boy lights a sparkler for her → they watch it together → he puts his arm around her",
        "vibe": "festival magic, tiny romance"
    },
    {
        "day": 10,
        "theme": "Feeding Ice Cream",
        "setting": "An ice cream cart on a summer evening street",
        "mood": "Melty, messy, adorable",
        "emotional_arc": "Boy buys one ice cream → takes a bite → offers it to girl → she takes a messy bite → both laugh with ice cream on their faces",
        "vibe": "one ice cream, two smiles"
    },
    {
        "day": 11,
        "theme": "Band-Aid Love",
        "setting": "A playground with a slide and grass",
        "mood": "Caring, gentle, touching",
        "emotional_arc": "Girl falls and scrapes knee → tears in eyes → boy runs over → puts a Band-Aid on it → kisses her forehead → she smiles through tears",
        "vibe": "tiny nurse, big comfort"
    },
    {
        "day": 12,
        "theme": "Matching Outfits",
        "setting": "A family function with decorations and guests",
        "mood": "Proud, twinning, cute",
        "emotional_arc": "Both arrive in matching outfits → notice each other → boy strikes a pose → girl copies → everyone goes aww",
        "vibe": "mini couple goals"
    },
    {
        "day": 13,
        "theme": "Stargazing",
        "setting": "A rooftop on a clear night with a blanket and pillows",
        "mood": "Dreamy, quiet, wonder-filled",
        "emotional_arc": "Both lying on blanket looking up → boy points at a star → whispers something → girl turns to look at him → both smile",
        "vibe": "tiny dreamers under big skies"
    },
    {
        "day": 14,
        "theme": "Dancing in the Rain Music",
        "setting": "A home porch with a small radio playing",
        "mood": "Musical, rhythmic, joyful",
        "emotional_arc": "Music plays → boy offers his hand → girl hesitates then takes it → they sway together → he dips her → both laugh",
        "vibe": "first dance, tiny feet"
    },
    {
        "day": 15,
        "theme": "Puppy Love",
        "setting": "A park bench where a stray puppy sits",
        "mood": "Tender, animal-loving, bonding",
        "emotional_arc": "Both see a puppy → girl is scared → boy picks it up gently → places it in her arms → both pet it together smiling",
        "vibe": "love multiplied by a puppy"
    },
    {
        "day": 16,
        "theme": "Birthday Surprise",
        "setting": "A decorated room with balloons and a small cake",
        "mood": "Surprised, grateful, celebratory",
        "emotional_arc": "Girl walks in blindfolded → boy removes it → she sees the cake → he sings → she blows candle → he hugs her",
        "vibe": "someone remembered, someone cared"
    },
    {
        "day": 17,
        "theme": "Lost and Found",
        "setting": "A crowded market street with shops and people",
        "mood": "Anxious then relieved, emotional",
        "emotional_arc": "Girl gets separated in crowd → looks scared and lost → boy finds her → grabs her hand firmly → wipes her tears → they walk together",
        "vibe": "I'll always find you"
    },
    {
        "day": 18,
        "theme": "Paper Boat Race",
        "setting": "A monsoon puddle/stream in a lane",
        "mood": "Competitive-playful, giggly",
        "emotional_arc": "Both make paper boats → race them in the stream → girl's boat wins → she cheers → boy pretends to sulk → she hugs him",
        "vibe": "tiny competition, tiny victory"
    },
    {
        "day": 19,
        "theme": "Saying Sorry",
        "setting": "A preschool classroom with toys scattered",
        "mood": "Apologetic, sincere, reconciling",
        "emotional_arc": "Boy accidentally breaks girl's toy tower → she gets upset → he rebuilds it → says sorry with puppy eyes → she forgives with a hug",
        "vibe": "first fight, first sorry, first forgive"
    },
    {
        "day": 20,
        "theme": "Sunset Promise",
        "setting": "A hilltop overlooking a city at golden hour",
        "mood": "Nostalgic, warm, bittersweet-hopeful",
        "emotional_arc": "Both sit watching sunset → boy points at the horizon → makes a pinky promise → girl locks pinkies → they lean on each other",
        "vibe": "forever starts tiny"
    },
    {
        "day": 21,
        "theme": "Shadow Game",
        "setting": "A street lamp at dusk casting long shadows",
        "mood": "Playful, creative, magical",
        "emotional_arc": "Boy makes shadow puppets on the wall → girl watches amazed → she tries and fails → he guides her hand → both make a heart shadow together",
        "vibe": "shadow magic, shared creativity"
    },
    {
        "day": 22,
        "theme": "First Rakhi Confusion",
        "setting": "A home during Raksha Bandhan with rakhis and sweets",
        "mood": "Comedy, confused-cute, twist",
        "emotional_arc": "Girl approaches with rakhi → boy thinks it's a gift → extends hand happily → she ties it → he looks confused → then hugs her anyway",
        "vibe": "is this love or sibling bond? adorable confusion"
    },
    {
        "day": 23,
        "theme": "Sharing an Umbrella",
        "setting": "A school gate during sudden rain",
        "mood": "Chivalrous, sweet, classic",
        "emotional_arc": "Rain pours → girl waiting alone → boy runs up with tiny umbrella → holds it over both → walks her home → she smiles the whole way",
        "vibe": "tiny gentleman, big gesture"
    },
    {
        "day": 24,
        "theme": "Diwali Sparkler Duel",
        "setting": "A courtyard with Diwali decorations at night",
        "mood": "Energetic, playful, festive",
        "emotional_arc": "Both hold sparklers → pretend they're swords → duel playfully → sparklers go out → boy lights a new one for her → they hold one together",
        "vibe": "festival lights, tiny knights"
    },
    {
        "day": 25,
        "theme": "Feeding Birds Together",
        "setting": "A park lake with ducks and pigeons",
        "mood": "Gentle, peaceful, bonding",
        "emotional_arc": "Boy brings bread crumbs → shares with girl → they feed ducks together → a duck nips her finger → boy holds her hand to comfort → both laugh",
        "vibe": "shared kindness, tiny nature lovers"
    },
    {
        "day": 26,
        "theme": "The Magic Trick",
        "setting": "A living room with a small table as a stage",
        "mood": "Theatrical, funny, impressive",
        "emotional_arc": "Boy puts on a fake mustache and hat → does a coin trick → girl gasps amazed → coin falls from behind her ear → she giggles uncontrollably",
        "vibe": "tiny magician, big audience of one"
    },
    {
        "day": 27,
        "theme": "Ferris Wheel Fear",
        "setting": "A fairground with a Ferris wheel at sunset",
        "mood": "Scared then brave, sweet",
        "emotional_arc": "Both on Ferris wheel → girl scared of height → grips the bar → boy holds her hand → she calms down → they wave from the top → she's happy",
        "vibe": "fear conquered together"
    },
    {
        "day": 28,
        "theme": "Color Fight",
        "setting": "A street during Holi with colors and water balloons",
        "mood": "Chaotic-fun, colorful, joyous",
        "emotional_arc": "Boy sneaks up with color → smears on girl's cheek → she gasps → grabs a handful → chases him → both covered in colors laughing",
        "vibe": "Holi havoc, colorful love"
    },
    {
        "day": 29,
        "theme": "Lullaby Goodnight",
        "setting": "A cozy bedroom with a night lamp and stars projected on ceiling",
        "mood": "Tender, sleepy, protective",
        "emotional_arc": "Both in pajamas → girl sleepy → boy pats her head → hums a tune → she falls asleep on his shoulder → he pulls blanket over both",
        "vibe": "tiny guardian, sweet dreams"
    },
    {
        "day": 30,
        "theme": "Graduation Day Hug",
        "setting": "A preschool stage with paper caps and a banner",
        "mood": "Proud, emotional, hopeful",
        "emotional_arc": "Both in paper graduation caps → boy gets his certificate → turns to girl → she claps → he runs and hugs her → they hold up certificates together",
        "vibe": "tiny graduates, big futures together"
    },
]

# ──────────────────────────────────────────────────────────
# VIDEO / REEL SPECS
# ──────────────────────────────────────────────────────────
REEL_SPECS = {
    "duration_seconds": 32,
    "num_scenes": 4,
    "scene_duration_seconds": 8,
    "aspect_ratio": "9:16 (vertical, 720x1280)",
    "platform": "YouTube Shorts / Instagram Reels",
    "animation_style": "High-quality 3D CGI, Pixar/Disney-like, photorealistic lighting, warm tones"
}
