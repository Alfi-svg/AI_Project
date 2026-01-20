# AI_Project
This project presents a fully offline AI-based video analysis system developed for an AI hackathon.
# 📘 README.md

## Offline AI-Based Video Analysis System

**(Phase-I & Phase-II Combined)**

---

## 📌 Project Overview

This project presents a **fully offline, AI-based video analysis system** developed for an AI hackathon.
The system is capable of analyzing video content to:

* Extract speech and generate text (Bangla & English)
* Perform Bangladesh-context sentiment analysis
* Generate explainable AI outputs
* Analyze presenter motion and visual behavior (non-verbal cues)

The entire system operates **without any external API, cloud service, or internet dependency**, strictly following all competition constraints.

---

## 🎯 Project Objectives

### Phase-I Objectives:

* Convert video speech into text using a trained ASR model
* Analyze generated text for sentiment (Positive, Negative, Neutral)
* Provide explainable AI-based reasoning for sentiment decisions

### Phase-II Objectives:

* Analyze presenter posture, gestures, eye-contact approximation, and movement
* Extract time-based, explainable visual and motion features
* Generate structured datasets and statistical summaries

---

## 🧠 AI Models Used

### Automatic Speech Recognition (ASR)

* Framework: TensorFlow / Keras
* Model Type: End-to-End Speech-to-Text
* Loss Function: CTC (Connectionist Temporal Classification)
* Transcription Level: Character-level
* Languages Supported: Bangla and English
* Model Format: TensorFlow SavedModel

Model loading is performed using:

```python
tf.keras.models.load_model()
```

---

## 🗂️ Project Structure

```text
AI_VIDEO_ANALYSIS_PROJECT/
│
├── backend/
│   ├── main.py
│   ├── config.py
│   ├── asr/
│   ├── sentiment/
│   ├── vision/
│   ├── utils/
│   ├── data/
│   │   └── BengaliDictionary_93.json
│   └── model/
│       ├── saved_model.pb
│       └── variables/
│
├── ui/
│   └── index.html
│
├── requirements.txt
├── README.md
└── documentation/
    ├── Phase_I_Documentation.pdf
    └── Phase_II_Documentation.pdf
```

---

## ⚙️ System Workflow

### Phase-I Workflow:

1. User provides video input (file or offline link)
2. Audio is extracted from the video
3. Speech is converted to text using the ASR model
4. Text is analyzed for sentiment (Bangladesh context)
5. Explainable AI output is generated

### Phase-II Workflow:

1. Video is segmented into frames or time intervals
2. Visual features are extracted from each segment
3. Motion and behavior signals are generated
4. Timeline datasets and statistical summaries are produced

---

## 📊 Extracted Features (Phase-II)

* **Posture Openness** – Open vs closed body posture
* **Hand Gesture Activity** – Frequency and intensity of gestures
* **Eye-Contact Approximation** – Camera-facing estimation (approximate)
* **Overall Movement & Pacing** – Stability and variability of movement

All features are **time-based, explainable, and interpretable**.

---

## 📁 Output Deliverables

* Speech transcription (JSON)
* Sentiment classification with explanation
* Movement timeline dataset (CSV / JSON)
* Statistical summaries of motion patterns
* Professional documentation (PDF)

---

## 🔒 Offline Compliance

This project strictly follows offline operation rules:

* ❌ No API calls
* ❌ No cloud-based services
* ❌ No internet dependency
* ❌ No external hosted models
* ✅ All processing is local

---

## 🧪 How to Run the Project

### 1. Environment Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Run Backend

```bash
cd backend
export ALLOW_NET_DOWNLOAD=1
uvicorn main:app --reload
```

### 3. Access API

```
http://127.0.0.1:8000/docs
```

### 4. Test UI

Open:

```text
ui/index.html
```

---

## 📌 Limitations

* Eye-contact estimation is approximate
* Performance depends on video quality
* Camera angle and lighting may affect results
* Partial occlusion can impact feature extraction

All limitations are transparently documented.

---

## 🏁 Conclusion

This project demonstrates a **robust, fully offline AI system** capable of analyzing both verbal and non-verbal aspects of video content.
By combining explainable speech analysis and motion-based visual features, the system provides meaningful insights while maintaining transparency, interpretability, and strict compliance with competition rules.

---

## 👨‍💻 Submission Notes

* The entire project is submitted as a ZIP file
* Screen recording demonstrates system functionality
* All documentation is provided in PDF format
* Google Drive sharing is enabled for evaluation

---

✅ **This README is FINAL SUBMISSION READY**
Just save it as `README.md` in your project root.

---

