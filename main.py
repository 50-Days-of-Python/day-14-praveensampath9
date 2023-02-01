from itertools import chain
def flat_list(l):
    # input nested list is stored in l
    # Insert Code below
    sdl=[]
    for elt in l:
        if type(elt) == list:
            sdl.extend(elt)
        else:
            sdl.append(elt)
    
    # Insert Code Above
    # Return single-dimension list.
    return sdl
