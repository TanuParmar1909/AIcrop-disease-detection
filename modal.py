
import tensorflow as tf
import keras 
url="https://github.com/TanuParmar1909/AIcrop-disease-detection/new/main/trained_modal.keras"
model_path=keras.utils.get_file("trained_modal.keras", url)

reconstructed_model = keras.models.load_model(model_path)
  