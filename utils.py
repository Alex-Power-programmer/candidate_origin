import json
from pprint import pprint


def load_candidates():
    with open('candidates.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        candidates = {}
        for candidate in data:
            candidates[candidate['id']] = candidate
        return candidates


load_candidates()
