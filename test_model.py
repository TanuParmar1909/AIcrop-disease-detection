import os
import sys

# Windows DLL directories for TensorFlow
if sys.platform == "win32":
    venv_dir = os.path.dirname(os.path.dirname(sys.executable))
    if os.path.exists(venv_dir):
        try:
            os.add_dll_directory(venv_dir)
            scripts_dir = os.path.join(venv_dir, "Scripts")
            if os.path.exists(scripts_dir):
                os.add_dll_directory(scripts_dir)
        except Exception as e:
            print("DLL directory note:", e)

import shutil
import numpy as np

print("Testing Model Loading...")
base_dir = os.path.dirname(os.path.abspath(__file__))
raw_model = os.path.join(base_dir, "Trained keras modal")
keras_model = os.path.join(base_dir, "trained_model.keras")

if os.path.exists(raw_model) and not os.path.exists(keras_model):
    print(f"Creating copy with .keras extension: {keras_model}")
    shutil.copyfile(raw_model, keras_model)

import tensorflow as tf
print("TensorFlow Version:", tf.__version__)

target_path = keras_model if os.path.exists(keras_model) else raw_model
print("Loading model from:", target_path)

try:
    model = tf.keras.models.load_model(target_path, compile=False)
    print("Model loaded successfully with compile=False!")
except Exception as e:
    print("Failed with compile=False, trying without compile=False:", e)
    model = tf.keras.models.load_model(target_path)
    print("Model loaded successfully!")

print("Model Input Shape:", model.input_shape)
print("Model Output Shape:", model.output_shape)
print("Layers count:", len(model.layers))

has_rescaling = any("rescaling" in layer.name.lower() or "rescale" in type(layer).__name__.lower() for layer in model.layers)
print("Has Rescaling Layer:", has_rescaling)

# Test dummy prediction
dummy_input = np.zeros((1, 128, 128, 3), dtype=np.float32)
pred = model.predict(dummy_input, verbose=0)
print("Dummy prediction successful! Output shape:", pred.shape)
print("Argmax index:", np.argmax(pred))
print("Sum of probs:", np.sum(pred))
print("ALL TESTS PASSED PERFECTLY!")
