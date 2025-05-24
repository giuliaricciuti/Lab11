import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self.nodes = []
        self.archi = []

    def buildGraph(self, year, color):
        self.nodes = DAO.getProductsByColor(color)
        self._idMapProd = {}
        for product in self.nodes:
            self._idMapProd[product.Product_number] = product
        self._graph.add_nodes_from(self.nodes)
        for n1 in self.nodes:
            for n2 in self.nodes:
                if n1!=n2:
                    count = DAO.getSameDaySales(n1, n2, year)
                    if count[0] > 0:
                        self._graph.add_edge(n1, n2, weight=count)


    def getAllColours(self):
        return DAO.getAllColours()


