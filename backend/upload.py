from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[""],  # Replace "*" with your frontend domain in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    # Do OCR / table extraction / ML here
    # Return dummy response for now
    return {
        "filename": file.filename,
        "message": "File received and processed.",
        "mock_data": {
            "Name": "John Doe",
            "USN": "1AI21CS001",
            "Marks": {"Math": 23, "Physics": 20, "Chemistry": 25}
        }
    }