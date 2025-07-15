# 🍋 Lemon Ripeness Classifier Django App

A Django web application that uses a Convolutional Neural Network (CNN) to classify whether a lemon is ripe or unripe based on uploaded images.

## Features

- **Web Interface**: Beautiful, responsive web interface for image upload
- **AI Prediction**: CNN model analyzes lemon images for ripeness classification
- **REST API**: JSON API endpoint for programmatic access
- **Admin Panel**: Django admin interface to manage predictions
- **Real-time Results**: Instant prediction results with confidence scores

## Setup Instructions

### 1. Prerequisites
- Python 3.8+
- Virtual environment (already set up)

### 2. Install Dependencies
```bash
# Dependencies are already installed in the virtual environment
```

### 3. Database Setup
```bash
# Run migrations (already done)
python manage.py makemigrations
python manage.py migrate
```

### 4. Model Setup
**Important**: Copy your trained model to the project directory:
- Your trained model should be saved as `lemon_classifier_model.h5`
- If you trained the model using the notebooks, run:
  ```bash
  python copy_model.py
  ```

### 5. Run the Server
```bash
python manage.py runserver
```

## Usage

### Web Interface
1. Open your browser and go to `http://localhost:8000`
2. Upload a lemon image using the form
3. View the prediction results with confidence score

### API Usage
Send POST requests to `http://localhost:8000/api/predict/` with an image file:

```python
import requests

files = {'image': open('lemon.jpg', 'rb')}
response = requests.post('http://localhost:8000/api/predict/', files=files)
result = response.json()
print(f"Prediction: {result['prediction']} ({result['confidence']:.1f}% confidence)")
```

### API Documentation
Visit `http://localhost:8000/api/docs/` for interactive API documentation.

## Project Structure

```
Model_1/
├── lemon_classifier/          # Django project settings
├── predictor/                 # Main Django app
│   ├── models.py             # Database models
│   ├── views.py              # Web views and API endpoints
│   ├── forms.py              # Django forms
│   ├── ml_utils.py           # Machine learning utilities
│   └── templates/            # HTML templates
├── media/                    # Uploaded images storage
├── training_data/            # Training dataset
├── test_data/                # Test dataset
├── manage.py                 # Django management script
└── lemon_classifier_model.h5 # Trained CNN model
```

## Model Architecture

The CNN model consists of:
- 2 Convolutional layers (32 filters each)
- 2 MaxPooling layers
- Dropout layer (0.4)
- Dense layer (128 neurons)
- Output layer (sigmoid activation for binary classification)

Input image size: 64x64 RGB

## Classification Logic

- **Ripe**: Prediction score < 0.7
- **Unripe**: Prediction score ≥ 0.7

## Admin Panel

Create a superuser to access the admin panel:
```bash
python manage.py createsuperuser
```

Then visit `http://localhost:8000/admin/` to manage predictions.

## Endpoints

- `/` - Home page with upload form
- `/result/<id>/` - View prediction results
- `/api/predict/` - POST endpoint for predictions
- `/api/docs/` - API documentation
- `/admin/` - Django admin panel

## Notes

- Images are automatically resized to 64x64 pixels for model input
- Uploaded images are stored in the `media/lemon_images/` directory
- The app includes error handling for invalid images and model issues
- Bootstrap 5 is used for responsive UI styling

## Model Training

If you need to retrain the model, use the provided notebooks:
- `model.ipynb` - Basic CNN training
- `model2.ipynb` - Enhanced training with model saving

Save the trained model as `lemon_classifier_model.h5` in the project root.
