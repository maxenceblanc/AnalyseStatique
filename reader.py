#! /usr/bin/env python
#-*- coding: utf-8 -*-

########################
# Python 3.7
# Author : Maxence Blanc - https://github.com/maxenceblanc
########################

# IMPORTS

# CUSTOM IMPORTS


''' TO DO LIST
'''


''' NOTES
'''

####################################################
###################| CLASSES |######################
####################################################

# class Graph():

#     def __init__():
#         pass

class Block():

    def __init__(id):

        self.id = id

        self.expressions = []

        self.block_before = []
        self.block_after = []

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
        data = [line.rstrip() for line in graph_file.readlines()]
        print(data)


    block_list = []

    for line in data:
        pass

    return block_list


def addNetwork(data, blocks):
    """  TODO

    INPUTS: 
    OUTPUT:
    """ 
    pass

####################################################
###################| CONSTANTS |####################
####################################################

GRAPH_FILE = "graphs/graph.json"

####################################################
####################| PROGRAM |#####################
####################################################

if __name__ == '__main__':

    block_list = parseFile(GRAPH_FILE)