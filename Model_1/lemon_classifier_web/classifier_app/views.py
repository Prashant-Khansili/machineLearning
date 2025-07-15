import os
import numpy as np
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from .forms import LemonImageForm
from .models import LemonImage
import tensorflow
# Try to import TensorFlow and load the model
TENSORFLOW_AVAILABLE = False
try:
    import tensorflow as tf
    from tensorflow.keras.preprocessing import image
    from tensorflow.keras.models import load_model
    model_path = os.path.join(settings.BASE_DIR, 'lemon_classifier_model.h5')
    if os.path.exists(model_path):
        model = load_model(model_path)
        TENSORFLOW_AVAILABLE = True
    else:
        print(f"Model file not found at: {model_path}")
except ImportError:
    print("TensorFlow not installed. Running in demo mode.")
except Exception as e:
    print(f"Error loading model: {e}")

def home(request):
    form = LemonImageForm()
    recent_predictions = LemonImage.objects.all().order_by('-uploaded_at')
    return render(request, 'home.html', {'form': form, 'recent_predictions': recent_predictions})

def predict(request):
    if request.method == 'POST':
        form = LemonImageForm(request.POST, request.FILES)
        if form.is_valid():
            lemon_image = form.save(commit=False)
            if TENSORFLOW_AVAILABLE:
                try:
                    img_path = os.path.join(settings.MEDIA_ROOT, lemon_image.image.name)
                    img = image.load_img(img_path, target_size=(64, 64))
                    img_array = image.img_to_array(img)
                    img_array = img_array / 255.0
                    img_array = np.expand_dims(img_array, axis=0)
                    prediction_value = model.predict(img_array)[0][0]
                    prediction = 'Unripened' if prediction_value >= 0.7 else 'Ripened'
                    lemon_image.prediction = prediction
                    lemon_image.confidence = float(prediction_value)
                except Exception as e:
                    print(f"Prediction error: {e}")
                    lemon_image.prediction = "Error during prediction"
                    lemon_image.confidence = 0.0
            else:
                import random
                lemon_image.prediction = "Unripened" if random.random() > 0.5 else "Ripened"
                lemon_image.confidence = random.uniform(0.6, 0.9)
                print("Using demo mode for prediction (TensorFlow not available)")
            lemon_image.save()
            return redirect('result', image_id=lemon_image.id)
    else:
        form = LemonImageForm()
    return render(request, 'home.html', {'form': form})

def result(request, image_id):
    lemon_image = get_object_or_404(LemonImage, id=image_id)
    confidence_percentage = int(lemon_image.confidence * 100)
    return render(request, 'result.html', {
        'lemon_image': lemon_image,
        'confidence_percentage': confidence_percentage,
        'demo_mode': not TENSORFLOW_AVAILABLE
    })
