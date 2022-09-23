
# Ads or Not Ads Tourism or Non tourism Classification

from operator import truediv
import tensorflow as tf
from tensorflow import keras
import requests

ads_model_path = './models/Model_ResNet50_C[AdsNoads]_E100B64.h5' 
tour_model_path = './models/Model_VGG16_C[TourNotour]_E100B64.h5' 
ads_model = keras.models.load_model(ads_model_path)
tour_model = keras.models.load_model(tour_model_path)

image_size = (224, 224)

def predict(shortcode):

    url = "https://www.instagram.com/p/{}/media/?size=l".format(shortcode)
    print(url)
    response = requests.get(url)
    image_path = "./temp/{}.jpg".format(shortcode)
    open(image_path, "wb").write(response.content)

    img = keras.preprocessing.image.load_img(
        image_path, target_size=image_size
    )
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create batch axis

    ads_predictions = ads_model.predict(img_array)
    tour_predictions = tour_model.predict(img_array)
    ads_score = ads_predictions[0]
    tour_score = tour_predictions[0]
    print(ads_score, tour_score)

    if ads_score[0] > ads_score[1]:
        ads_result = True
    else:
        ads_result = False   

    if tour_score[0] > tour_score[1]:
        tour_result = True
    else:
        tour_result = False       
    
    result = {
        "is_ads": ads_result,
        "is_tourism": tour_result
        }
    return result

