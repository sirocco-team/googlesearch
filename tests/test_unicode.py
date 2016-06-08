# -*- coding: utf-8 -*-
from googlesearch import GoogleSearch


def test_top_results():
    gs = GoogleSearch('george osborne hinkley point')
    res = gs.top_results()
    assert any((r['titleNoFormatting'].startswith('George Osborne presses')
                for r in res))


def test_top_results_unicode():
    gs = GoogleSearch('乔治·奥斯本欣克利点')
    res = gs.top_results()
    assert any((r['url'] == 'http://www.bbc.com/zhongwen/simp/uk/2015/10/151021_analysis_uk_xi_visit_nuclear_deal' for r in res))
