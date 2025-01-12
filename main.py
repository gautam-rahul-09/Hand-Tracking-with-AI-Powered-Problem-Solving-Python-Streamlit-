import cvzone
import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import google.generativeai as genai
from PIL import Image
import streamlit as st
import time

# # Streamlit UI Setup
st.set_page_config(layout="wide")

# st.image("MathGestures.png")

col1, col2 = st.columns([2, 1])
with col1:
    run = st.checkbox('Run', value=True)
    FRAME_WINDOW = st.image([])

with col2:
    st.title("Answer")
    output_text_area = st.empty()

# AI Model Configuration
genai.configure(api_key="AIzaSyBs0YW9z1z-rXsh0y9e2-o2FLspzqQPzOs")
model = genai.GenerativeModel("gemini-1.5-flash")

# Initialize Webcam
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

if not cap.isOpened():
    st.error("Error: Unable to access the webcam.")
    st.stop()

# Initialize Hand Detector
detector = HandDetector(staticMode=False, maxHands=1, modelComplexity=1, detectionCon=0.5, minTrackCon=0.5)

# Helper Functions
def getHandInfo(img):
    hands, img = detector.findHands(img, draw=True, flipType=True)
    if hands:
        hand = hands[0]
        lmList = hand["lmList"]
        fingers = detector.fingersUp(hand)
        return fingers, lmList
    return None

def draw(info, prev_pos, canvas):
    fingers, lmlist = info
    current_pos = None
    if fingers == [0, 1, 0, 0, 0]:  # Index finger up
        current_pos = lmlist[8][:2]
        if prev_pos is None:
            prev_pos = current_pos
        cv2.line(canvas, tuple(prev_pos), tuple(current_pos), color=(255, 0, 255), thickness=10)
    elif fingers == [1, 1, 1, 1, 1]:  # All fingers up
        canvas.fill(0)
        prev_pos = None
    return current_pos

def sendToAI(model, canvas, fingers):
    if fingers == [0, 1, 1, 1, 1]:  # Thumb down
        pil_image = Image.fromarray(canvas.astype('uint8'))
        # Assuming API supports text and image input
        response = model.generate_content(["Solve the maths problem", pil_image])
        return response.text
    return None

# Main Loop
prev_pos = None
canvas = None
img_combined = None
output_text = None

while run:
    success, img = cap.read()
    if not success:
        st.warning("Error: Unable to read frame from webcam.")
        break

    img = cv2.flip(img, flipCode=1)

    if canvas is None:
        canvas = np.zeros_like(img)

    info = getHandInfo(img)
    if info:
        fingers, lmlist = info
        prev_pos = draw(info, prev_pos, canvas)
        output_text = sendToAI(model, canvas, fingers)
        
        

    img_combined = cv2.addWeighted(img, 0.7, canvas, 0.3, 0)
    FRAME_WINDOW.image(img_combined, channels="BGR")
    
    if output_text:
        output_text_area.subheader(output_text)

    time.sleep(0.03)  # Reduce CPU usage

cap.release()
