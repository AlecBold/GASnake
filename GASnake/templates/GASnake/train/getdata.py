import json


def queryForData(data):
    # Get query
    get_query = True
    if get_query:
        with open("snake_front.json", "w") as frontsnake:
            json.dump(data, frontsnake)