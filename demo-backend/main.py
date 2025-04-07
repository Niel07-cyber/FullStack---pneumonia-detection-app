from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import tensorflow as tf
from PIL import Image
import numpy as np
import io



app = FastAPI()

# Load your model
model = tf.keras.models.load_model('pneumonia_detector.h5')

# Print model input shape to debug
print("✅ Model input shape is:", model.input_shape)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    
    # Open image and process
    image = Image.open(io.BytesIO(contents)).convert("L")  # Convert to grayscale
    image = image.resize((224, 224))  # 🛠️ Resize to 224x224 as model expects
    
    img_array = np.array(image) / 255.0  # Normalize to 0-1
    img_array = img_array.reshape((1, 224, 224, 1))  # 🛠️ Correct shape (batch, height, width, channels)
    
    # Make prediction
    prediction = model.predict(img_array)

    # Interpret result
    result = "Pneumonia" if prediction[0][0] < 0.5 else "Normal"
    
    return {"prediction": result}


