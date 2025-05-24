from database.DAO import DAO
from model.model import Model

m = Model()
m.buildGraph('Clear')
g = m._graph
print (g.number_of_nodes())