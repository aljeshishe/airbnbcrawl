import copy
import logging
from collections import deque
from typing import Dict, Any

import requests

from airbnbcrawl import constants

log = logging.getLogger(__name__)


def normalize(d: Dict[str, Any]) -> Dict[str, Any]:
    result = {}

    def _normalize(d, keys=deque()):
        for k, v in d.items():
            if k.startswith("__"):
                continue
            if isinstance(v, list):
                continue
            if isinstance(v, dict):
                _normalize(d=v, keys=keys + deque([k]))
                continue
            keys_str = "_".join(keys + deque([k]))
            result[keys_str] = v
        return result
    return _normalize(d=d)


def process(place_id, on_new_item):
    url = 'https://www.airbnb.ru/api/v3/StaysSearch?operationName=StaysSearch&locale=ru&currency=USD'
    for i in range(0, 2):
        data = copy.deepcopy(constants.data)
        data["variables"]["exploreRequest"]["placeId"] = place_id
        data["variables"]["exploreRequest"]["itemsOffset"] = i * constants.items_per_page

        response = requests.post(url=url, headers=constants.headers, json=data)
        response.raise_for_status()
        log.info(f'Page: {i}')

        # results = response.json()["data"]["presentation"]["explore"]["sections"]["sectionIndependentData"]["staysSearch"]["searchResults"]
        sections = response.json()["data"]["presentation"]["explore"]["sections"]["sections"]
        for section in sections:
            try:
                items = section["section"]["child"]["section"]["items"]
                for item in items:
                    on_new_item(d=normalize(d=item))
            except KeyError:
                pass

