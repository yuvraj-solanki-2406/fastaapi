from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {"page_name": "Home Page"}

@app.post("/login")
def login(req):
    name = req.name
    email = req.email
    return {"info": [name, email]}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)