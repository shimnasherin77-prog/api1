from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def fun():
    return {"message": "welcome to math API"}

@app.get("/multiply/{number}")
def fun1(number: int):
   result=number*6
   return {"message":{number},"result":{result}}

@app.get("/square/{number}")
def fun2(number: int):
    result2=number**2
    return {"message":{number},"result2":{result2}}