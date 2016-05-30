# coding: utf-8


class CategoryItem:

    def __init__(self, text):
        self.label = text

    def get_label(self):
        return self.label


class Categories:

    def __init__(self):
        self.items = [CategoryItem("New"), CategoryItem("Starred")]
