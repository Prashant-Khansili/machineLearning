import numpy as np
import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model

def train_and_save_model():
    """Train the CNN model and save it for Django app"""
    
    # Check if model already exists
    if os.path.exists('lemon_classifier_model.h5'):
        print("✅ Model already exists. Loading...")
        return load_model('lemon_classifier_model.h5')
    
    print("🔄 Training new model...")
    
    # Data generators
    training_generator = ImageDataGenerator(
        rescale=1/255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True
    )
    
    training_set = training_generator.flow_from_directory(
        'training_data',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary'
    )
    
    test_generator = ImageDataGenerator(rescale=1./255)
    
    test_set = test_generator.flow_from_directory(
        'test_data',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary'
    )
    
    # Build model
    cnn = tf.keras.models.Sequential()
    
    # 1st Convolutional layer
    cnn.add(tf.keras.layers.Conv2D(
        filters=32,
        kernel_size=3,
        activation='relu',
        input_shape=[64, 64, 3]
    ))
    cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))
    
    # 2nd Convolutional layer
    cnn.add(tf.keras.layers.Conv2D(filters=32, kernel_size=3, activation='relu'))
    cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))
    
    # Flatten and Dense layers
    cnn.add(tf.keras.layers.Flatten())
    cnn.add(tf.keras.layers.Dropout(0.4))
    cnn.add(tf.keras.layers.Dense(units=128, activation='relu'))
    cnn.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))
    
    # Compile
    cnn.compile(
        optimizer='adam',
        loss='binary_crossentropy',
        metrics=['accuracy']
    )
    
    # Train
    print("Training model...")
    cnn.fit(x=training_set, validation_data=test_set, epochs=25)
    
    # Save
    cnn.save('lemon_classifier_model.h5')
    print("✅ Model trained and saved successfully!")
    
    return cnn

if __name__ == "__main__":
    model = train_and_save_model()
