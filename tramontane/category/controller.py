# coding: utf-8

import json

CONF_FILE = 'conf.json'

class Controller:

    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.init_items()

    def init_items(self):
        with open('conf.json') as data_file:
            data = json.load(data_file)

        self.build_node(None, data)


    def build_node(self, treeiter, item):
        items = item.get('items', [])

        for item in items:
            new_treeiter = self.model.append(treeiter, [item['name']])
            self.build_node(new_treeiter, item)