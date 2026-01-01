import os
import cv2
import numpy as np
from flask import Flask, render_template, request, jsonify
from google import genai # Using the new upgraded SDK
import mediapipe as mp

app = Flask(__name__)

# --- CONFIGURATION ---
# Replace with your actual key - keep it secure!
API_KEY = "AIzaSyBJqWczOJEoLKEtfMqd1YxQlXKSHRsYzZs"
client = genai.Client(api_key=API_KEY)

# Initialize MediaPipe for Advanced Physical Exam tracking
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/diagnose', methods=['POST'])
def diagnose():
    try:
        data = request.json
        symptoms = data.get('problem', 'No symptoms provided')
        vitals = data.get('vitals', {})
        
        # Clinical reasoning prompt designed for MD-level triage
        prompt = f"""
        Act as a Senior Medical Consultant. Analyze the following telemedicine data:
        
        [PATIENT INPUT]
        Symptoms: {symptoms}
        
        [OBJECTIVE DATA FROM AI SCANNER]
        - Estimated Heart Rate: {vitals.get('hr')} BPM
        - Oral Cavity Status: {vitals.get('mouth')}
        - Detected Inflammation: {vitals.get('inflammation', 'Pending physical check')}
        
        [REQUIREMENTS]
        1. Format as a professional SOAP Note (Subjective, Objective, Assessment, Plan).
        2. Differential Diagnosis (DDx): Provide 3 possibilities ranked by likelihood.
        3. URGENCY SCORE: Assign a score (1-5) where 5 is Emergency.
        4. RED FLAGS: List critical symptoms requiring an immediate ER visit.
        5. DOCTOR SUMMARY: Provide a 2-sentence summary for the receiving physician.
        """

        # Generate content using Gemini 1.5 Flash
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )
        
        return jsonify({
            "report": response.text,
            "urgency": "High" if "Emergency" in response.text else "Standard"
        })

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Failed to connect to Medical AI Engine"}), 500

if __name__ == '__main__':
    # Using threaded=True allows the server to handle multiple patients at once
    app.run(debug=True, port=5000, threaded=True)