def new_list():
    newlist = {
        "elements": [],
        "size": 0,
    }
    return newlist

def get_element(my_list, index):
    return my_list["elements"][index]

def is_present(my_list, element, cmp_function):
    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1

def add_first(my_list, new_element):
    t_list=[]
    t_list.append(new_element)
    for i in my_list["elements"]:
        t_list.append(i)
    my_list["elements"]=t_list
    my_list["size"]+=1
    return my_list

def add_last(my_list, new_element):
    my_list["elements"].append(new_element)
    my_list["size"]+=1
    return my_list

def size(my_list):
    return my_list["size"]

def first_element(my_list):
    return my_list["elements"][0]