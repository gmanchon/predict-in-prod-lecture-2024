from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return { "true": 123 }

@app.get("/pred")
def pred(day_of_week, passenger_count):

    day = int(day_of_week)
    count = int(passenger_count)

    return { "pred" : day * count }
