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

class Block():

    def __init__(self, id, instructions=[], block_before=[], block_after=[]):

        self.id = id

        self.instructions = instructions

        self.block_before = block_before
        self.block_after = block_after

    def __repr__(self):
        chaine = f"Block {self.id}\nInstructions:\n"
        for instruction in self.instructions:
            chaine += f"    {instruction}\n"
        chaine += f"Before: {self.block_before}\nAfter:  {self.block_after}\n"
        return chaine

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
###################| CONSTANTS |####################
####################################################

GRAPH_FILE = "graphs/graph.json"

####################################################
####################| PROGRAM |#####################
####################################################

if __name__ == '__main__':

    block_dict = parseFile(GRAPH_FILE)

    for block_id in block_dict:
        print(block_id, block_dict[block_id])