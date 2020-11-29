

def split_list(n):
    """will return the list index"""
    return [(x+1) for x,y in zip(n, n[1:]) if y-x != 1]

def get_sub_list(my_list):
    """will split the list base on the index"""
    my_index = split_list(my_list)
    output = list()
    prev = 0
    for index in my_index:
        new_list = [ x for x in my_list[prev:] if x < index]
        output.append(new_list)
        prev += len(new_list)
    output.append([ x for x in my_list[prev:]])
    return output



def solution(my_list):
 print get_sub_list(my_list)
 s=""
 for elem in get_sub_list(my_list) :
     if len(elem) > 2 :
        s = s + str(elem[0]) + "-" + str(elem[-1]) + ","
     else : 
         if len(elem) > 1:
            s = s + str(elem[0]) + "," + str(elem[1]) + ","
         else : 
            s = s + str(elem[0]) + ","    
 return s.strip(",")           
