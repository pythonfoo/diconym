__author__ = 'oerb'
"""
inspired by
http://code.activestate.com/recipes/52266-multilistbox-tkinter-widget/

a MultiListBox with Filter
"""
from Tkinter import *

class Multilistbox(Frame):
    """
    tkInter MultiListBox


    takes two Arguments:
    master = Tkinter.Tk  Main Window/Widget
    lists = Inherits the Header Config Tuple ( Name as String , width as Int )

    """
    def __init__(self, master, **args):  # old: ,lists)
        """

        """
        self._master = None
        self.master = master
        self._labellist = {}
        self._text = "default"
        if "name" in args:
            if isinstance(args["name"], str):
                self._text = args["name"]

        # self.show(self.master, lists)


    @property
    def master(self):
        # Type Tkinter.Tk
        if self._master:
            return self._master
        else:
            raise AttributeError

    @master.setter
    def master(self, value):
        if isinstance(value, Tk):
            self._master = value
        else:
            raise TypeError

    def show(self):
        master = self.master
        Frame.__init__(self, master)
        self.lists = []
        sortedlabellist = self._get_sorted_labellist()
        for label in sortedlabellist:
            frame = Frame(self)
            frame.pack(side=LEFT, expand=YES, fill=BOTH)
            Label(frame, text=label.text, borderwidth=1, relief=RAISED, fg=label.text_color, bg=label.header_color).pack(fill=X)
                                        # TODO config Property borderwith, relief
            lb = Listbox(frame, width=label.width, borderwidth=0, selectborderwidth=0,
                 relief=FLAT, exportselection=FALSE)
                                        # TODO config Property borderwidth, selectborderwidth, relief, exportselection
            lb.pack(expand=YES, fill=BOTH)
            self.lists.append(lb)
            lb.bind('<B1-Motion>', lambda e, s=self: s._select(e.y))
            lb.bind('<Button-1>', lambda e, s=self: s._select(e.y))
            lb.bind('<Leave>', lambda e: 'break')
            lb.bind('<B2-Motion>', lambda e, s=self: s._b2motion(e.x, e.y))
            lb.bind('<Button-2>', lambda e, s=self: s._button2(e.x, e.y))
        frame = Frame(self); frame.pack(side=LEFT, fill=Y)
        Label(frame, borderwidth=1, relief=RAISED).pack(fill=X)
        sb = Scrollbar(frame, orient=VERTICAL, command=self._scroll)
        sb.pack(expand=YES, fill=Y)
        self.lists[0]['yscrollcommand']=sb.set

    def append_label(self, multilistbox_label):
        """
        Mulitlistbox_label has to be instantiated
        """
        if isinstance(multilistbox_label, Multilistbox_label):
            self._labellist[multilistbox_label.name]=multilistbox_label
        else:
            raise TypeError

    def _get_sorted_labellist(self):
        """
        returns a List of Multilistbox_label Objects sorted by Position
        """
        self._labelkeylist = []
        for label in self._labellist.values():
            self._labelkeylist.append((label.name, label.position))

        sorted_labelkeylist=sorted( self._labelkeylist, key=lambda position: position[1])
        sortedlist = [] # sorted list of Multilistbox_label Objects

        for label in sorted_labelkeylist:
            sortedlist.append(self._labellist[label[0]])

        return sortedlist



    def _select(self, y):
        row = self.lists[0].nearest(y)
        self.selection_clear(0, END)
        self.selection_set(row)
        return 'break'

    def _button2(self, x, y):
        for l in self.lists: l.scan_mark(x, y)
        return 'break'

    def _b2motion(self, x, y):
        for l in self.lists: l.scan_dragto(x, y)
        return 'break'

    def _scroll(self, *args):
        for l in self.lists:
            apply(l.yview, args)

    def curselection(self):
        return self.lists[0].curselection()

    def delete(self, first, last=None):
        for l in self.lists:
            l.delete(first, last)

    def get(self, first, last=None):
        result = []
        for l in self.lists:
            result.append(l.get(first,last))
        if last: return apply(map, [None] + result)
        return result

    def index(self, index):
        self.lists[0].index(index)

    def insert(self, index, *elements):
        for e in elements:
            i = 0
            for l in self.lists:
                l.insert(index, e[i])
                i = i + 1

    def size(self):
        return self.lists[0].size()

    def see(self, index):
        for l in self.lists:
            l.see(index)

    def selection_anchor(self, index):
        for l in self.lists:
            l.selection_anchor(index)

    def selection_clear(self, first, last=None):
        for l in self.lists:
            l.selection_clear(first, last)

    def selection_includes(self, index):
        return self.lists[0].selection_includes(index)

    def selection_set(self, first, last=None):
        for l in self.lists:
            l.selection_set(first, last)


