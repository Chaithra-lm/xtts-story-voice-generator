


# 🎙️ XTTS Story Voice Generator

A personalized AI-powered storytelling voice synthesizer built using [XTTS-v2](https://github.com/coqui-ai/TTS). This project enables the generation of high-quality speech in multiple voice styles (e.g., Sci-Fi, Bedtime, Motivational) from plain text input, supporting multilingual and emotional storytelling.

---

## 🚀 Features

- 🎤 **Voice Cloning**: Clone speaker voices from reference audio.
- 🌈 **Style-Based Generation**: Apply various speaking styles (e.g., bold, soft, comedic, bedtime, etc.).
- 🌍 **Multilingual**: Generate speech in multiple languages.
- 🔄 **Audio Conversion**: Supports `.wav` and `.mp3`, with compression for GitHub compatibility.
- 🧠 **XTTS-v2 Core**: Leverages Coqui XTTS for state-of-the-art zero-shot TTS.
- 🔧 **Preprocessing Tools**: Includes utilities to convert, compress, and manage audio files.

---

## 🗂️ Project Structure

```

Voice-Synthesis/
├── audio\_style/          # Pre-generated audio clips in different styles
├── reference/            # Reference audio samples for cloning
├── scripts/              # Audio preprocessing, conversion tools
├── output\_audio/         # Final synthesized outputs
├── main.py               # Main synthesis script using XTTS
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation

```


## 🛠️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/Chaithra-lm/xtts-story-voice-generator.git
cd xtts-story-voice-generator
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Setup XTTS-v2

Follow the installation instructions from [XTTS-v2 GitHub](https://github.com/coqui-ai/TTS) and place your model checkpoint in the appropriate directory.

### 4. Run synthesis

```bash
python xtts_inference.py --text "Once upon a time..." --style "Sci-fic" --language "en"
```

---

## 🎧 Audio Samples

Visit the `audio_style/` folder to explore different story voices:

* `Sci-fic_style_2_bold_converted.wav`
* `female_style_2_comedy_converted.wav`
* `soft_style_bedtime_converted.wav`
* `elon_musk_style_2_motivation_converted.wav`

---

## 📝 Note: Convert Specific Audio File Before Running

Before running the project, make sure to convert the following file to a `.wav` format under 100MB:

🎧 **Original file:** `audio_style/Sci-fic_style_2_bold_converted.mp3`

🔄 **Conversion command:**

```bash
ffmpeg -i audio_style/Sci-fic_style_2_bold_converted.mp3 -ar 22050 -ac 1 -sample_fmt s16 audio_style/Sci-fic_style_2_bold_converted.wav
```

✅ This ensures the `.wav` file remains under GitHub’s 100MB limit and is compatible with the project.

> 💡 Tip: Use Git LFS to track large audio files like `.wav` and `.mp3`.

---

## 💡 Credits

* **[Coqui.ai XTTS](https://github.com/coqui-ai/TTS)** — backbone TTS engine.

---

## 👩‍💻 Project Developed By

**Chaithra Lokasara Mahadevaswamy** ✅
*AI Enthusiast | 🧠 Data Alchemist | 🎓 Graduate Researcher | 🚀 Innovation Seeker*
**AI Tools Research Intern @ Unicorn Tutor AI**
Chang Gung University, Taoyuan City, Taiwan

📬 [LinkedIn Profile](https://www.linkedin.com/in/chaithra-lokasara-mahadevaswamy-5bb076214/)
🌐 *Building Tomorrow with Intelligence Today*


