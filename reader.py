#! /usr/bin/env python
#-*- coding: utf-8 -*-

########################
# Python 3.7
# Author : Maxence Blanc - https://github.com/maxenceblanc
########################

# IMPORTS
import json

# CUSTOM IMPORTS


''' TO DO LIST
'''


''' NOTES
'''

####################################################
###################| CLASSES |######################
####################################################

class Graph():
    """ Object representation of the graph.

    The methods that have the same name as in the Block() class are utility methods applied
    to the block marked as 'current' in the graph.

    """

    def __init__(self, block_dict):
        
        self.blocks = block_dict

        # Initialization
        self.current = None # Block being currently focused, ex: "B1"

        self.expr_collection = list(set([i for b in self.blocks for inst in self.blocks[b].instructions for i in inst[1::]]))
        # ... extra vars for the algorithm


    def __repr__(self):
        chaine = "\n".join([self.blocks[block_id].__repr__() for block_id in self.blocks])
        return chaine

    def getCurrentBlock(self):
        return self.blocks[self.current]

    def instructions(self):
        """  Gets the instructions of the current block.
        """ 
        return self.blocks[self.current].instructions

    def pred(self):
        """ Gets pred of the current block.
        """ 
        return self.blocks[self.current].pred

    def succ(self):
        """ Gets succ of the current block.
        """ 
        return self.blocks[self.current].succ

    def varIsRedefined(self, var):
        """ Calls the varIsRedefined() on the current block.
        """
        return self.blocks[self.current].varIsRedefined(var)

    def getExpressionContain(self, var):
        """ Get all the expression that contain var
        """
        return [expr for expr in self.expr_collection if var in expr]


    def hasExpression(self, expression):
        """ Calls the hasExpression() on the current block.
        """
        return self.blocks[self.current].hasExpression(expression)
        
    def getAllExpressionSelBlock(self):
        return self.blocks[self.current].getAllExpression()

    def getAllRedefinedVarSelBlock(self):
        return self.blocks[self.current].getAllRedefinedVar()

class Block():

    def __init__(self, id, instructions=[], pred=[], succ=[]):

        self.id = id

        self.instructions = instructions

        self.pred = pred
        self.succ = succ
        self.OUT = set()
        self.IN = set()
        self.KILL = set()
        self.GEN = set()

    def __repr__(self):
        chaine = f"Block {self.id}\nInstructions:\n"
        for instruction in self.instructions:
            chaine += f"    {instruction}\n"
        chaine += f"Before: {self.block_before}\nAfter:  {self.block_after}\n"
        return chaine

    def varIsRedefined(self, var):
        """ Checks if blocks has instructions containing a given variable
        and returns these instructions.
        """

        res = [instruction for instruction in self.instructions if var in instruction[0]]

        return res

    def hasExpression(self, expression):
        """ Checks if the block contains a given expression.
        """ 

        for instruction in self.instructions:
            if instruction[1] == expression: # On suppose qu'une expression a+b ne sera jamais écrite b+a
                return True

        return False

    def getAllExpression(self):
        """expressions used before any operands being redefined in n
        """
        redef = []
        l = []

        for inst in self.instructions:
            for i in inst[1::]:
                t = True
                for j in redef:
                    if j in i:
                        t = False
                if(t):
                    l.append(i)
            redef.append(inst[0])

        return l

    def getAllRedefinedVar(self):
        """operande writed in N
        """
        redef = []
        l = []

        # for inst in self.instructions:
        #     for i in inst[1::]:
        #         for j in redef:
        #             if j in i:
        #                 l.append(i)
        #     redef.append(inst[0])

        return [instr[0] for instr in self.instructions]

    def getAllRedefinedVar2(self):
        """expressions whose operands are redefined in n
                """
        redef = []
        l = []

        for inst in self.instructions:
            for i in inst[1::]:
                for j in redef:
                    if j in i:
                        l.append(i)
            redef.append(inst[0])
        return l
####################################################
##################| FUNCTIONS |#####################
####################################################

def parseFile(filename: str):
    """  reads a graph file, returns the graph in a data structure.

    INPUTS:     
            graph filename
    OUTPUT:

    """ 
    
    with open(filename) as graph_file:
        data =  json.load(graph_file)


    block_dict = {}

    for block_id in data:
        new_block = Block(block_id, data[block_id]["instructions"], data[block_id]["pred"], data[block_id]["succ"])
        block_dict[block_id] = new_block


    return block_dict



####################################################
####################| PROGRAM |#####################
####################################################

if __name__ == '__main__':

    # Parses graph file and get an object representation of the graph described
    block_dict = parseFile(GRAPH_FILE)
    graph = Graph(block_dict)

    # Printing the graph
    # print(graph)

    # Example : Checks which expressions of B8 contain variable "d"
    # graph.blocks["B8"].varIsRedefined("d")

    graph.current = "B7"
    print(graph.instructions())
    print(graph.varIsRedefined("e"))
    print(graph.hasExpression("e+1"))
