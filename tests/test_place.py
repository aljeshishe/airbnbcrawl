from airbnbcrawl import constants
from airbnbcrawl.place import Place


class Test_get_place_id:
    def test_complex(self, requests_mock):
        query = "antalya turkey"
        response = {
            "autocomplete_terms": [
                {
                    "id": "d33aadf9d9b0e7a19009fcdb5bf75a2ba596514c5b552b73c24018bccb35a883",
                    "explore_search_params": {
                        "params": [
                            {
                                "key": "acp_id",
                                "value_type": "string",
                                "in_array": False,
                                "value": "7297ac2f-04ce-43f3-b97d-a6ad09adb9d5",
                                "delete": False,
                                "invisible_to_user": False
                            }
                        ],
                        "place_id": "ChIJwa2t3a6awxQRMy7j-XOfxpU",
                        "query": "Antalya, Turkey",
                        "refinement_paths": [
                            "/homes"
                        ],
                        "refinement_path": "/homes",
                        "tab_id": "home_tab",
                        "reset_filters": False,
                        "reset_keys": []
                    },
                    "suggestion_type": "LOCATION",
                    "vertical_type": "homes",
                    "display_name": "Antalya, Turkey",
                    "metadata": {
                        "location_only_result": True,
                        "airmoji": "description_map_pin"
                    },
                    "location": {
                        "offset_start": 0,
                        "offset_end": 14,
                        "location_name": "Antalya, Turkey",
                        "google_place_id": "ChIJwa2t3a6awxQRMy7j-XOfxpU",
                        "types": [
                            "locality",
                            "political"
                        ],
                        "terms": [
                            {
                                "offset": 0,
                                "value": "Antalya"
                            },
                            {
                                "offset": 9,
                                "value": "Turkey"
                            }
                        ],
                        "parent_city_display_name": "",
                        "country_code": "TR",
                        "countryCode": "TR",
                        "parentCityDisplayName": ""
                    },
                    "refinements": [],
                    "highlights": [],
                    "sxs_debug_info": {
                        "sxs_score_attrs": {},
                        "sxs_debug_metadata": {}
                    },
                    "suggestionType": "LOCATION",
                    "verticalType": "homes"
                },
                {
                    "id": "30c9155b59c3a1e60b23499b3a8dea0f6d1962065a436099d44d4b2207b70047",
                    "explore_search_params": {
                        "params": [
                            {
                                "key": "acp_id",
                                "value_type": "string",
                                "in_array": False,
                                "value": "1c39ea22-43e8-4218-96ba-77c0e592bd95",
                                "delete": False,
                                "invisible_to_user": False
                            }
                        ],
                        "place_id": "ChIJWQCqO3B7wxQRdmlDcOgzsfE",
                        "query": "Belek, Antalya, Turkey",
                        "refinement_paths": [
                            "/homes"
                        ],
                        "refinement_path": "/homes",
                        "tab_id": "home_tab",
                        "reset_filters": False,
                        "reset_keys": []
                    },
                    "suggestion_type": "LOCATION",
                    "vertical_type": "homes",
                    "display_name": "Belek, Antalya",
                    "metadata": {
                        "location_only_result": True,
                        "airmoji": "description_map_pin"
                    },
                    "location": {
                        "offset_start": 0,
                        "offset_end": 21,
                        "location_name": "Belek, Antalya, Turkey",
                        "google_place_id": "ChIJWQCqO3B7wxQRdmlDcOgzsfE",
                        "types": [
                            "locality",
                            "political"
                        ],
                        "terms": [
                            {
                                "offset": 0,
                                "value": "Belek"
                            },
                            {
                                "offset": 7,
                                "value": "Antalya"
                            },
                            {
                                "offset": 16,
                                "value": "Turkey"
                            }
                        ],
                        "parent_city_display_name": "",
                        "country_code": "TR",
                        "countryCode": "TR",
                        "parentCityDisplayName": ""
                    },
                    "refinements": [],
                    "highlights": [],
                    "sxs_debug_info": {
                        "sxs_score_attrs": {},
                        "sxs_debug_metadata": {}
                    },
                    "suggestionType": "LOCATION",
                    "verticalType": "homes"
                },
                {
                    "id": "ee7360472eeccfd630e34f7a31c20f812aa04a505e6b879466a069e8f0ba5525",
                    "explore_search_params": {
                        "params": [
                            {
                                "key": "acp_id",
                                "value_type": "string",
                                "in_array": False,
                                "value": "0fdfc8ca-cf93-47d2-8c9d-cd697633319d",
                                "delete": False,
                                "invisible_to_user": False
                            }
                        ],
                        "place_id": "ChIJGd0brNBbwxQR6lDBgFVVqYw",
                        "query": "Side, Antalya, Turkey",
                        "refinement_paths": [
                            "/homes"
                        ],
                        "refinement_path": "/homes",
                        "tab_id": "home_tab",
                        "reset_filters": False,
                        "reset_keys": []
                    },
                    "suggestion_type": "LOCATION",
                    "vertical_type": "homes",
                    "display_name": "Side, Antalya",
                    "metadata": {
                        "location_only_result": True,
                        "airmoji": "description_map_pin"
                    },
                    "location": {
                        "offset_start": 0,
                        "offset_end": 20,
                        "location_name": "Side, Antalya, Turkey",
                        "google_place_id": "ChIJGd0brNBbwxQR6lDBgFVVqYw",
                        "types": [
                            "locality",
                            "political"
                        ],
                        "terms": [
                            {
                                "offset": 0,
                                "value": "Side"
                            },
                            {
                                "offset": 6,
                                "value": "Antalya"
                            },
                            {
                                "offset": 15,
                                "value": "Turkey"
                            }
                        ],
                        "parent_city_display_name": "",
                        "country_code": "TR",
                        "countryCode": "TR",
                        "parentCityDisplayName": ""
                    },
                    "refinements": [],
                    "highlights": [],
                    "sxs_debug_info": {
                        "sxs_score_attrs": {},
                        "sxs_debug_metadata": {}
                    },
                    "suggestionType": "LOCATION",
                    "verticalType": "homes"
                },
                {
                    "id": "e06fb2c8b2457bd1fcfa87919c8697a538d62845aa753d20e00832f6a7bbab1e",
                    "explore_search_params": {
                        "params": [
                            {
                                "key": "acp_id",
                                "value_type": "string",
                                "in_array": False,
                                "value": "f86ab07d-6b14-4e19-b5c3-7eb929e07c51",
                                "delete": False,
                                "invisible_to_user": False
                            }
                        ],
                        "place_id": "ChIJd8t--SWFwxQRLPz1nFcDN5Y",
                        "query": "Muratpaşa, Antalya, Turkey",
                        "refinement_paths": [
                            "/homes"
                        ],
                        "refinement_path": "/homes",
                        "tab_id": "home_tab",
                        "reset_filters": False,
                        "reset_keys": []
                    },
                    "suggestion_type": "LOCATION",
                    "vertical_type": "homes",
                    "display_name": "Muratpaşa, Antalya",
                    "metadata": {
                        "location_only_result": True,
                        "airmoji": "description_map_pin"
                    },
                    "location": {
                        "offset_start": 0,
                        "offset_end": 25,
                        "location_name": "Muratpaşa, Antalya, Turkey",
                        "google_place_id": "ChIJd8t--SWFwxQRLPz1nFcDN5Y",
                        "types": [
                            "administrative_area_level_2",
                            "political"
                        ],
                        "terms": [
                            {
                                "offset": 0,
                                "value": "Muratpaşa"
                            },
                            {
                                "offset": 11,
                                "value": "Antalya"
                            },
                            {
                                "offset": 20,
                                "value": "Turkey"
                            }
                        ],
                        "parent_city_place_id": "ChIJwa2t3a6awxQRMy7j-XOfxpU",
                        "parent_city_display_name": "安塔利亚",
                        "country_code": "TR",
                        "parentCityPlaceId": "ChIJwa2t3a6awxQRMy7j-XOfxpU",
                        "countryCode": "TR",
                        "parentCityDisplayName": "安塔利亚"
                    },
                    "refinements": [],
                    "highlights": [],
                    "sxs_debug_info": {
                        "sxs_score_attrs": {},
                        "sxs_debug_metadata": {}
                    },
                    "suggestionType": "LOCATION",
                    "verticalType": "homes"
                },
                {
                    "id": "a54c7101471b087e2ef14ed4ad140a876f4f6d42c814534a6b9ef826c44dac79",
                    "explore_search_params": {
                        "params": [
                            {
                                "key": "acp_id",
                                "value_type": "string",
                                "in_array": False,
                                "value": "dd6f3dcc-e106-4098-a16c-ee133be2db20",
                                "delete": False,
                                "invisible_to_user": False
                            }
                        ],
                        "place_id": "ChIJD5quDDI0whQR29gQ0hTB__0",
                        "query": "Çıralı, Antalya, Turkey",
                        "refinement_paths": [
                            "/homes"
                        ],
                        "refinement_path": "/homes",
                        "tab_id": "home_tab",
                        "reset_filters": False,
                        "reset_keys": []
                    },
                    "suggestion_type": "LOCATION",
                    "vertical_type": "homes",
                    "display_name": "Çıralı, Antalya",
                    "metadata": {
                        "location_only_result": True,
                        "airmoji": "description_map_pin"
                    },
                    "location": {
                        "offset_start": 0,
                        "offset_end": 22,
                        "location_name": "Çıralı, Antalya, Turkey",
                        "google_place_id": "ChIJD5quDDI0whQR29gQ0hTB__0",
                        "types": [
                            "locality",
                            "political"
                        ],
                        "terms": [
                            {
                                "offset": 0,
                                "value": "Çıralı"
                            },
                            {
                                "offset": 8,
                                "value": "Antalya"
                            },
                            {
                                "offset": 17,
                                "value": "Turkey"
                            }
                        ],
                        "parent_city_display_name": "",
                        "country_code": "TR",
                        "countryCode": "TR",
                        "parentCityDisplayName": ""
                    },
                    "refinements": [],
                    "highlights": [],
                    "sxs_debug_info": {
                        "sxs_score_attrs": {},
                        "sxs_debug_metadata": {}
                    },
                    "suggestionType": "LOCATION",
                    "verticalType": "homes"
                }
            ],
            "metadata": {
                "request_id": "c24e57a09a9b4f91a13b021d92b8e85a"
            },
            "terms_offsets": {},
            "autocomplete_result_title": "non_china_new_search_entry_request",
            "experiments_to_log": [],
            "disable_cdn_cache": False,
            "autocompleteResultTitle": "non_china_new_search_entry_request"
        }
        requests_mock.get(constants.AUTO_COMPLETE_URL.format(query=query), json=response)
        place = Place.from_query(query=query)
        assert place.id == "ChIJwa2t3a6awxQRMy7j-XOfxpU"
