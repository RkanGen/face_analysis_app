
---

# Face Analysis App

This application allows users to analyze an image of a face to detect keypoints, perform segmentation, and recognize the dominant emotion from the facial expression. It utilizes **MediaPipe** for facial landmarks detection, **OpenCV** for image processing, and **FER (Facial Expression Recognition)** for emotion detection.

## Features

- **Face Keypoints Detection**: Detects and visualizes keypoints on the face using **MediaPipe FaceMesh**.
- **Face Segmentation**: Creates a segmented mask of the face based on facial landmarks.
- **Emotion Recognition**: Recognizes the dominant emotion from the face using the **FER** library.

## Requirements

Before running the application, make sure you have the following installed:

### Python version:
- Python 3.9 or higher

### Install required dependencies:
```bash
pip install -r requirements.txt
```

### `requirements.txt`
```text
opencv-python-headless
mediapipe
fer
gradio
```

## How It Works

1. **Input**: Upload an image (JPG, PNG) containing a face.
2. **Processing**:
   - **Keypoints Detection**: MediaPipe detects 468 facial landmarks.
   - **Segmentation**: OpenCV uses convex hulls of detected landmarks to segment the face.
   - **Emotion Recognition**: FER analyzes the facial expression to determine the dominant emotion.
3. **Output**:
   - **Face Keypoints**: Image showing detected facial keypoints.
   - **Segmented Face**: Image showing a segmented face mask.
   - **Dominant Emotion**: A text label of the detected emotion with confidence score.

## File Structure

```bash
.
├── app.py               # Main application code
├── README.md            # Project documentation
├── requirements.txt     # Dependencies for the project
└── sample_image.png     # Example image for testing
```

### `app.py`
The main application logic which:
- Loads the image, detects keypoints, segments the face, and detects emotions.
- Utilizes the Gradio framework to create a user-friendly interface.

## How to Run the App

1. Clone the repository:
   ```bash
   git clone https://github.com/RkanGen/face-analysis-app.git
   cd face-analysis-app
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   python app.py
   ```

4. Open the app in your browser (Gradio provides a local web interface):
   ```
   http://localhost:7860/
   ```

## Usage

- Simply drag and drop or upload an image containing a face.
- The app will display:
  - **Keypoints**: Small green dots marking the facial keypoints.
  - **Segmented Face**: A mask overlay on the face based on the convex hull of detected landmarks.
  - **Dominant Emotion**: The detected emotion (e.g., Happy, Sad) and the confidence score.

## Example
![face_app](https://github.com/user-attachments/assets/8949b776-3326-40ae-834c-3e80bc5a8312)

![faceapp2](https://github.com/user-attachments/assets/c7e4c8d0-1ba5-43b1-bcb4-2870a2137992)

![show](https://github.com/user-attachments/assets/34733c8d-e105-47e7-a8e2-a18f16cc3b69)

- **Face Keypoints**: Detected keypoints on the image.
- **Segmented Face**: The segmented face overlaid on the original image.
- **Dominant Emotion**: Detected emotion with confidence score.

## Future Enhancements

- Improve segmentation accuracy by applying more sophisticated techniques.
- Add support for video input (real-time face analysis).
- Introduce additional facial analysis like age, gender detection, or more advanced emotion detection.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **MediaPipe** for facial landmarks detection.
- **OpenCV** for image manipulation.
- **FER** for facial emotion recognition.
- **Gradio** for creating a user-friendly web interface.

---
