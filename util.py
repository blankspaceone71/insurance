import numpy as np
import pickle

with open('./artifacts/alk.pickle', 'rb') as g:
    model = pickle.load(g)


def insurance_prediction(input_data):

    y = np.array(input_data)
    d = y.reshape(1, -1)
    prediction = model.predict(d)

    return round(prediction[0], 2)
