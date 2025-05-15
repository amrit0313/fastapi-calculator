from fastapi import APIRouter, Query

router = APIRouter()

@router.get("/add")
def add(x: float = Query(...), y: float = Query(...)):
    return {"result": x + y}

@router.get("/subtract")
def subtract(x: float = Query(...), y: float = Query(...)):
    return {"result": x - y}

@router.get("/multiply")
def multiply(x: float = Query(...), y: float = Query(...)):
    return {"result": x * y}

@router.get("/divide")
def divide(x: float = Query(...), y: float = Query(...)):
    if y == 0:
        return {"error": "Division by zero"}
    return {"result": x / y}
