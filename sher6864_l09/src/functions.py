"""
-------------------------------------------------------
Program Description
-------------------------------------------------------
Author:  Jack Sherwood
ID:             1691168645
Email:        sher6864@mylaurier.ca
__updated__ = Mar 12, 2026
-------------------------------------------------------
"""

def hash_table(slots, values):
    """
    -------------------------------------------------------
    Print a hash table of a set of values. The format is:
    Hash     Slot Key
    -------- ---- --------------------
     695    2 Lasagna, 7
    1355    4 Butter Chicken, 2
    Do not create an actual Hash_Set.
    Use: hash_table(slots, values)
    -------------------------------------------------------
    Parameters:
       slots - the number of slots available (int > 0)
       values - the values to hash (list of ?)
    Returns:
       None
    -------------------------------------------------------
    """
    
    print("Hash     Slot Key")
    print("-------- ---- --------------------")
    
    for val in values:
        h=hash(val)
        slot = h%slots
        k=val.key()
        print(f"{h:>8} {slot:>4} {k}")
    return
        
        