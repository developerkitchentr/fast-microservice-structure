from pydantic import BaseModel


class BodyModel(BaseModel):
    lang: str
    name: str
    age: int
