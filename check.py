import glob
AUDIO_STYLE_DIR = 'audio_style'
AUDIO_STYLES = {
    "Bedtime Stories (Style 1)": "Scary Style bedtime",
    "Science Fiction (Style 1)": "Sci-fic Spiderman style 1",
    "Humor & Comedy (Style 1)": "male style 1 comedy",
    "Life Lessons (Style 1)": "moral_style_1",
    "Motivational (Style 1)": "steve harvey style 1 -motivation",
    "Bedtime Stories (Style 2)": "soft style bedtime",
    "Science Fiction (Style 2)": "Sci-fic style 2 bold",
    "Humor & Comedy (Style 2)": "female style 2 comedy",
    "Life Lessons (Style 2)": "moral style 2",
    "Motivational (Style 2)": "elon musk style 2 - motivation"
}
style_dict = {key: f"{AUDIO_STYLE_DIR}/{AUDIO_STYLES[key]}.wav" for key in AUDIO_STYLES.keys()}
print(style_dict)
