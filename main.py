import base64
import string

import numpy as np
import uvicorn
from fastapi import FastAPI, File, UploadFile
import shutil

import cv2


app = FastAPI()

@app.post("/")
async def create_upload_file(file: UploadFile = File(...)):
    test = file.file.read()
    test2 = np.frombuffer(test,np.uint8)
    img = cv2.imdecode(test2,cv2.IMREAD_COLOR)
    cv2.imshow("test", img)
    cv2.waitKey()

    return {"filename": file.filename}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
