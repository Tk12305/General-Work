import json

data = {
    "name": "Chloe",
    "age": 16,
    "City": "Kidlington"
}

json_data = json.dumps(data, indent=4)
print(json_data)