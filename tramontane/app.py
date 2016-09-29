# coding: utf-8

# Import from gi
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
gi.require_version('GdkPixbuf', '2.0')
from gi.repository import Gio, GObject, Gtk

# Import from tramontane
from tramontane.components import FluxComp, FeedComp
from tramontane.cache import Cache


class TramontaneGtkApplicationWindow(Gtk.ApplicationWindow):

    default_title = "Tramontane"
    default_width = 800
    default_height = 600

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.set_title(TramontaneGtkApplicationWindow.default_title)
        self.set_default_size(
            TramontaneGtkApplicationWindow.default_width,
            TramontaneGtkApplicationWindow.default_height
        )

        # Main box
        hbox = Gtk.HBox()
        application = kwargs.get('application')
        cache = application.cache

        # Flux component
        flux_component = FluxComp()
        # Signals
        cache.connect('cache_changed', flux_component.on_cache_changed)
        # Add to main view
        hbox.pack_start(flux_component.view.widget, True, True, 0)

        # Feed list component
        feed_list_component = FeedComp()
        # Signals
        cache.connect('cache_changed', feed_list_component.on_cache_changed)
        flux_component.view.widget.connect('row-activated', feed_list_component.on_category_changed)
        flux_component.view.widget.get_selection().connect("changed", feed_list_component.on_selection)
        # Add to main view
        hbox.pack_start(feed_list_component.view.widget, True, True, 0)

        # Add box to main window
        self.add(hbox)


class TramontaneApp(Gtk.Application):

    def __init__(self, **kwargs):
        super().__init__(application_id="github.io.tramontane", **kwargs)
        self.window = None
        # Cache
        self.cache = Cache()

    def do_startup(self):
        Gtk.Application.do_startup(self)

        # Quit action
        action_quit = Gio.SimpleAction.new("quit", None)
        action_quit.connect("activate", self.on_quit)
        self.add_action(action_quit)

        # Refresh all action
        action_refresh_all = Gio.SimpleAction.new("refresh_all", None)
        action_refresh_all.connect("activate", self.on_refresh_all)
        self.add_action(action_refresh_all)

        # Menu
        builder = Gtk.Builder.new_from_file("tramontane/menu.xml")
        self.set_app_menu(builder.get_object("app-menu"))

    def do_activate(self):
        if not self.window:
            # Main window
            self.window = TramontaneGtkApplicationWindow(application=self)
            self.window.show_all()
        self.window.present()

    def on_quit(self, action, extra):
        self.quit()

    def on_refresh_all(self, action, param):
        self.cache.refresh()
