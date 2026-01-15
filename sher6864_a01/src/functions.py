"""
-------------------------------------------------------
Assignment 1, Functions
-------------------------------------------------------
Author:  Jack Sherwood
ID:             1691168645
Email:        sher6864@mylaurier.ca
__updated__ = Jan 6, 2026
-------------------------------------------------------
"""
#Imports

#Constants
ALPHABET="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def clean_list(values):
    """
    -------------------------------------------------------
    Removes all duplicate values from a list: values contains
    only one copy of each of its integers. The order of values
    must be preserved.
    Use: clean_list(values)
    -------------------------------------------------------
    Parameters:
        values - a list of integers (list of int)
    Returns:
        None
    -------------------------------------------------------
    """
    
    seen_values=[]
    
    i=0
    
    while i < len(values):
        if(values[i] in seen_values):
            values.pop(i)
        else:
            seen_values.append(values[i])
            i+=1
    return

def list_subtraction(minuend, subtrahend):
    """
    -------------------------------------------------------
    Alters the contents of minuend so that it does not contain
    any values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are removed from the first list.
    Use: list_subtraction(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to not include in difference (list)
    Returns:
        None
    ------------------------------------------------------
    """
    
    i=0
    while i<len(minuend):
        if(minuend[i] in subtrahend):
            minuend.pop(i)
        else:
            i+=1
    return

def dsmvwl(string):
    """
    -------------------------------------------------------
    Disemvowels a string. out contains all the characters in s
    that are not vowels. ('y' is not considered a vowel.) Case is preserved.
    Use: out = dsmvwl(string)
    -------------------------------------------------------
    Parameters:
       string - a string (str)
    Returns:
       out - string with the vowels removed (str)
    -------------------------------------------------------
    """
    
    vowels="aeiou"
    
    out=""
    for i in range (len(string)):
        if(string[i].lower() not in vowels):
            out+=string[i]
    
    return out

def file_analyze(fv):
    """
    -------------------------------------------------------
    Analyzes the characters in a file.
    The contents of the file must be unchanged:
    Do not strip() the lines.
    Use: upp, low, dig, whi, rem = file_analyze(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file reference (file variable)
    Returns:
        upp - the number of uppercase letters in the file (int)
        low - the number of lowercase letters in the file (int)
        dig - the number of digits in the file (int)
        whi - the number of whitespace characters in the file (int)
        rem - the number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    
    line=fv.readline()
    
    upp, low, dig, whi, rem=0,0,0,0,0
    
    while line:
        for i in range (len(line)):
            if line[i].isalpha() and line[i].isupper():
                upp+=1
            elif line[i].isalpha() and line[i].islower():
                low+=1
            elif line[i].isnumeric():
                dig+=1
            elif line[i].isspace():
                whi+=1
            else:
                rem+=1
        line=fv.readline()
            
    return upp, low, dig, whi, rem

def find_subs(string, sub):
    """
    -------------------------------------------------------
    Finds the indices of the locations of sub within string,
        left to right. Already used characters are ignored.
    Use: locations = find_subs(string, sub)
    -------------------------------------------------------
    Parameters:
        string - a string to evaluate (str)
        sub - a substring to locate in string (str)
    Returns:
        locations - an ordered list of the indices of the locations
            of sub within string (list of int)
    -------------------------------------------------------
    """
    
    locations = []
    i = 0
    length = len(sub)

    while i <= len(string) - length:
        if string[i:i+length] == sub:
            locations.append(i)
            i += length        
        else:
            i += 1

    return locations

def is_leap_year(year):
    """
    -------------------------------------------------------
    Leap year determination.
    Use: leap_year = is_leap_year(year)
    -------------------------------------------------------
    Parameters:
        year - year to determine if it is a leap year (int > 0)
    Returns:
        leap_year - True if year is a leap year, False otherwise (boolean)
    -------------------------------------------------------
    """
    leap_year=False
    if (year % 4 ==0):
        if(year % 100 == 0):
            if(year % 400 == 0):
                leap_year=True
            else:
                leap_year=False
        
            
    return leap_year

def is_palindrome(string):
    """
    -------------------------------------------------------
    Determines if s is a palindrome. Ignores case, spaces, and
    punctuation in s.
    Use: palindrome = is_palindrome(s)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -------------------------------------------------------
    """
    palindrome=False
    
    
    duplicate=""
    for i in range(len(string.strip())):
        if(string[i].isalnum):
            duplicate+=string[i].lower()
    
    if duplicate[::-1] == duplicate:
        palindrome=True
    
    return palindrome

def matrixes_multiply(a, b):
    """
    -------------------------------------------------------
    Multiplies the contents of matrixes a and b.
    If a is mxn in size, and b is nxp in size, then c is mxp.
    a and b must be unchanged.
    Use: c = matrixes_multiply(a, b)
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of int/float)
        b - a 2D list (2D list of int/float)
    Returns:
        c - the matrix multiple of a and b (2D list of int/float)
    -------------------------------------------------------
    """
    
    #I thought I was free from the clutches of linear algebra, at least for a semester, but alas...
    
    rows_a = len(a)
    cols_a = len(a[0])
    cols_b = len(b[0])

    c = []

    for i in range(rows_a):
        row = []
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += a[i][k] * b[k][j]
            row.append(total)
        c.append(row)

    return c
        
        
def substitute(string, ciphertext):
    """
    -------------------------------------------------------
    Encipher a string using the letter positions in ciphertext.
    Only letters are enciphered, and the returned string is
    in upper case.
    Use: estring = substitute(string, ciphertext):
    -------------------------------------------------------
    Parameters:
        string - string to encipher (str)
        ciphertext - ciphertext alphabet (str)
    Returns:
        estring - the enciphered string (str)
    -------------------------------------------------------
    """
    
    buffer_str=string.upper()
    
    #Assemble list where each number in the list corresponds to its alphabetical assignment
    num_list=[]
    for char in range (len(buffer_str)):
        for i in range (len(ALPHABET)):
            if buffer_str[char] == ALPHABET[i]:
                num_list.append(i)
    
    #build estring
    estring=""
    for k in range (len(num_list)):
        estring+=ciphertext[num_list[k]]
        
    return estring

def shift(string, n):
    """
    -------------------------------------------------------
    Encipher a string using a shift cipher.
    Only letters are enciphered, and the returned string is
    in upper case.
    Use: estring = shift(string, n):
    -------------------------------------------------------
    Parameters:
        string - string to encipher (str)
        n - the number of letters to shift (int)
    Returns:
        estring - the enciphered string (str)
    -------------------------------------------------------
    """
    
    #Determine letters position in alphabet, add to a list
    num_pos_list=[]
    for i in range(len(string)):
        for k in range(len(ALPHABET)):
            if string.upper()[i] == ALPHABET[k]:
                num_pos_list.append(k)
    
    #determine new letter positions based on n
    for p in range(len(num_pos_list)):
        num_pos_list[p]+=n
        if num_pos_list[p]>25:
            num_pos_list[p]=num_pos_list[p]-24
    
    #assemble estring
    estring=""
    for l in range (len(num_pos_list)):
        estring+=ALPHABET[num_pos_list[l]]
    
    return estring
                
        
        
                
    
                
                
            
    

                
            
    
        
            


            
            
