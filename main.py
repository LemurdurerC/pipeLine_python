import base64
import string

import numpy as np
import uvicorn
from fastapi import FastAPI, File, UploadFile
import shutil
from fastapi.middleware.cors import CORSMiddleware

import cv2


app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/")
async def create_upload_file(file: UploadFile = File(...)):
    test = file.file.read()
    test2 = np.frombuffer(test,np.uint8)
    try:
        img = cv2.imdecode(test2,cv2.IMREAD_COLOR)
        print("ok")
        cv2.imshow("test", img)
        cv2.waitKey()
    except Exception as e:
        print("Lol")
    return "test"

    # appeler le reste du pipeline
    #ocr
    #prédiction
    # retour à l'utilisateur + stockage elastic search


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
