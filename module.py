from pydantic import BaseModel

class Service(BaseModel):
    id: int
    name: str
    desc: str
