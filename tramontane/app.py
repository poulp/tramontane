# coding: utf-8
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
gi.require_version('GdkPixbuf', '2.0')

from gi.repository import Gio, GObject, Gtk

from tramontane.category.controller import Controller
from tramontane.category.model import MCategories
from tramontane.category.view import VCategoriesListView


class TramontaneGtkApplicationWindow(Gtk.ApplicationWindow):

    default_title = "Tramontane"
    default_width = 800
    default_height = 600

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        model = MCategories()
        view = VCategoriesListView()
        controller = Controller(model=model, view=view)

        self.set_title(TramontaneGtkApplicationWindow.default_title)
        self.set_default_size(
            TramontaneGtkApplicationWindow.default_width,
            TramontaneGtkApplicationWindow.default_height
        )

        hbox = Gtk.HBox()
        hbox.pack_start(view.widget, True, True, 0)
        # categories = CategoriesListView(Categories(items=[CategoryItem("New"), CategoryItem("Starred"), Categories(items=[CategoryItem("New"), CategoryItem("Starred")])]))
        # hbox.pack_start(categories.get_view(), True, True, 0)
        # categories = CategoriesListView(Categories(items=[]))
        # hbox.pack_start(categories.get_view(), True, True, 0)
        self.add(hbox)


class TramontaneApp(Gtk.Application):

    def __init__(self, **kwargs):
        super().__init__(application_id="github.io.tramontane", **kwargs)
        self.window = None

    def do_startup(self):
        Gtk.Application.do_startup(self)

        action = Gio.SimpleAction.new("quit", None)
        action.connect("activate", self.on_quit)
        self.add_action(action)

    def do_activate(self):
        if not self.window:
            # Main window
            self.window = TramontaneGtkApplicationWindow(application=self)
            self.window.show_all()
        self.window.present()

    def on_quit(self):
        self.quit()
