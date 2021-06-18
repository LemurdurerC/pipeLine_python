import base64
import json
import string

import numpy as np
import uvicorn
from fastapi import FastAPI, File, UploadFile
import shutil
from fastapi.middleware.cors import CORSMiddleware
from elasticsearch import Elasticsearch

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
    data = {"id" : "999", "company" : "alfonso", "date" : "18-06-2021", "total" : "200"}
    datas = json.dumps(data)
    sendElasticSearch(datas)

    # appeler le reste du pipeline
    #ocr
    #prédiction
    # retour à l'utilisateur + stockage elastic search

def sendElasticSearch(datas):
    es = Elasticsearch(HOST="http://localhost", PORT=9200)
    es = Elasticsearch()
    ticket_data = json.loads(datas)
    ticket = {"id": ticket_data["id"], "company": ticket_data["company"],"date": ticket_data["date"], "total": ticket_data["total"]}
    es.index(index="tickets", doc_type="text", body=ticket)



if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
