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
