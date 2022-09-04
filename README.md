Keratitis Diagnosis System - Diagnosis Keratitis by simply uploading photos
---
![Demo](https://github.com/az0s/KDS/blob/main/demo.gif?raw=true)
A web application showcasing keratitis classification using deep learning, based on DenseNet and ResNet.

Live Demo currently closed.

## Setup 

Clone this repository, modity `server.py` to run backend server on your server:
```py
109    app.run(host='0.0.0.0', port=8080, debug=False)
``` 

Install frontend dependencies:
```sh
cd frontend && yarn install
```
run frontend server:

```sh
npm run start
```

## Dirs 
.  
├── README.md  
├── backend             --Full backend  
├── frontend            --Regular frontend  
├── frontend_mobile     --Mobile frontend   
├── pyqt_deploy         --PyQt source file  
└── server.py           --Entry file for backend server