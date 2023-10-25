# database = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
database = [{"item_id": i, "name": f"Item {i}"} for i in range(100)]

items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {
        "name": "Bar", 
        "description": "The Bar fighters", 
        "price": 62, 
        "tax": 20.2
    },
    "baz": {
        "name": "Baz",
        "description": "There goes my baz",
        "price": 50.2,
        "tax": 10.5,
    },
}

base_items = {
    "item1": {"description": "All my friends drive a low rider", "type": "car"},
    "item2": {
        "description": "Music is my aeroplane, it's my aeroplane",
        "type": "plane",
        "size": 5,
    },
}

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
