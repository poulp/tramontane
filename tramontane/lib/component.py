# coding: utf-8


class Component:

    class Meta:
        view = None

    def __init__(self):
        if hasattr(self.Meta, 'view') and self.Meta.view:
            self.view = self.Meta.view()
        else:
            self.view = self.get_view()

    def get_view(self):
        raise NotImplementedError


class ModelComponent(Component):

    class Meta:
        model = None

    def __init__(self):
        super().__init__()
        if hasattr(self.Meta, 'model') and self.Meta.model:
            self.model = self.Meta.model()
        else:
            self.model = self.get_model()

    def get_model(self):
        raise NotImplementedError


class ListComponent(ModelComponent):

    def __init__(self):
        super().__init__()
        self.view.widget.bind_model(self.model, self.view.get_item_widget)