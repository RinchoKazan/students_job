from typing import Annotated
from fastapi import Path, APIRouter

router = APIRouter(
    prefix="/items",
    tags=["items"]
)

@router.get("/")
def list_items():
    return {
        'item1': 'test1',
        'item2': 'test1',
        'item3': 'test3',
        'item4': 'test4',
    }



@router.get('/latest')
def get_latest_item():
    return {'item_id': {'id': '0', 'name': 'latest'}}


@router.get("/{item_id}")
def list_items(item_id: Annotated[int, Path(ge=1, lt=100000)]):
    return {
        'item': {
            "id": item_id,
        }
    }
