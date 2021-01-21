#! /usr/bin/env python
from AnalyseStatique import reader

GRAPH_FILE = "graphs/graph.json"
block_dict = reader.parseFile(GRAPH_FILE)
graph = reader.Graph(block_dict)

# %%
# Construct Kill and Gen sets for each blocks
for block in graph.blocks:
    graph.current = graph.blocks[block].id
    b = graph.getCurrentBlock()

    # https://www.seas.upenn.edu/~mhnaik/edu/cis700/lessons/dataflow_analysis.pdf
    # Gen = every expression of the program
    b.GEN = set(b.getAllExpression())
    # kill = every expression where a variable is redefined in b
    b.KILL = set([expr for var in b.getAllRedefinedVar() for expr in graph.getExpressionContain(var)])

    # Set In and Out for each nodes
    b.IN = [set(graph.expr_collection)]
    b.OUT = [set(graph.expr_collection)]

stopCrit = True

while stopCrit:

    for block in graph.blocks:
        graph.current = block
        b = graph.getCurrentBlock()
        #Get the list of IN in B successors
        inlist = [graph.blocks[s].IN[-1] for s in graph.succ()]
        # OUTb(n) = Interesection (INb_succ(n-1))
        b.OUT.append(set.intersection(*inlist) if inlist else set())
        # INb(n) = (OUTb(n) - KILLb) U GENb
        b.IN.append(b.GEN.union(b.OUT[-1].difference(b.KILL)))


    # When every out and in stay the same as the precedent phase
    stopCrit = False
    for block in graph.blocks:
        graph.current = graph.blocks[block].id
        b = graph.getCurrentBlock()
        if b.IN[-1] != b.IN[-2] or b.OUT[-1] != b.OUT[-2]:
            stopCrit = True

# Print last out variable
for block in graph.blocks:
    graph.current = block
    b = graph.getCurrentBlock()
    print(f"Block %s : " % block + ",".join(b.OUT[-1]))
