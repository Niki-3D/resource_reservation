from fastapi import FastAPI

app = FastAPI(title="Resource Reservation System")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Resource Reservation API!"}
