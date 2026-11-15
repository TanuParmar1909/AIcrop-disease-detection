
'''import tensorflow as tf
import keras 
url="https://github.com/TanuParmar1909/AIcrop-disease-detection/new/main/trained_modal.keras"
model_path=keras.utils.get_file("trained_modal.keras", url)

reconstructed_model = keras.models.load_model(model_path)
  '''
'''import keras

# Paste your direct GitHub Release asset URL here
release_url = "https://github.com/TanuParmar1909/AIcrop-disease-detection/releases/tag/v1.0.0"

# Download and cache the file locally
model_path = keras.utils.get_file(
    fname="Trained keras modal", 
    origin=release_url
)

# Load the model into memory
model = keras.models.load_model(model_path)
'''

import os
import urllib.request
import keras

MODEL_URL = "https://github.com/TanuParmar1909/AIcrop-disease-detection/releases/download/v1.0.0/trained_modal.keras"
LOCAL_PATH = "Trained keras modal"

def load_trained_model():
    # Download the file only if it doesn't already exist locally
    if not os.path.exists(LOCAL_PATH):
        print("Downloading model from GitHub Release...")
        try:
            urllib.request.urlretrieve(MODEL_URL, LOCAL_PATH)
            print("Model downloaded successfully!")
        except Exception as e:
            raise RuntimeError(
                f"Failed to download model. Ensure your repository is Public and the release tag 'v1.0.0' exists. Error: {e}"
            )
    
    # Load and return the Keras model
    return keras.models.load_model(LOCAL_PATH)

# Load your model ready for use
model = load_trained_model()
# Verify that the model loaded correctly
model.summary()