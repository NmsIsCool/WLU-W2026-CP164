"""
-------------------------------------------------------
Assignment 9 Functions
-------------------------------------------------------
Author:  Jack Sherwood
ID:             1691168645
Email:        sher6864@mylaurier.ca
__updated__ = '2026-03-18'
-------------------------------------------------------
"""

from Word import Word

def insert_words(fv, hash_set):
    """
    -------------------------------------------------------
    Retrieves every Word in file_variable and inserts into
    a Hash_Set. Each Word object in hash_set contains the number
    of comparisons required to insert that Word object from
    file_variable into hash_set.
    Use: insert_words(file_variable, hash_set)
    -------------------------------------------------------
    Parameters:
        fv - the already open file containing data to evaluate (file)
        hash_set - the Hash_Set to insert the words into (Hash_Set)
    Returns:
        None
    -------------------------------------------------------
    """
    
    line=clean_line(fv.readline())
    while line:
        #Tokenize Line
        words = line.split(" ")
        
        #load tokens into hash_set
        for word in words:
            if word:
                #print(word)
                hash_set.insert(Word(word))
            
        #Get next line:
        line=clean_line(fv.readline())
    
    return
        
        
    
def clean_line(line):
    """
    -------------------------------------------------------
    Takes in a string and removes all non letter characters
    as well as capitalizing all letters
    Use: cleaned=clean_line(line)
    -------------------------------------------------------
    Parameters:
        line - line of text (string)
    Returns:a
        cleaned - cleaned line of text (string)
    -------------------------------------------------------
    """
    
    cleaned=""
    for char in line:
        if char.isalpha():
            cleaned+=char.lower()
        elif char.isspace():
            cleaned+=" "
    
    return cleaned

def comparison_total(hash_set):
    """
    -------------------------------------------------------
    Sums the comparison values of all Word objects in hash_set.
    Use: total, max_word = comparison_total(hash_set)
    -------------------------------------------------------
    Parameters:
        hash_set - a hash set of Word objects (Hash_Set)
    Returns:
        total - the total of all comparison fields in the Hash_Set
            Word objects (int)
        max_word - the word having the most comparisons (Word)
    -------------------------------------------------------
    """
    
    max_word=None
    total=0
    
    for item in hash_set:
        total+=item.comparisons
        if max_word is None or item.comparisons >= max_word.comparisons :
            max_word = item
    
    return total, max_word
            
            
            
    
    
    
    

