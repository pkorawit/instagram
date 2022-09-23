
# Tourist or Non-tourist post classification

import tensorflow as tf
from tensorflow import keras
model_path = './models/Model_VGG16_C[TourNotour]_E100B64.h5' 
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

def setIsTourism(shortcode):
    try:
        sql = """ UPDATE sandbox.post SET is_tourism=true WHERE shortcode='{}'""".format(shortcode)
        cur = conn.cursor()
        # print(sql)
        cur.execute(sql)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    

import os
directory = 'post_images_sandbox'
#directory = 'photos'
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
            # "%d/%d %s =>  %.2f percent Tourism and %.2f percent None Tourism."
            # % (count, len(list), shortcode, score[0] * 100, score[1] * 100)
            # )
            if score[0] > score[1]:
                print("%d/%d %s => is Tourism" % (count, len(list), shortcode))
                setIsTourism(shortcode)
        except (Exception) as error:
            print(error)

conn.commit()
conn.close()