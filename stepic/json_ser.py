import json

def main():

    python_data = {
        "make" : "Opel",
        "model" : "Mokka",
        "colours" : [
            "Black", 
            "White",
            "Blue"
        ],
        "price" : 20000.99
    }

    json_str = json.dumps(python_data, indent = 3)
    print(json_str)
