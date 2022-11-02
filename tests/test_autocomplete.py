from airbnbcrawl import autocomplete


class Test_get_place_id:
    def test_ok(self):
        assert autocomplete.get_place_id("antalya turkey") == "ChIJwa2t3a6awxQRMy7j-XOfxpU"
