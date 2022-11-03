import copy
from collections import deque
from typing import Dict, Any, Callable

import requests
import logging

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



class Place:

    @staticmethod
    def from_query(query: str) -> 'Place':
        resp = requests.get(url=constants.AUTO_COMPLETE_URL.format(query=query))
        resp.raise_for_status()
        data = resp.json()["autocomplete_terms"][0]["explore_search_params"]
        place = Place(id=data["place_id"], query=data["query"])
        log.info(f'Autompleting:{query=}. Result: {place=}')
        return place

    def __init__(self, id: str, query: str) -> None:
        self.id = id
        self.query = query

    def __str__(self):
        return f"Place(id={self.id} query={self.query})"

    __repr__ = __str__

    def process(self, on_new_item: Callable[[Any], None]) -> None:
        for i in range(0, 2):
            data = copy.deepcopy(constants.data)
            data["variables"]["exploreRequest"]["placeId"] = self.id
            data["variables"]["exploreRequest"]["itemsOffset"] = i * constants.items_per_page

            response = requests.post(url=constants.STAY_SEARCH_URL, headers=constants.headers, json=data)
            response.raise_for_status()
            log.info(f'Page: {i}')

            # results = response.json()["data"]["presentation"]["explore"]["sections"]["sectionIndependentData"]["staysSearch"]["searchResults"]
            sections = response.json()["data"]["presentation"]["explore"]["sections"]["sections"]
            for section in sections:
                try:
                    items = section["section"]["child"]["section"]["items"]
                    for item in items:
                        item = self._prepare_item(item=normalize(d=item))
                        on_new_item(item=item)
                except KeyError:
                    pass

    def _prepare_item(self, item: Dict[str, Any]) -> Dict[str, Any]:
        item["place_name"] = self.query
        return item

