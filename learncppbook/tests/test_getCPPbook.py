import learncppbook.getCPPbook as getCPPbook


def test_fail():
    assert getCPPbook.JinjaTemplateMaker.OPENING_TAG == """{% extends "template.html" %}"""
