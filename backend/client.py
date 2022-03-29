'''
Date: 2022-03-25 13:07:06
LastEditors: Azus
LastEditTime: 2022-03-27 21:23:27
FilePath: /KDS/pyqt_deploy/client.py
'''
import requests
import time

# Initialize the keras REST API endpoint URL.
REST_API_URL = 'http://101.43.232.154:7000/predict'
REST_API_URL = 'http://101.43.232.154:7000/predict'


def predict_result(image_path):
    # Initialize image path
    image = open(image_path, 'rb').read()
    payload = {'image': image}

    # Submit the request.
    r = requests.post(REST_API_URL, files=payload).json()

    # Ensure the request was successful.
    if r['success']:
        # Loop over the predictions and display them.
        result: object
        for (i, result) in enumerate(r['predictions']):
            return result
    # Otherwise, the request failed.
    else:
        print('Request failed')


if __name__ == '__main__':
    t1 = time.time()
    img_path = './amb.JPG'
    predict_result(img_path)
    t2 = time.time()
    print(t2 - t1)
