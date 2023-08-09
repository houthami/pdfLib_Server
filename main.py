
from libraries import *
app = FastAPI()

@app.get("/")
def welcome():
    return {"message": 'api Hello world '}
