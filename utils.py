import json
import os


def load_schema(filepath):
    with open(os.path.dirname(os.path.abspath(__file__)) + '/schemes/' + filepath) as file:
        schema = json.load(file)
        return schema
