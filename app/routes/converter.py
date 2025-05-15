from fastapi import APIRouter, Query

router = APIRouter()

@router.get("/cm-to-inch")
def cm_to_inch(value: float = Query(...)):
    return {"result": round(value / 2.54, 2)}

@router.get("/kg-to-pound")
def kg_to_pound(value: float = Query(...)):
    return {"result": round(value * 2.20462, 2)}
