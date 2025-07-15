# 🍋 Lemon Ripeness Classifier

A comprehensive machine learning web application that classifies lemon images as **Ripe** or **Unripe** using a Convolutional Neural Network (CNN) built with TensorFlow and Django.

## 📋 Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [Running the Application](#running-the-application)
- [Training Your Own Model](#training-your-own-model)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Model Information](#model-information)
- [Contributing](#contributing)


## ✨ Features

- **🤖 AI-Powered Classification**: Uses a trained CNN model to classify lemon ripeness
- **🖼️ Image Upload**: Drag & drop or browse to upload lemon images
- **📊 Confidence Scoring**: Shows prediction confidence percentage
- **📱 Responsive Design**: Modern, mobile-friendly Bootstrap interface
- **📈 Complete Prediction History**: View all previous predictions with timestamps
- **⚡ Real-time Results**: Instant predictions with visual feedback
- **🔄 Demo Mode**: Fallback mode when TensorFlow is not available
- **👨‍💼 Admin Panel**: Django admin interface to manage predictions
- **🌐 REST API**: JSON API endpoints for programmatic access

## 📁 Project Structure

```
Model_1/
├── lemon_classifier_web/          # Django web application
│   ├── classifier_app/            # Main Django app
│   │   ├── models.py              # Database models (LemonImage)
│   │   ├── views.py               # View controllers
│   │   ├── forms.py               # Form definitions
│   │   ├── urls.py                # URL routing
│   │   └── templates/             # HTML templates
│   ├── media/uploads/             # Uploaded images storage
│   ├── static/css/                # CSS files
│   ├── templates/                 # Base templates (home.html, result.html)
│   ├── manage.py                  # Django management script
│   └── requirements.txt           # Python dependencies
├── predictor/                     # Additional Django app
│   ├── models.py                  # Additional models
│   ├── views.py                   # API views
│   ├── ml_utils.py                # Machine learning utilities
│   └── templates/                 # Predictor templates
├── training_data/                 # Training dataset
│   ├── ripe_lemons/              # Ripe lemon images
│   └── unripe_lemons/            # Unripe lemon images
├── test_data/                     # Test dataset
│   ├── ripe_lemons/              # Test ripe lemon images
│   └── unripe_lemons/            # Test unripe lemon images
├── Masked/                        # Masked dataset (alternative)
├── predictions/                   # Sample prediction images
├── lemon_classifier_model.h5      # Trained TensorFlow model
├── train_model.py                 # Model training script
├── copy_model.py                  # Model copying utility
├── setup_model.py                 # Model setup script
├── manage.py                     # Django management (root level)
├── model.ipynb                   # Jupyter notebook for training
├── model2.ipynb                  # Enhanced training notebook
├── confusion_matrix.ipynb        # Model evaluation notebook
└── README.md                     # This file
```

## 🔧 Prerequisites

- **Python 3.8+**
- **pip** (Python package manager)
- **Git** (for cloning the repository)

## 🚀 Installation & Setup

### 1. Clone or Download the Project

```bash
# If using Git
git clone https://github.com/Prashant-Khansili/machineLearning.git
cd Model_1

# Or download and extract the ZIP file
```

### 2. Create a Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
# Navigate to the Django project directory
cd lemon_classifier_web

# Install required packages
pip install -r requirements.txt
```

**Required packages:**
- `django` - Web framework
- `pillow` - Image processing
- `tensorflow` - Machine learning model

### 4. Database Setup

```bash
# From the lemon_classifier_web directory
python manage.py makemigrations
python manage.py migrate

# Or from the root directory
python manage.py makemigrations
python manage.py migrate
```

### 5. Model Setup

**Option A: Use Existing Model**
- Ensure `lemon_classifier_model.h5` is in the root directory

**Option B: Copy Model from Training**
```bash
python copy_model.py
```

**Option C: Train New Model**
```bash
python train_model.py
```

### 6. Create Media Directory

```bash
# Create media directory for uploaded images (if not exists)
mkdir media
mkdir media\uploads
```

### 7. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

## ▶️ Running the Application

```

 Manual Django Server

```bash
# Navigate to Django project directory
cd lemon_classifier_web

# Start the development server
python manage.py runserver

# Or specify a custom port
python manage.py runserver 8080
```



The application will be available at: **http://127.0.0.1:8000** or **http://localhost:8000**

## 🎯 Training Your Own Model

### 1. Prepare Your Dataset

Organize your images in the following structure:

```
training_data/
├── ripe_lemons/       # Put ripe lemon images here
└── unripe_lemons/     # Put unripe lemon images here

test_data/
├── ripe_lemons/       # Put test ripe lemon images here
└── unripe_lemons/     # Put test unripe lemon images here
```

### 2. Train the Model

```bash
# From the root directory
python train_model.py
```

**Or use Jupyter Notebooks:**
- `model.ipynb` - Basic CNN training
- `model2.ipynb` - Enhanced training with model saving
- `confusion_matrix.ipynb` - Model evaluation and metrics

### 3. Model Architecture

The CNN model includes:
- **Input Layer**: 64x64x3 (RGB images)
- **Convolutional Layers**: Feature extraction with 32 filters
- **MaxPooling Layers**: Dimensionality reduction
- **Dropout Layer**: Prevents overfitting (0.4 rate)
- **Dense Layers**: Classification (128 neurons)
- **Output**: Binary classification (Ripe/Unripe)

## 🖥️ Usage

### Web Interface

1. **Home Page**: Upload lemon images using drag & drop or file browser
2. **Prediction**: Click "Check Ripeness" to classify the image
3. **Results**: View prediction results with confidence score
4. **History**: See all previous predictions in the scrollable sidebar
5. **Admin Panel**: Access at `/admin/` to manage predictions

### Image Requirements

- **Formats**: JPEG, JPG, PNG
- **Recommended Size**: Any size (automatically resized to 64x64)
- **Content**: Clear images of lemons

## 🌐 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Home page with upload form and prediction history |
| `/predict/` | POST | Upload image and get prediction |
| `/result/<id>/` | GET | View specific prediction result |
| `/admin/` | GET | Django admin panel |

### API Usage Example

```python
import requests

# Upload image for prediction
files = {'image': open('lemon.jpg', 'rb')}
response = requests.post('http://localhost:8000/predict/', files=files)

# The response will redirect to the result page
# You can parse the redirect URL to get the prediction ID
```

## 🧠 Model Information

- **Architecture**: Convolutional Neural Network (CNN)
- **Input Size**: 64x64 pixels, RGB
- **Classes**: Binary (Ripe/Unripe)
- **Framework**: TensorFlow/Keras
- **Training**: Image augmentation with rotation, zoom, and flip

### Classification Logic

- **Ripe**: Prediction score < 0.7
- **Unripe**: Prediction score ≥ 0.7

### Prediction Confidence

- **High Confidence**: >80% - Very reliable prediction
- **Medium Confidence**: 60-80% - Good prediction
- **Low Confidence**: <60% - Less reliable, consider retaking image

## 🔧 Troubleshooting

### Common Issues

**1. TensorFlow Installation Issues**
```bash
# If TensorFlow fails to install
pip install tensorflow --upgrade
# Or for CPU-only version
pip install tensorflow-cpu
```

**2. "No module named 'PIL'"**
```bash
pip install Pillow
```

**3. Database Errors**
```bash
# Reset database
python manage.py migrate --run-syncdb
```

**4. Media Files Not Loading**
- Ensure `media/uploads/` directory exists
- Check Django settings for `MEDIA_ROOT` and `MEDIA_URL`

**5. Model Not Found**
- Ensure `lemon_classifier_model.h5` is in the root directory
- Run `python train_model.py` to create a new model

**6. Static Files Not Loading**
```bash
python manage.py collectstatic
```



## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## 📄 License

This project is open source and available under the MIT License.

