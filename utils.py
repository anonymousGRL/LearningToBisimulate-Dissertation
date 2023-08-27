import numpy as np
import networkx as nx
from z3 import *

def extract_quotient(adj_matrix):
    G = nx.DiGraph()
    r = np.array([[as_bool(e) for e in r] for r in adj_matrix])
    for i in range(len(r)):
        for j in np.nonzero(r[i])[0].tolist():
            G.add_edge('%s' % i, '%s' % j)
    return G

def as_real(x):
    return float(x.numerator_as_long()) / float(x.denominator_as_long())

def as_bool(x):
    try:
        return bool(x)
    except:
        return 0

def test(x):
    return 1

def decimal(a):
    if type(a) == float:
        return a
    dec = simplify(a).as_decimal(10)
    if dec[-1] == "?":
        return float(dec[:-1])
    else: 
        return float(dec)
