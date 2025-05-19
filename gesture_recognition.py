import cv2
import mediapipe as mp

# Initialize MediaPipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(static_image_mode=True, max_num_hands=1)

# Load uploaded gesture image
image_path = "thumb.jpeg"  # Replace with your image filename
image = cv2.imread(image_path)

if image is None:
    print("❌ Image not found!")
    exit()

# Convert to RGB
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
result = hands.process(rgb_image)

gesture = "Unknown"

if result.multi_hand_landmarks:
    hand_landmarks = result.multi_hand_landmarks[0]

    # Get landmark coordinates
    landmarks = hand_landmarks.landmark

    fingers_up = 0

    # Thumb: Check if tip is to the right of IP (for right hand)
    if landmarks[mp_hands.HandLandmark.THUMB_TIP].x > landmarks[mp_hands.HandLandmark.THUMB_IP].x:
        fingers_up += 1

    # Other 4 fingers
    tips = [mp_hands.HandLandmark.INDEX_FINGER_TIP,
            mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
            mp_hands.HandLandmark.RING_FINGER_TIP,
            mp_hands.HandLandmark.PINKY_TIP]
    
    pips = [mp_hands.HandLandmark.INDEX_FINGER_PIP,
            mp_hands.HandLandmark.MIDDLE_FINGER_PIP,
            mp_hands.HandLandmark.RING_FINGER_PIP,
            mp_hands.HandLandmark.PINKY_PIP]

    for tip, pip in zip(tips, pips):
        if landmarks[tip].y < landmarks[pip].y:
            fingers_up += 1

    # Gesture classification
    if fingers_up == 0:
        gesture = "Fist"
    elif fingers_up == 1:
        gesture = "Thumbs Up"
    elif fingers_up == 2:
        gesture = "Two Fingers Up"
    elif fingers_up == 5:
        gesture = "Open Hand"
    else:
        gesture = f"{fingers_up} Fingers Up"

    # Draw hand landmarks
    mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
else:
    gesture = "No hand detected"

# Show result
cv2.putText(image, gesture, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
cv2.imshow("Detected Gesture", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
