from pydantic import BaseModel

class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name

class HorseException(Exception):
    def __init__(self, name: str):
        self.name = name

class Item(BaseModel):
    title: str
    size: int
