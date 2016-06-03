# coding: utf-8


class Controller:

    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.set_items()

    def set_items(self):
        self.view.set_list(self.model.items)
