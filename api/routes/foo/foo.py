from leanapi.path import controller
from leanapi.server import router
from .models.body import BodyModel


@controller("foo", router)
class Foo:
    @router.get("/get/{path_id}")
    def get_personel(self, path_id: int) -> dict:
        return {"id": path_id}

    @router.post("/post")
    def save_product(self, data: BodyModel) -> dict:
        return dict(data)
