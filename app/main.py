from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="DevOps Journey API",
    description="A small API starter for an end-to-end DevOps project.",
    version="1.0.0",
)

STATIC_DIR = Path(__file__).parent / "static"
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


class Item(BaseModel):
    id: int
    name: str
    description: str


ITEMS = {
    1: Item(id=1, name="sample-item", description="A sample catalog item."),
    2: Item(id=2, name="devops", description="Ready for the DevOps journey."),
}


@app.get("/", tags=["learning hub"])
def read_root() -> FileResponse:
    return FileResponse(STATIC_DIR / "index.html")


@app.get("/health", tags=["health"])
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/api/v1/items", response_model=list[Item], tags=["items"])
def list_items() -> list[Item]:
    return list(ITEMS.values())


@app.get("/api/v1/items/{item_id}", response_model=Item, tags=["items"])
def get_item(item_id: int) -> Item:
    item = ITEMS.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
