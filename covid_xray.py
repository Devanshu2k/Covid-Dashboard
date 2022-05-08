
from keras.models import model_from_json 
from keras.losses import binary_crossentropy
from keras.preprocessing import image
import numpy as np

# opening and store file in a variable
def xray_predict(name):
    json_file = open('model.json','r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights("model.h5")

    loaded_model.compile(loss="binary_crossentropy",optimizer='adam',metrics=['accuracy'])

    img=image.load_img(name, target_size=(224,224 ))
    x=image.img_to_array(img)
    x /= 255
    x=np.expand_dims(x, axis=0)
    res = loaded_model.predict(x)
    print(res[0])
    if res[0]<0.5:
        return "COVID"
    else:
        return "NORMAL"