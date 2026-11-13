



import streamlit as st
import tensorflow as tf
import numpy as np

def model_prediction(test_image):
  model= tf.keras.models.load_model('trained_modal.keras')
  image=tf.keras.preprocessing.image.load_img(test_image,target_size=(128,128))
  input_arr=tf.keras.preprocessing.image.img_to_array(image)
  input_arr=np.array([input_arr])     # convert single image to a batch
  prediction= model.predict(input_arr)
  result_index=np.argmax(prediction)
  return result_index

#sidebar
st.sidebar.title('DASHBOARD')
app_mode= st.sidebar.selectbox("Select Page",['Home','About','Disease recognition'])

#home page
if app_mode=='Home':
  st.header('Welcome to the Crop Disease Detection App')
  image_path= "home_page.png"
  st.image(image_path,use_column_width=True )
  st.markdown('''
  This is a web application that uses deep learning to detect crop diseases from images of  your crop field from each corner and center. )
''')

#about page
elif app_mode=='About':
  st.header('About')
  st.markdown('''
  This application is designed to help farmers and agricultural professionals quickly identify crop diseases from images of their fields.
  ''')