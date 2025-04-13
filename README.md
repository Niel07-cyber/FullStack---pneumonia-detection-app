📄 FINAL FULL README.md
markdown
Copy
Edit
# 🩺 Pneumonia Detection Full Stack App (FastAPI + Next.js)

This project is a complete full-stack application for detecting pneumonia from chest X-ray images using deep learning.

- **Frontend**: Next.js (React)
- **Backend**: FastAPI (Python)
- **AI Model**: TensorFlow CNN (trained manually)
- **Deployment**: Local (localhost)


![Frontend UI](https://github.com/Niel07-cyber/FullStack---pneumonia-detection-app/blob/main/images/Screenshot%202025-04-13%20233716.png)
---

## 🛠 Project Structure

projetai/ ├── demo-backend/ # FastAPI Backend │ ├── main.py │ ├── pneumonia_detector.h5 # Model file (must be created manually) │ ├── radiograph_ai.ipynb # Notebook to train the model │ └── venv/ (ignored)
├── demo-frontend/ # Next.js Frontend │ ├── src/ │ ├── public/ │ └── package.json ├── README.md └── .gitignore


---

## 🚀 How to Run Locally

### 1. Clone the Repository

```
git clone https://github.com/YOUR_USERNAME/FullStack---pneumonia-detection-app.git
cd FullStack---pneumonia-detection-app
```
### 2. Generate the Model (pneumonia_detector.h5)
```
⚠️ The trained model file pneumonia_detector.h5 was not uploaded because of GitHub's 100MB file size limit.

You must create it yourself:

Open the Jupyter Notebook located at:

demo-backend/radiograph_ai.ipynb
Run the notebook cells.

After training, it will automatically create a file:


demo-backend/pneumonia_detector.h5
✅ Now you are ready to run the backend.
```
### 3. Setup and Run Backend (FastAPI)
```
cd demo-backend
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install fastapi uvicorn tensorflow pillow
uvicorn main:app --reload --port 8000
The backend will be live at http://localhost:8000

Test API using Swagger UI at http://localhost:8000/docs
```
### 4. Setup and Run Frontend (Next.js)
```
cd ../demo-frontend
npm install
npm run dev
The frontend will be live at http://localhost:3000
```

### 📸 Features
Upload Chest X-ray images (.jpg/.jpeg/.png)

Get prediction: Pneumonia or Normal

See model confidence score for each prediction

Clean and responsive user interface


### 🧠 Tech Stack
Layer	Technologies
Backend	FastAPI, TensorFlow, Pillow
Frontend	Next.js 15 (React 18)
Machine Learning	Convolutional Neural Network (CNN)
Language	Python, JavaScript


### ⚡ Additional Notes
Make sure the backend server is running before using the frontend.

The frontend expects the backend API to be available at http://localhost:8000.

Always upload grayscale chest X-ray images for best results.

You can retrain the model anytime by running the provided Jupyter notebook.

### 🏁 Final Summary
Item	Status
Frontend	✅
Backend	✅
AI Model Training	✅
Model Generation Instructions	✅
Full Stack Deployment (Localhost)	✅


### 🙏 Acknowledgments
Special thanks to all open-source contributors in the fields of Machine Learning, FastAPI, and Next.js who make building projects like this possible.



---
