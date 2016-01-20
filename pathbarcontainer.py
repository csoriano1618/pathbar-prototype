from gi.repository import Gtk
from gi.repository import Pango

class PathBarContainer (Gtk.Container):

    def __init__(self):
        super(PathBarContainer, self).__init__()
        self.set_has_window(False)
        self._children = []
        button = Gtk.Button()
        label = Gtk.Label()
        label.set_text("heya")
        label.set_ellipsize(Pango.EllipsizeMode.MIDDLE)
        label.set_max_width_chars(6)
        button.add(label)
        revealer = Gtk.Revealer()
        revealer.add(button)
        revealer.set_parent(self)
        revealer.show_all()
        revealer.set_reveal_child(True)
        self._children.append(revealer)

        button = Gtk.Button()
        label = Gtk.Label()
        label.set_text("heya 2")
        label.set_ellipsize(Pango.EllipsizeMode.MIDDLE)
        label.set_max_width_chars(6)
        button.add(label)
        revealer = Gtk.Revealer()
        revealer.add(button)
        revealer.set_parent(self)
        revealer.show_all()
        revealer.set_reveal_child(True)
        self._children.append(revealer)

        button = Gtk.Button()
        label = Gtk.Label()
        label.set_text("heya 2")
        label.set_ellipsize(Pango.EllipsizeMode.MIDDLE)
        label.set_max_width_chars(6)
        button.add(label)
        revealer = Gtk.Revealer()
        revealer.add(button)
        revealer.set_parent(self)
        revealer.show_all()
        revealer.set_reveal_child(True)
        self._children.append(revealer)

    def do_forall(self, include_internals, callback):
        for child in self._children:
            if include_internals:
                callback(child)

    def _update_children_visibility(self, allocation):
        totalMinWidth = 0
        allocateMoreChildren = True
        childrenToAllocate = []
        sizes = []
        for child in self._children:
            if not child.is_visible():
                continue
            minWidth, natWidth = child.get_preferred_width()
            if totalMinWidth < allocation.width and allocateMoreChildren:
                child.set_child_visible(True)
                childrenToAllocate.append(child)
                totalMinWidth += minWidth
                requestedSize = Gtk.RequestedSize()
                requestedSize.minimum_size = minWidth
                requestedSize.natural_size = natWidth
                sizes.append(requestedSize)
            else:
                child.set_child_visible(False)
                allocateMoreChildren = False

        return sizes, childrenToAllocate, totalMinWidth

    def do_size_allocate(self, allocation):

        self.set_allocation(allocation)

        sizes, childrenToAllocate, totalMinWidth = self._update_children_visibility(allocation)
        extraSpace = allocation.width - totalMinWidth
        Gtk.distribute_natural_allocation(extraSpace, len(childrenToAllocate), sizes)

        x = allocation.x
        for i in range(len(childrenToAllocate)):
            childAllocation = []
            childAllocation.x = x
            childAllocation.y = allocation.y
            childAllocation.width = sizes[i].minimum_size
            childAllocation.height = allocation.height
            childrenToAllocate[i].size_allocate(childAllocation)
            x += childAllocation.width
        
