from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="DevOps Journey API",
    description="A small API starter for an end-to-end DevOps project.",
    version="1.0.0",
)


class Item(BaseModel):
    id: int
    name: str
    description: str


ITEMS = {
    1: Item(id=1, name="sample-item", description="A sample catalog item."),
    2: Item(id=2, name="devops", description="Ready for the DevOps journey."),
}


@app.get("/", tags=["root"])
def read_root() -> dict[str, str]:
    return {
        "message": "Welcome to the DevOps Journey API",
        "docs": "/docs",
        "health": "/health",
    }


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
