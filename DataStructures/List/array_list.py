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

def last_element(my_list):
    return my_list["elements"][len(my_list["elements"])-1]

def is_empty(my_list):
    if my_list["elements"]==[]:
        return True
    else:
        return False

def remove_first(my_list):
    temp_list=[]
    if my_list["size"]>=1:
        rst=my_list["elements"][0]
    if my_list["size"]>1:
        for i in range(1, my_list["size"]):
            temp_list.append(my_list["elements"][i])
    my_list["elements"]=temp_list
    if my_list["size"]>=1:
        my_list["size"]-=1
    return rst

def remove_last(my_list):
    temp_list=[]
    if my_list["size"]>=1:
        rst=my_list["elements"][my_list["size"]-1]
    if my_list["size"]>1:
        for i in range(0, my_list["size"]-1):
            temp_list.append(my_list["elements"][i])
    my_list["elements"]=temp_list
    if my_list["size"]>=1:
        my_list["size"]-=1
    return rst

def insert_element(my_list, position, new_element):
    if my_list["size"]>=1:
        my_list["elements"].append(0)
        i=my_list["size"]
        while i >= position:
            my_list["elements"][i]=my_list["elements"][i-1]
            i-=1
        my_list[position]=new_element
    else:
        my_list["elements"].append(new_element)
    my_list["size"]+=1
    
    return my_list
        
def delete_element(my_list, position):
    my_list["elements"].pop(position)
    my_list["size"]-=1
    return my_list

def change_info(my_list, position, new_element):
    my_list["elements"][position]=new_element
    return my_list

def exchange(my_list, pos1, pos2):
    temp=my_list["elements"][pos1]
    my_list["elements"][pos1]=my_list["elements"][pos2]
    my_list["elements"][pos2]=temp
    return my_list

def sub_list(my_list, pos1, pos2):
    temp_list=[]
    if my_list["size"] >=1:
        for i in range(pos1, pos2):
            temp_list.append(my_list["elements"][i])
        newlist = {
            "elements": temp_list,
            "size": len(temp_list),
    }
    else:
        newlist = {
        "elements": [],
        "size": 0,
    }
    return newlist