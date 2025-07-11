import random

caption_bank = {
    "Future": [
        "Game Changer OS",
        "Ai Not Everwhere 🚀",
        "Every day counts. Make it happen!",
        "Stay focused.Ai is Comming.",
    ],
    "funny": [
        "Life’s too short to be serious 😜",
        "Warning: 100% pure awesomeness!",
        "This video might cause extreme laughter 😂",
        "Just vibing... 😎"
    ],
    "lifestyle": [
        "Living my best life 🌴",
        "Chasing sunsets and dreams 🌅",
        "Eat. Sleep. Create. Repeat.",
        "Keeping it real 💯"
    ]
}

def get_caption(category):
    return random.choice(caption_bank.get(category, ["New post! ✨"]))
