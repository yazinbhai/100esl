# 🗿 Kerala Talking Statue & Toy Kiosk (100 English Q&A)

An interactive, voice-driven talking installation designed for **Kerala school students** to practice English speaking and listening (ESL Beginner / A1 level).

The microphone and speaker are installed inside a physical statue or toy character. Students walk up to the statue at any time during school hours and ask questions; the statue listens, thinks, and answers aloud in spoken English.

---

## 🌟 Key Features

1. **100 Curated Kerala-Context Questions & Declarative Answers**:
   - Covers Self-Introduction, Family, School, Kerala Nature, Monsoon, Onam, Local Food (Appam, Puttu, Sambar), Animals, and Daily Life.
2. **Accurate Speech-to-Text for Kerala Students**:
   - Tuned to Indian English (`en-IN`) acoustic models.
   - Built-in **Kerala ESL Fuzzy Matching Engine** that understands typical beginner phrasing, phonetics, and contractions (e.g., *"which standard"*, *"whats ur name"*, *"where is u house"*).
3. **Strict Fallback Rule**:
   - If a student asks any question outside the 100 curriculum questions, the statue gently answers:  
     > **"I don't understand the question."**
4. **24/7 Always Awake (Kiosk Mode)**:
   - Utilizes Windows `SetThreadExecutionState` API and HTML5 `Screen Wake Lock` so the PC never dims its screen, sleeps, or turns off the audio interface.
5. **Acoustic Feedback Protection (Anti-Echo)**:
   - Microphone input is automatically muted while the statue's speaker answers, preventing the statue from hearing and re-transcribing its own voice.
6. **Animated Statue Mascot (Web/Visual UI)**:
   - Interactive 2.5D Kerala-themed golden mascot with animated blinking eyes, pulsing sound-wave equalizers, and mouth movements synchronized with voice output.
7. **Two Ready-to-Use Platforms**:
   - **Windows App**: Runs full-screen with borderless app window and auto-allowed mic permissions via `launcher.py` / `run_statue_kiosk.bat`.
   - **Web App**: Zero-dependency standalone HTML/JS application (`web/index.html`) ready to open in any browser or deploy on Netlify/Vercel/GitHub Pages.

---

## 🚀 How to Run

### Option 1: Running as a Windows Kiosk App (Recommended for the Statue)
1. Ensure your microphone and speaker are plugged into the PC (or connected via USB/Bluetooth inside the statue).
2. Double-click **`run_statue_kiosk.bat`** (or open a terminal and run `python launcher.py`).
3. The application will:
   - Lock Windows power management to **Always Awake**.
   - Launch a dedicated, borderless Windows desktop application window in full screen.
   - Automatically enable microphone access without asking for permission prompts each time.

### Option 2: Running the Web App (For Quick Demo / Browser Testing)
1. Open the folder `kerala-talking-statue/web/`.
2. Double-click **`index.html`** in **Google Chrome** or **Microsoft Edge**.
3. Click anywhere on the screen once to grant audio/mic access.
4. Speak into your microphone, or use the interactive **"Test Question"** buttons on the right-hand panel.

---

## 📁 Project Structure

```
kerala-talking-statue/
│
├── data/
│   └── questions.json          # 100 Q&A database with categories, synonyms & keywords
│
├── web/
│   ├── index.html              # Interactive Kiosk UI with animated statue & audio engine
│   └── questions.js            # Client-side bundle for zero-CORS browser execution
│
├── launcher.py                 # Windows power management + App Mode launcher
├── run_statue_kiosk.bat        # 1-click Windows desktop startup shortcut
├── generate_dataset.py         # Reproducible dataset compiler
└── README.md                   # Documentation
```

---

## 🎙️ Hardware Setup Tips for School Statues / Toys

- **Microphone Placement**: Place a high-sensitivity boundary microphone or unidirectional USB mic near the mouth/chest area of the statue.
- **Speaker Placement**: Place a small USB or 3.5mm powered speaker inside the statue with an acoustic mesh opening.
- **Windows Sound Settings**:
  - Set the statue mic as the **Default Recording Device**.
  - Adjust microphone gain in Windows Sound Settings to approximately 75–85% with noise suppression enabled.
