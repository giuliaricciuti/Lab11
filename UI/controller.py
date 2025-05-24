import flet as ft
import networkx as nx

from database.DAO import DAO


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listColor = []
        self._color = None
        self._year = None


    def fillDD(self, dd: ft.Dropdown):
        self._listYear = self._model.getAllColours()
        for c in self._listYear:
            dd.options.append(
                ft.dropdown.Option(text = str(c),
                on_click = self.readColor))

    def readColor(self, e):
        self._color = e.control.text


    def handle_graph(self, e):
        self._view.txtOut.controls.append(ft.Text(""))
        self._year = self._view._ddyear.value
        if self._year is None:
            self._view.txtOut.controls.append(ft.Text("No year selected!"))
            self._view.update_page()
        elif self._color is None:
            self._view.txtOut.controls.append(ft.Text("No color selected!"))
            self._view.update_page()
        else:
            self._view.txtOut.controls.append(ft.Text(f"{self._year}, {self._color}"))
            self._view.update_page()



    def fillDDProduct(self):
        pass


    def handle_search(self, e):
        pass
