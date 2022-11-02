from typing import Any
import pandas as pd


class Results:
    def __init__(self, artifacts):
        self.artifacts = artifacts
        self.data = []

    def on_new_item(self, d: dict[str, Any]):
        self.data.append(d)

    def dump(self):
        data = pd.json_normalize(self.data)
        pd.to_pickle(obj=data, filepath_or_buffer=(self.artifacts / 'data.zip'))
