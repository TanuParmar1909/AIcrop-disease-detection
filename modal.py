
'''import tensorflow as tf
import keras 
url="https://github.com/TanuParmar1909/AIcrop-disease-detection/new/main/trained_modal.keras"
model_path=keras.utils.get_file("trained_modal.keras", url)

reconstructed_model = keras.models.load_model(model_path)
  '''
import keras

# Paste your direct GitHub Release asset URL here
release_url = "https://github.com/TanuParmar1909/AIcrop-disease-detection/releases/download/v1.0.0/trained_model.keras"

# Download and cache the file locally
model_path = keras.utils.get_file(
    fname="trained_model.keras", 
    origin=release_url
)

# Load the model into memory
model = keras.models.load_model(model_path)

# Verify that the model loaded correctly
model.summary()