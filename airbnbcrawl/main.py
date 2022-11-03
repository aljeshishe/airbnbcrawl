import datetime
import logging
from pathlib import Path

from airbnbcrawl.place import Place
from airbnbcrawl.results import Results

log = logging.getLogger(__name__)


def main() -> None:
    logging.basicConfig(level=logging.INFO)
    # requests_cache.install_cache("requests.cache", allowable_methods=("GET", "POST", "HEAD"))
    dt_str = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
    artifacts = Path(__file__).parent.parent / f"artifacts/{dt_str}"
    artifacts.mkdir(parents=True, exist_ok=True)

    results = Results(artifacts=artifacts)

    queryies = ['antalya turkey']
    for query in queryies:
        place = Place.from_query(query=query)
        place.process(on_new_item=results.on_new_item)
    results.dump()


if __name__ == "__main__":
    main()
