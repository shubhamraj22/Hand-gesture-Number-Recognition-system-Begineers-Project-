# 🖐️ Hand Gesture Number Recognition System

A beginner-friendly Computer Vision and Machine Learning project designed to recognize hand gestures representing numbers using OpenCV and MediaPipe/CNNs.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?logo=opencv)
![License](https://img.shields.io/badge/License-MIT-brightgreen)

---

## 📌 Features

- **Real-Time Detection**: Captures webcam video feed and classifies finger counts/hand signs live.
- **ROI / Hand Landmark Tracking**: Uses skin-color segmentation / contour analysis or MediaPipe landmarks to detect hand shapes accurately.
- **Beginner Friendly**: Simple, modular code structure ideal for students and enthusiasts starting with Computer Vision.
- **Customizable**: Easy to extend for additional gesture controls or more complex sign language digits.

---

## 🛠️ Tech Stack & Requirements

- **Language**: Python 3.8+
- **Key Libraries**:
  - `opencv-python` (Real-time video feed and image processing)
  - `numpy` (Array operations & matrix transformations)
  - `mediapipe` *(optional/recommended for landmark tracking)*
  - `tensorflow` or `scikit-learn` *(if trained model is included)*

---

## 🚀 Quick Start & Installation

### 1. Clone the Repository
```bash
git clone [https://github.com/shubhamraj22/Hand-gesture-Number-Recognition-system-Begineers-Project-.git](https://github.com/shubhamraj22/Hand-gesture-Number-Recognition-system-Begineers-Project-.git)
cd Hand-gesture-Number-Recognition-system-Begineers-Project-
2. Set Up Virtual Environment (Optional but Recommended)
Bash
# On Linux/macOS
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
3. Install Dependencies
Bash
pip install opencv-python numpy mediapipe
4. Run the Recognition System
Bash
python main.py
(Note: Replace main.py with your script's filename if named differently, e.g., gesture_recognition.py)

📸 How It Works
Video Capture: Initializes the default webcam (cv2.VideoCapture(0)).

Preprocessing: Converts frame to HSV / Grayscale, applies Gaussian Blur, and thresholding or MediaPipe landmark extraction.

Contour Analysis / Landmark Estimation: Identifies finger tips and counts raised fingers based on convexity defects or joint positions.

Output: Displays the recognized digit live on the screen overlay.

🎮 Usage Instructions
Ensure your camera is properly connected and functioning.

Maintain good lighting conditions and a clear background for best accuracy.

Press q or Esc on your keyboard while the output window is focused to exit the application.

🤝 Contributing
Contributions are welcome! If you'd like to improve the recognition logic, add custom models, or update the UI:

Fork the Project

Create your Feature Branch (git checkout -b feature/AwesomeGesture)

Commit your Changes (git commit -m 'Add some AwesomeGesture')

Push to the Branch (git checkout origin feature/AwesomeGesture)

Open a Pull Request

📝 License
Distributed under the MIT License. See LICENSE for more information.

👤 Author
Shubham Raj

GitHub: @shubhamraj22