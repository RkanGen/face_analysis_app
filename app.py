import cv2
import gradio as gr
import numpy as np
import mediapipe as mp
from fer import FER

# Initialize MediaPipe FaceMesh and FER Emotion Detector
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1, min_detection_confidence=0.5)
emotion_detector = FER(mtcnn=True)

# Function to create a transparent face mask based on landmarks using OpenCV utilities
def create_enhanced_mask(image, landmarks):
    mask = np.zeros(image.shape[:2], dtype=np.uint8)
    face_points = np.array([[int(p.x * image.shape[1]), int(p.y * image.shape[0])] for p in landmarks], np.int32)
    
    # Use convex hull to find the face contours and fill the mask
    hull = cv2.convexHull(face_points)
    cv2.fillConvexPoly(mask, hull, 255)
    
    # Create a transparent overlay by combining the mask and the original image
    overlay = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    alpha = 0.6  # Transparency level
    segmented_face = cv2.addWeighted(image, 1 - alpha, overlay, alpha, 0)
    
    return segmented_face

# Function to process the image
def process_image(image):
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(image_rgb)

    if results.multi_face_landmarks:
        landmarks = results.multi_face_landmarks[0].landmark
        
        # Create a refined face mask using OpenCV
        segmented_face = create_enhanced_mask(image, landmarks)
        
        # Drawing smaller keypoints using MediaPipe landmarks
        keypoints = np.array([[int(p.x * image.shape[1]), int(p.y * image.shape[0])] for p in landmarks])
        for keypoint in keypoints:
            cv2.circle(image, tuple(keypoint), 1, (0, 255, 0), -1)  # Smaller keypoints
        
        # Emotion recognition
        emotions = emotion_detector.detect_emotions(image_rgb)
        dominant_emotion = max(emotions[0]['emotions'].items(), key=lambda x: x[1]) if emotions else None
        
        # Convert the segmented face and keypoints images back to RGB for display
        segmented_face_rgb = cv2.cvtColor(segmented_face, cv2.COLOR_BGR2RGB)
        keypoint_image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        return (segmented_face_rgb, keypoint_image_rgb, dominant_emotion[0].capitalize(), dominant_emotion[1])

    return None, None, "No face detected", None

# Function for Gradio interface
def analyze_image(uploaded_file):
    # Read the image from filepath
    image = cv2.imread(uploaded_file)

    # Process the image to get segmented face, keypoints, and emotion
    segmented_face, keypoint_image, emotion, confidence = process_image(image)

    # If no face is detected, return error message
    if segmented_face is None:
        return None, None, "No face detected", None

    return keypoint_image, segmented_face, f"{emotion}: {confidence:.2f}"

# Create Gradio interface with swapped layout
iface = gr.Interface(
    fn=analyze_image, 
    inputs=gr.Image(type="filepath"),  # Use 'filepath' for image input
    outputs=[
        gr.Image(type="numpy", label="Face Keypoints"), 
        gr.Image(type="numpy", label="Segmented Face"),  # Segmentation is now below keypoints
        gr.Textbox(label="Dominant Emotion")
    ],
    title="Face Analysis App",
    description="Upload an image to analyze the face for keypoints and dominant emotion."
)

# Launch the Gradio app
iface.launch()
