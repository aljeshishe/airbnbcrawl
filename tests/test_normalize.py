import json

from airbnbcrawl.place import normalize


class TestNormalize:
    def test_empty(self):
        d = {}
        assert normalize(d) == {}

    def test1(self):
        d = {"a": {"b": 1}}
        assert normalize(d) == {"a_b": 1}

    def test_dunderscore_keys_deleted(self):
        d = {"__a": 2}
        assert normalize(d) == {}

    def test_complex(self):
        d = '''{
            "__typename": "ExploreListingItem",
            "listing": {
                "__typename": "ExploreListing",
                "avgRating": 4.64,
                "businessHostLabel": null,
                "contextualPictures": [
                    {
                        "__typename": "ExplorePicture",
                        "caption": null,
                        "id": "1419043944",
                        "picture": "https://a0.muscache.com/im/pictures/29aac32f-f966-4bf8-ad21-0f0fe9b5322e.jpg?im_w=720"
                    },
                    {
                        "__typename": "ExplorePicture",
                        "caption": {
                            "__typename": "ExploreKickerContent",
                            "kickerBadge": null,
                            "messages": [
                                "2 кровати",
                                "2 спальни"
                            ]
                        },
                        "id": "1371851785",
                        "picture": "https://a0.muscache.com/im/pictures/8212fd45-9b28-439a-87fa-6afde5e016e0.jpg?im_w=720"
                    },
                    {
                        "__typename": "ExplorePicture",
                        "caption": {
                            "__typename": "ExploreKickerContent",
                            "kickerBadge": null,
                            "messages": [
                                "1 ванная"
                            ]
                        },
                        "id": "1419043258",
                        "picture": "https://a0.muscache.com/im/pictures/9bf5bea5-4a1f-4039-949e-1224e987238c.jpg?im_w=720"
                    },
                    {
                        "__typename": "ExplorePicture",
                        "caption": {
                            "__typename": "ExploreKickerContent",
                            "kickerBadge": null,
                            "messages": [
                                "Wi-Fi",
                                "Кондиционер",
                                "Стиральная машина",
                                "Кухня"
                            ]
                        },
                        "id": "1419041904",
                        "picture": "https://a0.muscache.com/im/pictures/1a87a680-8cbe-4afa-a6b0-388b1a3793f7.jpg?im_w=720"
                    },
                    {
                        "__typename": "ExplorePicture",
                        "caption": {
                            "__typename": "ExploreKickerContent",
                            "kickerBadge": null,
                            "messages": [
                                "Оценка за чистоту 4,2 из 5"
                            ]
                        },
                        "id": "1412402147",
                        "picture": "https://a0.muscache.com/im/pictures/35d68249-3dd1-41b6-be47-14a76539e5b4.jpg?im_w=720"
                    },
                    {
                        "__typename": "ExplorePicture",
                        "caption": null,
                        "id": "1370064278",
                        "picture": "https://a0.muscache.com/im/pictures/miso/Hosting-593482590454706058/original/02379e2f-fefa-41f9-9e2c-bf64e798df8c.jpeg?im_w=720"
                    }
                ],
                "contextualPicturesPageInfo": {
                    "__typename": "PageInfo",
                    "hasNextPage": true,
                    "endCursor": "NQ=="
                },
                "formattedBadges": [
                    {
                        "__typename": "ExploreFormattedBadge",
                        "backgroundColor": "rgba(255, 255, 255, 0.95)",
                        "borderColor": "rgba(0, 0, 0, 0.2)",
                        "text": "Редкая находка",
                        "textColor": "#222222"
                    }
                ],
                "homeDetails": [
                    {
                        "__typename": "BasicListItem",
                        "title": "2 гостя"
                    },
                    {
                        "__typename": "BasicListItem",
                        "title": "2 спальни"
                    },
                    {
                        "__typename": "BasicListItem",
                        "title": "2 кровати"
                    },
                    {
                        "__typename": "BasicListItem",
                        "title": "1 ванная"
                    }
                ],
                "id": "593482590454706058",
                "isNewListing": false,
                "isSuperhost": false,
                "kickerContent": {
                    "__typename": "ExploreKickerContent",
                    "kickerBadge": null,
                    "messages": [
                        "Отдельная комната, Konak"
                    ],
                    "textColor": null
                },
                "lat": 38.43808,
                "listingObjType": "REGULAR",
                "lng": 27.146795,
                "localizedDistanceText": null,
                "locationTitle": null,
                "mainSectionMessage": {
                    "__typename": "ExploreMainSectionMessage",
                    "body": "Это жилье обычно забронировано.",
                    "bodyType": null,
                    "headline": "Редкая находка",
                    "iconType": null,
                    "type": "occupancy_rate"
                },
                "mainSectionMessages": [
                    {
                        "__typename": "ExploreMainSectionMessage",
                        "body": "Это жилье обычно забронировано.",
                        "bodyType": null,
                        "headline": "Редкая находка",
                        "iconType": null,
                        "type": "occupancy_rate"
                    }
                ],
                "name": "Альтернативная квартира в Альсанчаке",
                "overview": [
                    {
                        "__typename": "BasicListItem",
                        "title": "Отдельная комната"
                    },
                    {
                        "__typename": "BasicListItem",
                        "title": "Konak"
                    }
                ],
                "pdpDisplayExtensions": [],
                "pdpType": "MARKETPLACE",
                "pdpUrlType": "ROOMS",
                "personCapacity": 2,
                "pictureUrls": [],
                "previewAmenityNames": [
                    "Wi-Fi",
                    "Кондиционер",
                    "Стиральная машина",
                    "Кухня"
                ],
                "relaxedFilterLabels": null,
                "reviewsCount": 22,
                "roomTypeCategory": "private_room",
                "roomTypeId": null,
                "showPhotoSwipeIndicator": null,
                "summary": null,
                "tierId": 0,
                "titleLocale": "ru",
                "avgRatingLocalized": "4,64 (22)",
                "avgRatingA11yLabel": "Средний рейтинг: 4,64 из 5. Отзывов: 22",
                "structuredContent": {
                    "__typename": "ExploreStructuredContent",
                    "distance": [],
                    "primaryLine": [
                        {
                            "__typename": "MainSectionMessage",
                            "body": "2 кровати",
                            "bodyA11yLabel": null,
                            "bodyType": null,
                            "headline": null,
                            "type": null
                        }
                    ],
                    "secondaryLine": null
                },
                "title": "Отдельная комната, Konak"
            },
            "listingParamOverrides": null,
            "pricingQuote": {
                "__typename": "ExplorePricingQuote",
                "applicableDiscounts": null,
                "barDisplayPriceWithoutDiscount": null,
                "canInstantBook": null,
                "displayRateDisplayStrategy": null,
                "monthlyPriceFactor": null,
                "price": null,
                "priceDropDisclaimer": null,
                "priceString": null,
                "rate": null,
                "rateType": null,
                "rateWithoutDiscount": null,
                "rateWithServiceFee": null,
                "secondaryPriceString": null,
                "shouldShowFromLabel": false,
                "structuredStayDisplayPrice": {
                    "__typename": "StructuredDisplayPrice",
                    "primaryLine": {
                        "__typename": "QualifiedDisplayPriceLine",
                        "displayComponentType": "QUALIFIED_DISPLAY_PRICE_LINE",
                        "accessibilityLabel": "$19 за ночь",
                        "price": "$19",
                        "qualifier": "ночь",
                        "concatQualifierLeft": false,
                        "trailingContent": null
                    },
                    "secondaryLine": {
                        "__typename": "BasicDisplayPriceLine",
                        "displayComponentType": "BASIC_DISPLAY_PRICE_LINE",
                        "accessibilityLabel": "Всего $58",
                        "price": "Всего $58",
                        "trailingContent": null
                    },
                    "explanationData": {
                        "__typename": "DisplayPriceExplanationData",
                        "title": "Разбивка цены",
                        "priceDetails": [
                            {
                                "__typename": "DisplayPriceExplanationLineGroup",
                                "displayComponentType": "DISPLAY_PRICE_EXPLANATION_LINE_GROUP",
                                "items": [
                                    {
                                        "__typename": "DefaultExplanationLineItem",
                                        "displayComponentType": "DEFAULT_EXPLANATION_LINE_ITEM",
                                        "description": "$17 x 3 ночи",
                                        "priceString": "$50",
                                        "explanationData": null
                                    },
                                    {
                                        "__typename": "DefaultExplanationLineItem",
                                        "displayComponentType": "DEFAULT_EXPLANATION_LINE_ITEM",
                                        "description": "Сбор за услуги Airbnb",
                                        "priceString": "$8",
                                        "explanationData": null
                                    }
                                ],
                                "renderBorderTop": false,
                                "collapsable": null
                            }
                        ]
                    },
                    "explanationDataDisplayPosition": "SECONDARY_LINE",
                    "explanationDataDisplayPriceTriggerType": null,
                    "layout": "ROW_WITH_SEPARATOR"
                },
                "totalPriceDisclaimer": null,
                "totalPriceWithoutDiscount": null,
                "weeklyPriceFactor": null
            },
            "luxuryInfo": null,
            "verified": {
                "__typename": "ExploreVerified",
                "badgeSecondaryText": "Проверено",
                "badgeText": "Plus",
                "enabled": false,
                "kickerBadgeType": "filled"
            },
            "verifiedCard": false
        }
        '''
        actual = normalize(json.loads(d))
        expected = {'listing_avgRating': 4.64, 'listing_businessHostLabel': None,
                    'listing_contextualPicturesPageInfo_hasNextPage': True,
                    'listing_contextualPicturesPageInfo_endCursor': 'NQ==', 'listing_id': '593482590454706058',
                    'listing_isNewListing': False, 'listing_isSuperhost': False,
                    'listing_kickerContent_kickerBadge': None, 'listing_kickerContent_textColor': None,
                    'listing_lat': 38.43808, 'listing_listingObjType': 'REGULAR', 'listing_lng': 27.146795,
                    'listing_localizedDistanceText': None, 'listing_locationTitle': None,
                    'listing_mainSectionMessage_body': 'Это жилье обычно забронировано.',
                    'listing_mainSectionMessage_bodyType': None,
                    'listing_mainSectionMessage_headline': 'Редкая находка',
                    'listing_mainSectionMessage_iconType': None, 'listing_mainSectionMessage_type': 'occupancy_rate',
                    'listing_name': 'Альтернативная квартира в Альсанчаке', 'listing_pdpType': 'MARKETPLACE',
                    'listing_pdpUrlType': 'ROOMS', 'listing_personCapacity': 2, 'listing_relaxedFilterLabels': None,
                    'listing_reviewsCount': 22, 'listing_roomTypeCategory': 'private_room', 'listing_roomTypeId': None,
                    'listing_showPhotoSwipeIndicator': None, 'listing_summary': None, 'listing_tierId': 0,
                    'listing_titleLocale': 'ru', 'listing_avgRatingLocalized': '4,64 (22)',
                    'listing_avgRatingA11yLabel': 'Средний рейтинг: 4,64 из 5. Отзывов: 22',
                    'listing_structuredContent_secondaryLine': None, 'listing_title': 'Отдельная комната, Konak',
                    'listingParamOverrides': None, 'pricingQuote_applicableDiscounts': None,
                    'pricingQuote_barDisplayPriceWithoutDiscount': None, 'pricingQuote_canInstantBook': None,
                    'pricingQuote_displayRateDisplayStrategy': None, 'pricingQuote_monthlyPriceFactor': None,
                    'pricingQuote_price': None, 'pricingQuote_priceDropDisclaimer': None,
                    'pricingQuote_priceString': None, 'pricingQuote_rate': None, 'pricingQuote_rateType': None,
                    'pricingQuote_rateWithoutDiscount': None, 'pricingQuote_rateWithServiceFee': None,
                    'pricingQuote_secondaryPriceString': None, 'pricingQuote_shouldShowFromLabel': False,
                    'pricingQuote_structuredStayDisplayPrice_primaryLine_displayComponentType': 'QUALIFIED_DISPLAY_PRICE_LINE',
                    'pricingQuote_structuredStayDisplayPrice_primaryLine_accessibilityLabel': '$19 за ночь',
                    'pricingQuote_structuredStayDisplayPrice_primaryLine_price': '$19',
                    'pricingQuote_structuredStayDisplayPrice_primaryLine_qualifier': 'ночь',
                    'pricingQuote_structuredStayDisplayPrice_primaryLine_concatQualifierLeft': False,
                    'pricingQuote_structuredStayDisplayPrice_primaryLine_trailingContent': None,
                    'pricingQuote_structuredStayDisplayPrice_secondaryLine_displayComponentType': 'BASIC_DISPLAY_PRICE_LINE',
                    'pricingQuote_structuredStayDisplayPrice_secondaryLine_accessibilityLabel': 'Всего $58',
                    'pricingQuote_structuredStayDisplayPrice_secondaryLine_price': 'Всего $58',
                    'pricingQuote_structuredStayDisplayPrice_secondaryLine_trailingContent': None,
                    'pricingQuote_structuredStayDisplayPrice_explanationData_title': 'Разбивка цены',
                    'pricingQuote_structuredStayDisplayPrice_explanationDataDisplayPosition': 'SECONDARY_LINE',
                    'pricingQuote_structuredStayDisplayPrice_explanationDataDisplayPriceTriggerType': None,
                    'pricingQuote_structuredStayDisplayPrice_layout': 'ROW_WITH_SEPARATOR',
                    'pricingQuote_totalPriceDisclaimer': None, 'pricingQuote_totalPriceWithoutDiscount': None,
                    'pricingQuote_weeklyPriceFactor': None, 'luxuryInfo': None,
                    'verified_badgeSecondaryText': 'Проверено', 'verified_badgeText': 'Plus', 'verified_enabled': False,
                    'verified_kickerBadgeType': 'filled', 'verifiedCard': False}
        assert actual == expected
