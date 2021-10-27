
def invert_file(fin, fout = None):
    """specify file input to read from arg[0], optional: file to write inverted dict to arg[1]"""
    inverted_dict = dict()
    #clean up input to prepare to push to new dict; chained replace methods are fastest way for this
    d = open(fin).read().replace("{","").replace("}","").replace(" ","").replace("'","").split(",")
    #split each element @ ":" into a list of key/value pairs
    for line in d:
        l = line.split(":")
        key = l[0]
        val = l[1]
        #swap values with keys in inverted dict. 
        if val not in inverted_dict:
            inverted_dict[val] = key
    #if second arg is given, make file with inverted dict
    if fout != None:
        try:
            new_file = open(fout, 'w+')
            new_file.write(str(inverted_dict))
        except Exception as err:
            print(err)
            return inverted_dict
    #else, return inverted dictionary
    return inverted_dict
    
print("Original dict: ", open('dict.txt').read())
print("Inverted dict: ", invert_file('dict.txt','new1.txt'))



