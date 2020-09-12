from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def dashboard():
    """
    displays the stock screener dashboard/ homepage

    """
    return {"Dashboard": "Home Page"}


@app.post("/stock")
def create_stock():
    """
    create a stock and stores in the database

    """
    return {
        "code": "success",
        "message": "created",
    }
