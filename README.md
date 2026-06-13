# AI-DOCTOR: Advanced Telemedicine & Biometric Diagnostic Terminal

AI-DOCTOR is a next-generation telemedicine application that combines real-time client-side biometric computer vision with state-of-the-art Large Language Models (LLMs) to perform clinical triaging. Utilizing **MediaPipe Face Mesh** for objective physical inspection and the upgraded **Google GenAI SDK (Gemini 1.5 Flash)**, the application generates professional, MD-level medical reports mapped directly to the clinical **SOAP format**.

---

## 🚀 Key Features

* **Real-time Biometric Tracking:** Uses MediaPipe client-side ML to scan facial landmarks and dynamically evaluate oral cavity status (detecting open/closed mouth orientation).
* **Vital Sign Simulation:** Simulates continuous heart rate telemetry mimicking integrated remote patient monitoring devices.
* **Automated SOAP Note Generation:** Generates comprehensive medical documentation structure including *Subjective, Objective, Assessment, and Plan*.
* **Differential Diagnosis (DDx):** Ranks the top 3 clinical possibilities based on cross-referencing user symptoms against objective visual/numerical data.
* **Clinical Safety Triaging:** Dynamically calculates an urgency score (1-5), flags critical "Red Flags" requiring emergency room dispatch, and prepares a handoff summary for receiving physicians.
* **Cyberpunk Medical Terminal UI:** Fully responsive, dark-mode medical command interface built with native HTML5, CSS3 Variables, and modern JavaScript.

---

## 🛠️ Architecture & Tech Stack

### Backend
* **Python / Flask:** Lightweight WSGI web application server configured with multi-threaded routing to handle concurrent sessions natively.
* **Google GenAI SDK:** Integrated with `gemini-1.5-flash` for high-speed, medically contextualized reasoning prompts.
* **MediaPipe & OpenCV:** Integrated on the backend for future server-side frame-by-frame computational analysis.

### Frontend
* **MediaPipe FaceMesh JavaScript API:** Client-side structural tracking of facial topologies to optimize performance and lower server bandwidth.
* **Vanilla JS & Fetch API:** Asynchronous pipeline passing patient metrics directly to the Flask diagnostic endpoint without page reloads.

---

## 📋 Prerequisites

* Ensure your environment meets the following requirements before installation: *
* Python 3.9 or higher
* Modern web browser with camera permissions enabled (Chrome, Firefox, Edge)
* A valid Google Gemini API Key

---

## 💻 Installation & Setup

1. **Clone the Repository**

   ```bash
   git clone [https://github.com/meetpotdar777/AI-DOCTOR.git](https://github.com/meetpotdar777/AI-DOCTOR.git)
   cd AI-DOCTOR
   ```
2. **Set Up a Virtual Environment**
### ◘ Windows

  ```bash
  python -m venv venv
  .\venv\Scripts\activate
  ```
### ◘ macOS/Linux

  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
3. **Install Dependencies**

  ```bash
  pip install flask opencv-python numpy google-genai mediapipe
  ```

4. **Project Structure Configuration**

  * Ensure your local project directory structure matches the layout below:*
   
```bash
AI-DOCTOR/
├── app.py
├── templates/
│   └── index.html
└── README.md
```

5. **Configure Environment Security**
   
* ⚠️ **CRITICAL SECURITY NOTE:** Never hardcode your API key inside app.py. It is highly recommended to update your script to read from environment variables (os.environ.get()).

*To set your API key in your terminal session:*

```bash
# Windows (CMD)
set GEMINI_API_KEY="your_api_key_here"

# Windows (PowerShell)
$env:GEMINI_API_KEY="your_api_key_here"

# macOS/Linux
export GEMINI_API_KEY="your_api_key_here"
```

6. **Run the Application**

```bash
python app.py
```
*Open your browser and navigate to http://127.0.0.1:5000/.*

---

## 🩺 Diagnostic Workflow

* **Biometric Authorization:** Upon load, authorize the browser to access your camera. The terminal status will change to SYSTEM ONLINE.
* **Physical Scan:** The scanner tracks your face structure. Open your mouth wide to watch the tracking state switch from Closed to WIDE OPEN (Scanned) in real-time.
* **Symptom Logging:** Input patient presentation details (e.g., "Throat pain, fever, and coughing for two days").
* **Clinical Processing:** Click Generate Clinical Analysis. The interface compiles your simulated heart rate, visual oral examination metadata, and text parameters before parsing them through Gemini.
* **Report Presentation:** A clean, printable clinical medical profile populates on-screen.

---

## ⚖️ Disclaimer

This application is an AI-assisted experimental triage prototype intended strictly for educational and demonstration purposes. It does not provide real medical advice, diagnosis, or treatment. Always consult a certified healthcare professional for medical concerns.

---
