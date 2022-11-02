import datetime
from pathlib import Path
import logging
from airbnbcrawl import autocomplete
from airbnbcrawl import stay_search
from airbnbcrawl.results import Results

log = logging.getLogger(__name__)


def main() -> None:
    logging.basicConfig(level=logging.INFO)
    # requests_cache.install_cache("requests.cache", allowable_methods=("GET", "POST", "HEAD"))
    dt_str = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
    artifacts = Path(f"artifacts/{dt_str}")
    artifacts.mkdir(parents=True, exist_ok=True)

    results = Results(artifacts=artifacts)

    queryies = ['antalya turkey']
    for query in queryies:
        place_id = autocomplete.get_place_id(query=query)
        stay_search.process(place_id=place_id, on_new_item=results.on_new_item)
    results.dump()


if __name__ == "__main__":
    main()
