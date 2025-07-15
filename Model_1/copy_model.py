"""
Copy your trained model to the Django app
Run this if you have a trained model from your notebooks
"""

import shutil
import os

def copy_trained_model():
    """Copy trained model if it exists"""
    
    # Check if there's already a model in the current directory
    model_files = [
        'lemon_classifier_model.h5',
        'model.h5',
        'trained_model.h5'
    ]
    
    for model_file in model_files:
        if os.path.exists(model_file) and model_file != 'lemon_classifier_model.h5':
            print(f"Found model: {model_file}")
            shutil.copy2(model_file, 'lemon_classifier_model.h5')
            print("✅ Model copied successfully!")
            return True
    
    print("ℹ️  No pre-trained model found.")
    print("📝 To use your trained model:")
    print("   1. Train your model using one of the notebook files")
    print("   2. Save it as 'lemon_classifier_model.h5' in this directory")
    print("   3. Or run this script after training")
    
    return False

if __name__ == "__main__":
    copy_trained_model()
