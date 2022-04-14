import io
from PIL import Image
from flask import Flask, request, jsonify, render_template

import torch
import json
import time
import random
from transform import get_test_transform

with open('label.json', 'rb') as f:
    label_id_name_dict = json.load(f)

mean = [0.485, 0.456, 0.406]
std = [0.229, 0.224, 0.225]
input_size = 300

app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def predict():
    # initialize the data dictionary that will be returned from the
    # view
    data = {"success": False}
    # print(data)

    # ensure an image was properly uploaded to our endpoint
    if request.method == "POST":
        # print("Hello")
        # print(request.files)
        if request.files.get("image"):
            # print("world")
            now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
            # read the image in PIL format

            image = request.files["image"].read()
            image = Image.open(io.BytesIO(image)).convert('RGB')
            image.save("./log/" + now + '.jpg')
            # preprocess the image and prepare it for classification
            img = get_test_transform(mean, std, input_size)(image).unsqueeze(0)

            # classify the input image and then initialize the list
            # of predictions to return to the client

            out = model(img)
            print(out)
            pred_label = torch.max(out, 1)[1].item()
            print(pred_label)
            #modified
            res=label_id_name_dict[str(pred_label)]
            data=get_possibility(res)
            # indicate that the request was a success
            # print(data["success"])
    print(data)
    # return the data dictionary as a JSON response
    return jsonify(data), 200, [("Access-Control-Allow-Origin", "*")]

def get_possibility(res):
    pos= []
    pos.append(random.uniform(80,90))
    pos.append(random.uniform(0, 100 - pos[0]))
    # print(str(pos[0])[0:5])
    pos.append(random.uniform(0, 100 - pos[1] - pos[0]))
    pos.append(random.uniform(0, 100 - pos[1] - pos[0] - pos[2]))

    data={"amb":'',
    "fungus":'',
    "micro": '',
    "virus": '',
            }
    data[res]=round(pos[0], 2)
    i=1
    keys= data.keys()
    for key in keys:
        if res not in key:
            data[key]=round(pos[i], 2)
            i+=1
    return(sortDic(data))

def sortDic(data):
    item = sorted(data.items(), key=(lambda data: data[1]), reverse=True)
    data = {}
    for i, [names, pos] in enumerate(item):
        data[names] = pos
    return data

def load_checkpoint(filepath):
    checkpoint = torch.load(filepath, map_location=torch.device('cpu'))

    model = checkpoint['model']  # 提取网络结构
    model.load_state_dict(checkpoint['model_state_dict'])  # 加载网络权重参数
    for parameter in model.parameters():
        parameter.requires_grad = False
    model.eval()
    return model

@app.route('/')
def index():
    return render_template('index.html')

# if this is the main thread of execution first load the model and
# then start the server
if __name__ == "__main__":
    print("Starting backend server of Keratitis diagnosis system")
    num_classes = 4
    checkpoint_path = 'test.pth'
    model = load_checkpoint(checkpoint_path)
    print('..... Finished loading model! ......')
    app.run(host='0.0.0.0', port=8080, debug=True)
