import requests
import logging


log = logging.getLogger(__name__)


def get_place_id(query):
    url = f'https://www.airbnb.com/api/v2/autocompletes?country=TR&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&language=en&locale=en-GB&num_results=5&user_input={query}&api_version=1.2.0&satori_config_token=EhIiQRIiIjISEjISIRESIlFCNaoDFQYVWBUCBYoBAAA&vertical_refinement=homes&region=-1&options=should_filter_by_vertical_refinement|hide_nav_results|should_show_stays|simple_search|flex_destinations_june_2021_launch_web_treatment'
    resp = requests.get(url=url)
    resp.raise_for_status()
    data = resp.json()["autocomplete_terms"][0]["explore_search_params"]
    place_id = data["place_id"]
    log.info(f'Autompleting:{query=}. Result: {place_id=} query={data["query"]}')
    return place_id
