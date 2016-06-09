# -*- coding: utf-8 -*-
from googlesearch import GoogleSearch


def test_top_results():
    gs = GoogleSearch('george osborne hinkley point')
    res = gs.top_results()
    assert any((r['titleNoFormatting'].startswith('George Osborne presses')
                for r in res))


"""  Damn !!
{"responseData": null, "responseDetails": "The Google Web Search API is no
longer available. Please migrate to the Google Custom Search API
(https://developers.google.com/custom-search/)", "responseStatus": 403}
"""