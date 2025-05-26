from fastapi import FastAPI

app = FastAPI()

@app.get("/data")
def data():
    return {"message": "Hello World"}

@app.get('/api')
def datta():
    return [
        {
            'name': 'Moeez',
            'age': 23
        },
        {
            'name': 'Adnan',
            'age': 21
        },
        {
            'name': 'Ali',
            'age': 25
        }
    ]

