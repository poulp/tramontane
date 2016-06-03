# coding: utf-8


class MCategoryItem:

    def __init__(self, text):
        self.label = text

    def get_label(self):
        return self.label


class MCategories:

    def __init__(self, items):
        self.items = items
