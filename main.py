from fastapi import FastAPI
app = FastAPI()

#define a root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello,World"}

#define another endpoint with a parameter
@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}!"}