class Multilistbox_label(object):
    """
    Define a Label for Mulitlistbox

    @name = Tablefield Name
    @text = Label Text
    @text_colour = set Text Colour
    @header_colour = set Label Colour
    @is_filter = set Lable as Filterbutton
    @width = set width
    @position = set Position
    """
    def __init__(self, labelname):
        # private Properties pleas do not use them
        self._name = ""
        self._text = ""
        self._text_color = "black"
        self._header_color = "grey"
        self._is_filter = False
        self._width = 10
        self._position = 1
        # set Name
        self.name = labelname

        # TODO: Textbase Filter above Header as Inputboxes

    @property
    def name(self):
        if self._name:
            return self._name
        else:
            raise NameError

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value
        else:
            raise TypeError

    @property
    def text(self):
        if self._text:
            return self._text
        else:
            raise NameError

    @text.setter
    def text(self, value):
        if isinstance(value, str):
            self._text = value
        else:
            raise TypeError


    @property
    def text_color(self):
        return self._text_color

    @text_color.setter
    def text_color(self, value):
        if isinstance(value, str): # TODO Color Type Proof
            self._text_color = value
        else:
            raise TypeError

    @property
    def header_color(self):
        return self._header_color

    @header_color.setter
    def header_color(self, value):
        if isinstance(value, str):
            self._header_color = value
        else:
            raise TypeError

    @property
    def is_filter(self):
        return self._is_filter

    @is_filter.setter
    def is_filter(self, value):
        if isinstance(value, bool):
            self._is_filter = value
        else:
            raise TypeError

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if isinstance(value, int):
            self._width = value
        else:
            raise TypeError

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        if isinstance(value, int):
            self._position = value
        else:
            raise TabError

if __name__ == '__main__':
    tk = Tk()
    Label(tk, text='MultiListbox_by_Oerb').pack()

    mlb = Multilistbox(tk) # instantiate Multilistbox
    # define the Header Label
    label1 = Multilistbox_label("label1")
    label1.position = 1
    label1.width = 40
    label1.text = "Subject"
    label1.header_color = "red"
    label1.text_color = "blue"
    label1.is_filter = True
    mlb.append_label(label1)

    label2 = Multilistbox_label("label2")
    label2.position = 2
    label2.width = 20
    label2.text = "Sender"
    mlb.append_label(label2)

    label3 = Multilistbox_label("label3")
    label3.position = 3
    label3.width = 10
    label3.text = "Date"
    mlb.append_label(label3)

    label4 = Multilistbox_label("label4")
    label4.position = 4
    label4.width = 30
    label4.text = "User"
    mlb.append_label(label4)
    mlb.show()
    # TODO: Dynamische Laenge Spalten pruefen
    for i in range(1000):
        mlb.insert(END, ('Important Message: %d' % i, 'John Doe', '10/10/%04d' % (1900+i),'by Oerb'))
    mlb.pack(expand=YES,fill=BOTH)
    tk.mainloop()

# TODO: Lable needs: Image, Filter Files
# TODO: List needs Stripes so it needs something for Colours
# TODO: List needs coloured character