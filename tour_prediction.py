
# Tourist or Non-tourist post classification

import tensorflow as tf
from tensorflow import keras
model_path = './models/Model_VGG16_C[TourNotour]_E100B64.h5' 
model = keras.models.load_model(model_path)
image_size = (224, 224)

def predict(file):
    img = keras.preprocessing.image.load_img(
        file, target_size=image_size
    )
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create batch axis

    predictions = model.predict(img_array)
    score = predictions[0]
    return score
    

import os
directory = 'photos'
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        score = predict(f)
        print(
        "%s =>  %.2f percent Tourist and %.2f percent None-Tourist."
        % (f, score[0] * 100, score[1] * 100)
        )
