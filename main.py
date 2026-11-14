



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

#prediction page
elif (app_mode=='Disease recognition'):
  st.header('Disease Recognition')
  test_image= st.file_uploader("Choose an image...")

  #Predict button
  if (st.button("Predict")):
    with st.spinner('Wait for it...'):
       
      st.write("our Prediction is in progress...")
      result_index=model_prediction(test_image)
    #define class
    class_names=['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy', 'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___healthy']
    st.success('the images is Predicting and it is a{}'.format(class_names[result_index]))
  
  '''if test_image is not None:
    st.image(test_image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    label=model_prediction(test_image)
    if label==0:
      st.success('The crop is healthy.')
    elif label==1:
      st.error('The crop is affected by disease.')
  '''