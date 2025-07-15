# Lemon Ripeness Classifier Django App

## Features
- Upload lemon images and predict ripeness (Ripened/Unripened)
- Uses your trained model from model2.ipynb (lemon_classifier_model.h5)
- Beautiful, responsive UI
- Recent predictions history
- Demo mode if TensorFlow/model is missing

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Copy your trained model (lemon_classifier_model.h5) to this directory.
3. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Start the server:
   ```bash
   python manage.py runserver
   ```
5. Visit http://127.0.0.1:8000/

## How it works
- Upload an image
- The app preprocesses and predicts using your model
- Results and confidence are shown
- If TensorFlow/model is missing, demo mode gives random predictions
