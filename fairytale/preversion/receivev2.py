'''
file: receive.py
author: Guyoung Kwon
date: 2022.09.19
memo:
    
'''

from flask import Flask, Response, request
import cv2
import numpy as np
import jsonpickle
import matplotlib.pyplot as plt
import base64

app = Flask(__name__)
app.debug = True

def showImage(img):
    plt.imshow(img)
    plt.show()


@app.route('/receive/image', methods=['POST'])
def receive():
    data = request.get_json()
    img = base64.b64decode(data["image"])
    nparr = np.fromstring(img, dtype=np.uint8)
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # print(img)
    showImage(img)
    response = {'message':'image received. size={}x{}'.format(img.shape[0], img.shape[1])}

    # encode response
    response = jsonpickle.encode(response)
    return Response(response=response, status = 200, mimetype='application/json')

if __name__=='__main__':
    app.run(host='0.0.0.0', port = 5003)