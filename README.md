# 🖐️ Hand Gesture Detection using MediaPipe

This project detects and classifies basic *hand gestures* from an image using *MediaPipe* and *OpenCV*. It supports gestures like Thumbs Up, Fist, Two Fingers, and Open Hand.

---

## 📸 Demo

| Input | Output |
|-------|--------|
| ![thumb](examples/thumb_input.jpg) | ![thumb_detected](examples/thumb_detected.jpg) |

---

## 🧠 How it Works

- Uses *MediaPipe Hands* to detect 21 hand landmarks.
- Classifies gestures based on which fingers are up:
  - 👍 *Thumbs Up*
  - ✊ *Fist*
  - ✌️ *Two Fingers*
  - 🖐️ *Open Hand*
- Visualizes the hand landmarks on the image.

---

## 🛠️ Requirements

- Python 3.x
- OpenCV
- MediaPipe

Install the dependencies:

```bash
pip install opencv-python mediapipe
