#!/usr/bin/python3
try:
    import gi
except ImportError:
    sys.exit("Missing pygobject")
try:
    gi.require_version('GLib', '2.0')
    gi.require_version('Gio', '2.0')
    gi.require_version('GObject', '2.0')
    gi.require_version('Gtk', '3.0')
    gi.require_version('Gdk', '3.0')
except ValueError as e:
    sys.exit("Missing dependency: {}".format(e))


from gi.repository import Gio
from gi.repository import Gtk
from pathbarcontainer import PathBarContainer

if __name__ == "__main__":
    win = Gtk.Window()
    win.connect("delete-event", Gtk.main_quit)
    pathBarContainer = PathBarContainer()
    box = Gtk.Box()
    box.set_orientation(Gtk.Orientation.HORIZONTAL)
    box.set_valign(Gtk.Align.START)
    home = Gtk.Button()
    home.set_label("Home")
    leftExpandButton = Gtk.Button()
    leftExpandButton.set_label("///")
    rightExpandButton = Gtk.Button()
    rightExpandButton.set_label("///")
    last = Gtk.Button()
    last.set_label("Tail hey")

    box.add(home)
    box.add(leftExpandButton)
    box.add(pathBarContainer)
    box.add(rightExpandButton)
    box.add(last)

    win.add (box)
    win.show_all()

    Gtk.main()
