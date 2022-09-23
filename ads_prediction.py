
# Ads or Not Ads Classification

import tensorflow as tf
from tensorflow import keras
model_path = './models/Model_ResNet50_C[AdsNoads]_E100B64.h5' 
model = keras.models.load_model(model_path)
image_size = (224, 224)

import psycopg2
conn = psycopg2.connect(
    host="172.26.117.18",
    database="postgres",
    user="postgres",
    password="zxc123**")


def predict(file):
    img = keras.preprocessing.image.load_img(
        file, target_size=image_size
    )
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create batch axis

    predictions = model.predict(img_array)
    score = predictions[0]
    return score

def setIsAds(shortcode):
    try:
        sql = """ UPDATE sandbox.post SET is_ads=true WHERE shortcode='{}'""".format(shortcode)
        cur = conn.cursor()
        # print(sql)
        cur.execute(sql)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    

import os
directory = 'post_images_sandbox'
# directory = `I:\\post_images_sandbox\\`
count = 0
list =  sorted(os.listdir(directory))
for filename in list:
    count = count + 1
    f = os.path.join(directory, filename)
    shortcode = os.path.splitext(filename)[0]
    # checking if it is a file
    if os.path.isfile(f):
        try:
            score = predict(f)
            # print(
            # "%d/%d %s =>  %.2f percent Ads and %.2f percent Not Ads."
            # % (count, len(list), shortcode, score[0] * 100, score[1] * 100)
            # )
            if score[0] > score[1]:
                print("%d/%d %s => is Ads" % (count, len(list), shortcode))
                setIsAds(shortcode)
        except (Exception) as error:
            print(error)

conn.commit()
conn.close()
