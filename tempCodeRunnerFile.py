@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}!"}