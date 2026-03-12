"""
-------------------------------------------------------
Assignment 8, Functions
-------------------------------------------------------
Author:  Jack Sherwood
ID:             1691168645
Email:        sher6864@mylaurier.ca
__updated__ = Mar 11, 2026
-------------------------------------------------------
"""
from Letter import Letter

def do_comparisons(file_variable, bst):
    """
    -------------------------------------------------------
    Retrieves every letter in file_variable from bst. Generates
    comparisons in bst objects. Each Letter object in bst contains
    the number of comparisons found by searching for that Letter
    object in file_variable.
    Use: do_comparisons(file_variable, bst)
    -------------------------------------------------------
    Parameters:
        file_variable - the already open file containing data to evaluate (file)
        bst - the binary search tree containing 26 Letter objects
            to retrieve data from (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    # Zeroes out all comparison values in tree nodes
    for node in bst:
        node.comparisons = 0

    # your code here
    for line in file_variable:
        line=clean_line(line)
        for char in line:
            _ = bst.retrieve(Letter(char))
            
    

def clean_line(line):
    """
    -------------------------------------------------------
    Takes in a string and removes all non letter characters
    as well as capitalizing all letters
    Use: clean_line=clean_line(line)
    -------------------------------------------------------
    Parameters:
        line - line of text (string)
    Returns:
        clean_line - cleaned line of text (string)
    -------------------------------------------------------
    """
    
    clean_line=""
    for char in line:
        if char.isalpha():
            clean_line+=char.upper()
    
    return clean_line

def comparison_total(bst):
    """
    -------------------------------------------------------
    Sums the comparison values of all Letter objects in bst.
    Use: total = comparison_total(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        total - the total of all comparison fields in the bst
            Letter objects (int)
    -------------------------------------------------------
    """
    total=0
    
    letters=bst.inorder()
    for letter in letters:
        total+=letter.comparisons
    return total

def letter_table(bst):
    """
    -------------------------------------------------------
    Prints a table of letter counts for each Letter object in bst.
    Use: letter_table(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    
    letter_count = 0
    letters=bst.inorder()
    for letter in letters:
        letter_count+=letter.count
    
    
    print("Letter Count/Percent Table")
    print("")
    print(f"Total Count: {letter_count:,}")
    print("")
    print("Letter  Count       %")
    print("---------------------")
    
    for letter in letters:
        percentage = (letter.count/letter_count)*100
        print(f"{letter.letter:>5} {letter.count:>7,} {percentage:>6.2f}%")
    
    
        
    
    


    

        
