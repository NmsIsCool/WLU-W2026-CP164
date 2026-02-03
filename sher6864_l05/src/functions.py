"""
------------------------------------------------------------------------
Lab 5, Functions
------------------------------------------------------------------------
Author: Jack Sherwood
ID:           169116864
Email:     sher6864@mylaurier.ca
__updated__ = '2026-02-02'
------------------------------------------------------------------------
"""

def recurse(x, y):
    """
    -------------------------------------------------------
    Recursive function - example of tree recursion.
    Use: ans = recurse(x, y)
    -------------------------------------------------------
    Parameters:
        x - an integer (int)
        y - an integer (int)
    Returns:
        ans - the function result (int)
    -------------------------------------------------------
    """
    
    #Base Case
    if((x < 0) or (y<0)):
        ans=x-y
    else:
        ans = recurse(x-1,y) + recurse(x, y-1)
    
    return ans

def gcd(m, n):
    """
    -------------------------------------------------------
    Recursively find the Greatest Common Denominator of two numbers.
    Use: ans = gcd(m, n)
    -------------------------------------------------------
    Parameters:
        n - an integer (int)
        m - an integer (int)
    Returns:
        ans - the function result (int)
    -------------------------------------------------------
    """
    
    if m % n == 0:
        ans= n
    else:
        ans=gcd(n, m % n)
    
    return ans

def vowel_count(s):
    """
    -------------------------------------------------------
    Recursively counts number of vowels in a string.
    Use: count = vowel_count(s)
    -------------------------------------------------------
    Parameters:
        s - string to examine (str)
    Returns:
        count - number of vowels in s (int)
    -------------------------------------------------------
    """
    
    if (len(s) == 0):
        count=0
    else:
        pass
        
        
    
def to_power(base, power):
    """
    -------------------------------------------------------
    Calculates base^power.
    Use: ans = to_power(base, power)
    -------------------------------------------------------
    Parameters:
        base - base to apply power to (float)
        power - power to apply (int)
    Returns:
        ans - base ^ power (float)
    -------------------------------------------------------
    """
    
    
    
    
        
    
    
    