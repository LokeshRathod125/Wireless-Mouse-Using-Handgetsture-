"""
# Wireless Mouse Using Hand Gesture

This project allows you to control your computer mouse using **hand gestures** captured via a webcam.  
It leverages **computer vision** and **gesture recognition** techniques to provide a touchless, intuitive way of interacting with your system.

---

## 🚀 Features

- **Touchless Mouse Control** — Move the cursor using hand movements.
- **Click Actions** — Perform left-click, right-click, and click-and-drag with gestures.
- **Real-Time Detection** — Instant feedback and smooth cursor tracking.
- **Accessible Interaction** — Designed for both convenience and accessibility.

---

## 🛠 Tech Stack

- **Language:** Python  
- **Libraries:**  
  - OpenCV — Computer vision and image processing  
  - MediaPipe — Hand tracking and landmark detection  
  - PyAutoGUI — Mouse control and automation  
  - NumPy — Numerical computations  

---

## 📂 Project Structure

Wireless-Mouse-Using-Handgetsture-/
├── wirelessMouce.py       # Main script to run the gesture-based mouse
├── README.md              # Project documentation
└── requirements.txt       # Python dependencies

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   git clone https://github.com/LokeshRathod125/Wireless-Mouse-Using-Handgetsture-.git
   cd Wireless-Mouse-Using-Handgetsture-

2. **Create a virtual environment** (optional but recommended)
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows

3. **Install dependencies**
   pip install -r requirements.txt

   If `requirements.txt` is not available:
   pip install opencv-python mediapipe pyautogui numpy

4. **Run the program**
   python wirelessMouce.py

---

## 🎯 How It Works

1. **Hand Detection** — The webcam captures real-time video frames.
2. **Landmark Recognition** — MediaPipe identifies specific points on your hand.
3. **Gesture Mapping** — Certain gestures are mapped to mouse actions:
   - Index finger: Cursor movement
   - Pinch gesture: Left-click
   - Two-finger pinch: Right-click
4. **Mouse Control** — PyAutoGUI executes these actions on your system.

---

## 📸 Example Gestures

| Gesture            | Action Performed |
|--------------------|------------------|
| Index finger up    | Move cursor      |
| Pinch              | Left click       |
| Two-finger pinch   | Right click      |
| Pinch & drag       | Drag and drop    |

---

## 💡 Usage Tips

- Use in well-lit environments for better hand detection.
- Ensure the background is not too cluttered for accurate tracking.
- Keep your hand within the camera frame at all times.
- Exit the program by pressing `q` in the OpenCV window.

---

## 📌 Future Enhancements

- Add scroll gesture support.
- Customize sensitivity and cursor speed.
- Support multiple gesture profiles for different use cases.

---

## 👤 Author

Lokesh Rathod  
🎓 AI & Data Science Engineering Student, R.T.M.N.U  
⚡ Skills: Data Science, Machine Learning, Embedded Systems, Python, Problem Solving, Communication  
🌐 Portfolio: LokeshRathod125.github.io  
💼 GitHub: LokeshRathod125  
📧 Email: lokeshrathod123213@gmail.com

---

📜 **License**: MIT License
"""

# =========================
# Your actual Python code starts below
# =========================
