'''
Date: 2022-03-27 16:37:30
LastEditors: Azus
LastEditTime: 2022-03-27 18:59:38
FilePath: /KDS/possibility.py
'''
import enum
import random

            # {
            #   "0":"micro",
            #   "1":"fungus",
            #   "2":"amb",
            #   "3":"virus"
            # }

            # #modified
            # res = label_id_name_dict[str(pred_label)]
            # data = get_possibility(res)
            # # indicate that the request was a success
            # data["success"] = True
            # # print(data["success"])

    # return the data dictionary as a JSON response
    # return jsonify(data), 200, [("Access-Control-Allow-Origin", "*")]


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

if __name__=='__main__':
    data=get_possibility('virus')
    print(data)