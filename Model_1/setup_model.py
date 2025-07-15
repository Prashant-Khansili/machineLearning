"""
Script to set up the trained model for Django app
"""
import os
import shutil

def setup_model():
    """Copy or create the model file for Django app"""
    
    # Check if model already exists in root directory
    if os.path.exists('lemon_classifier_model.h5'):
        print("✅ Model file already exists!")
        return
    
    # If you have a trained model elsewhere, you can copy it here
    # For now, we'll create a placeholder that can be replaced with your trained model
    
    print("📝 Please copy your trained model file to: lemon_classifier_model.h5")
    print("   The Django app will work once the model file is in place.")
    
    # Create a dummy model structure (this will be replaced with actual trained model)
    import tensorflow as tf
    
    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(32, 3, activation='relu', input_shape=[64, 64, 3]),
        tf.keras.layers.MaxPool2D(pool_size=2, strides=2),
        tf.keras.layers.Conv2D(32, 3, activation='relu'),
        tf.keras.layers.MaxPool2D(pool_size=2, strides=2),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dropout(0.4),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    model.save('lemon_classifier_model.h5')
    print("📦 Placeholder model created. Replace with your trained model for accurate predictions.")

if __name__ == "__main__":
    setup_model()
