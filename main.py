def flat_list(l):
    # input nested list is stored in l
    # Insert Code below
    sdl=[]
    for item in 1:
        if type(item) == list:
            sdl.extend(flat_list(item))
        else:
            sdl.append(item)
    
    # Insert Code Above
    # Return single-dimension list.
    return sdl
