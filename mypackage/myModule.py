def top_n (items, n):
    '''Returns the top n items in an array in desc order.
    
    Args:
    items(array): list or array-like object containg numerical values
    n(int): number of top item to return to return.
    returns:
       array: top n items in descending order.
    Examples:
        >>> top_n([8, 3, 2, 7, 4], 3)
        [8, 7, 4]
    '''

    for i in range(n): #keep sorting until we have the top_n items
        for j in range(len(items)-1-i):

            if items[j] > items[j+1]: #if this item is bigger than the next one...
                items[j], items[j+1] = items[j+1], items[j] #swap the two

#Get the last items
    top_n = items[-n:]

#Return in descending order
    return top_n[::-1]