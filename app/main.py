from pathlib import Path
import sys

import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

PROJECT_DIR = Path(__file__).resolve().parent.parent
if str(PROJECT_DIR) not in sys.path:
    sys.path.insert(0, str(PROJECT_DIR))

STATIC_DIR = Path(__file__).parent / "static"

app = FastAPI(
    title="DevOps Journey",
    description="A practical learning hub for DevOps tools and workflows.",
    version="1.0.0",
)
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


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
