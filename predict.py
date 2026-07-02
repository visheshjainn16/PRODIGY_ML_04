import cv2
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model

# Load model
model = load_model("models/best_hand_gesture_model.keras")
# Class names
class_names = [
    "Palm",
    "L",
    "Fist",
    "Fist Moved",
    "Thumb",
    "Index",
    "OK",
    "Palm Moved",
    "C",
    "Down"
]

# Image path (change this to any image you want to test)
image_path = input("Enter image path: ")
# Read image
image = cv2.imread(image_path)

if image is None:
    print("Image not found!")
    exit()

# Preprocess
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_resized = cv2.resize(image_rgb, (64, 64))
image_normalized = image_resized / 255.0
image_input = np.expand_dims(image_normalized, axis=0)

# Predict
prediction = model.predict(image_input)
predicted_class = np.argmax(prediction)
confidence = np.max(prediction)

# Print result
print("Predicted Gesture:", class_names[predicted_class])
print(f"Confidence: {confidence * 100:.2f}%")

# Show image
plt.imshow(image_rgb)
plt.title(
    f"Prediction: {class_names[predicted_class]}\nConfidence: {confidence * 100:.2f}%"
)
plt.axis("off")
plt.show()