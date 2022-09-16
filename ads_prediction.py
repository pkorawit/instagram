
# Ads or Not Ads Classification

import tensorflow as tf
from tensorflow import keras
model_path = './models/Model_ResNet50_C[AdsNoads]_E100B64.h5' 
model = keras.models.load_model(model_path)
image_size = (224, 224)
img = keras.preprocessing.image.load_img(
    "./photos/CS0f9gyBjOm.jpg", target_size=image_size
)
img_array = keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)  # Create batch axis

predictions = model.predict(img_array)
score = predictions[0]
print(score)
print(
    "This image is %.2f percent Ads and %.2f percent Not Ads."
    % (score[0] * 100, score[1] * 100)
)