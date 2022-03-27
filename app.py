'''
Date: 2022-03-26 14:01:38
LastEditors: Azus
LastEditTime: 2022-03-26 22:12:10
FilePath: /react-ml-app/app.py
'''
import _thread
from backend import *
import time
import os


# def get_mode():
#     for i in range(1,15):
#                 time.sleep(2)
#                 i+=1
#                 print(os.getenv('FLASK_ENV')
# )

app = create_app()

if __name__ =="__main__":
    # _thread.start_new_thread(get_mode, ())
    
    app.run(debug=False)

    # app.run(debug=True)