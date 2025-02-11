def new_list():
    newlist = {
        "first": None,
        "last" : None,
        "size" : 0
    }
    return newlist

def get_element(my_list, pos):
    searchpos = 0
    node = my_list['first']
    while searchpos < pos:
        node = node['next']
        searchpos += 1
    return node['info']

def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list['first']
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp['info']) == 0:
            is_in_array = True
        else: 
            temp = temp['next']
            count += 1
    if not is_in_array:
        count -=1
    return count

def add_first(my_list, element):
    if my_list['size'] == 0:
        my_list['first'] = {'info': element,
                            'next':None}
        my_list['last'] = my_list['first'] #Jsantanilla - Convierte element en el primer y ultimo dato
        my_list['size'] += 1
    else:
        first_anterior = my_list['first']
        my_list['first'] = {'info': element,
                            'next':first_anterior} #Jsantanilla - Convierte element en el primer dato y asigna el primer dato anterior como el siguiente
        my_list['size'] += 1
    return my_list

def add_last(my_list, element):
    if my_list['size'] == 0:
        my_list['first'] = {'info': element,
                            'next':None}
        my_list['last'] = my_list['first'] #Jsantanilla - Convierte element en el primer y ultimo dato
        my_list['size'] += 1
        return my_list
    else: 
        my_list['last']['next'] = {'info':element, 
                                    'next':None} #Jsantanilla - Relaciona element con el ultimo elemento actual de la lista
        my_list['last'] = my_list['last']['next'] #Jsantanilla - Convierte element en el ultimo elemento de la lista y añade 1
        my_list['size'] += 1
    return my_list

def size(my_list):
    cantidad = my_list['size'] #Jsantanilla - Saca el tamaño de la lista, de la variable size y lo retorna
    return cantidad

def first_element(my_list):
    if my_list['size'] != 0:
        primero = my_list['first']['info'] #Jsantanilla - Saca primer elemento de la lista, de la variable first y lo retorna
        return primero
    else:
        raise Exception('IndexError: list index out of range') #Jsantanilla - Retorna error

def last_element(my_list):
    if my_list['size'] != 0:
        primero = my_list['last']['info'] #Jsantanilla - Saca ultimo elemento de la lista, de la variable last y lo retorna
        return primero
    else:
        raise Exception('IndexError: list index out of range') #Jsantanilla - Retorna error

def remove_first(my_list):
    if my_list['size'] == 1:#Jsantanilla - Valida cuando solo hay un elemento para eliminar el dato last
        elemento = my_list['first']['info']
        my_list ['first'] = None
        my_list ['last'] = None
        my_list['size'] -= 1
        return elemento
    if my_list['size'] != 0 and my_list['size'] != 1: #Jsantanilla - Guarda el siguiente en una variable, la asigna a first y borra relacion con el anterior.
        elemento = my_list['first']['info']
        siguiente = my_list['first']['next']
        my_list['first']['next'] = None
        my_list['first'] = siguiente
        my_list['size'] -= 1
        return elemento
    if my_list['size'] == 0:
        raise Exception('IndexError: list index out of range') #Jsantanilla - Retorna error
    return my_list
    
def remove_last(my_list):
    if my_list['size'] == 1:#Jsantanilla - Valida cuando solo hay un elemento para eliminar el dato first
        elemento = my_list['last']['info']
        my_list ['first'] = None
        my_list ['last'] = None
        my_list['size'] -= 1
        return elemento
    if my_list['size'] != 0 and my_list['size'] != 1: 
        elemento = my_list ['last']['info']
        nodo = my_list['first']
        while nodo['next'] != my_list['last']: #Jsantanilla - Corta relacion con last desde el dato anterior y asigna uno nuevo
            nodo = nodo['next']
        my_list['last'] = nodo
        nodo['next'] = None
        my_list['size'] -= 1
        return elemento
    if my_list['size'] == 0:
        raise Exception('IndexError: list index out of range') #Jsantanilla - Retorna error
    return my_list

def is_empty(my_list):
    if my_list['size'] == 0: #Jsantanilla - Valida con la variable size el tamaño de la lista
        return True
    else:
        return False

def insert_element(my_list, element, pos):
    if pos < 0 or pos > size(my_list):#Jsantanilla - Retorna error
        raise Exception('IndexError: list index out of range')
    posicion = 1
    nodo = my_list['first']
    if my_list['size'] == 1:
        my_list = add_first(my_list, element) #Jsantanilla - Valida que haya más de un solo elemento 
    else:
        while posicion != pos and nodo['next'] != None:
            nodo = nodo['next']     #Jsantanilla - Cuenta posiciones y añade el nuevo elemento
        if nodo != my_list['last']:
            nodo_anterior = nodo
            nodo_siguiente = nodo['next']
            nodo_anterior['next'] = {'info': element,
                               'next':nodo_siguiente}
            my_list['size'] +=1
        else:
            my_list = add_last(my_list, element)#Jsantanilla - Valida que cuando se quiere insertar en el ultimo elemento
    return my_list

def delete_element(my_list,pos):
    if pos < 0 or pos > size(my_list):#Jsantanilla - Retorna error
        raise Exception('IndexError: list index out of range')
    posicion = 1
    nodo = my_list['first']
    if my_list['size'] == 1:
        remove_first(my_list) #Jsantanilla - Valida que haya más de un solo elemento 
    else:
        while posicion != pos and nodo['next'] != None:
            nodo = nodo['next']     #Jsantanilla - Cuenta posiciones y elimina el elemento
        if nodo != my_list['last']:
            nodo_anterior = nodo
            nodo_siguiente = nodo['next']
            nodo_anterior['next'] = nodo_siguiente
            my_list['size'] -=1
        else:
            remove_last(my_list)#Jsantanilla - Valida que cuando se quiere insertar en el ultimo elemento
    return my_list

def change_info(my_list,pos,new_info):
    if pos < 0 or pos > size(my_list):#Jsantanilla - Retorna error
        raise Exception('IndexError: list index out of range')
    posicion = 1
    nodo = my_list['first']
    while posicion != pos and nodo['next'] != None:
            nodo = nodo['next']     #Jsantanilla - Cuenta posiciones y cambia la informacion
    nodo['info'] = new_info
    return my_list

def exchange (my_list,pos1,pos2):
    if pos1 < 0 or pos1 > size(my_list) or pos2 < 0 or pos2 > size(my_list):#Jsantanilla - Retorna error
        raise Exception('IndexError: list index out of range')
    if pos1 == pos2:
        return my_list
    else:
        posicion = 1
        nodo = my_list['first']
        exchange = False
        while exchange != True: #Jsantanilla - Valida que el cambio no este hecho
            nodo = nodo['next']
            if posicion <= pos1 or posicion <= pos2: 
                nodo_a1 = nodo
                nodo_s1 = nodo['next']
                nodo_a2 = nodo
                nodo_s2 = nodo['next'] #Jsantanilla - Modifica todos los punteros hasta encontrar la primer coincidencia
                nodo1 = nodo_a1['next']
                nodo2 = nodo_a2['next']
            elif posicion > pos1 or posicion > pos2:
                nodo_a2 = nodo
                nodo_s2 = nodo['next']
                nodo2 = nodo_a2['next'] #Jsantanilla - Modifica los punteros de solo uno de los nodos hasta encontrar la segunda coincidencia dentro del mismo ciclo
            elif posicion >= pos1 and posicion >= pos2:
                nodo_a1['next'] = nodo2
                nodo2['next'] = nodo_s1 #Jsantanilla - valida que las coincidencias esten hechas y hace el cambio
                nodo_a2['next'] = nodo1
                nodo1['next'] = nodo_s2
                if nodo1 == my_list['first']: #Jsantanilla - Valida si alguno de los casos es first o last
                    my_list['first'] = nodo2
                if nodo2 == my_list['last']:
                    my_list['last'] = nodo1
                exchange = True           #Jsantanilla - sale del ciclo
        return my_list
def sub_list(my_list, pos, num_elements):
    if pos < 0 or pos > size(my_list):#Jsantanilla - Retorna error
        raise Exception('IndexError: list index out of range')
    if pos == size(my_list):
        return last_element(my_list)
    elif pos == 1:
        return my_list
    else:
        posicion = 1
        nodo = my_list['first']
        nueva_lista = {'first':None,
                       'last':None,
                       'size':0}
        while nodo['next'] != None:
            nodo = nodo ['next']
            posicion +=1
            sub = 0
            if posicion == pos:
                sub += 1
                nueva_lista['first'] = nodo
                nodo2 = nueva_lista['first']
            elif posicion > pos and nueva_lista['first'] != None and sub <= num_elements:
                nodo2['next'] = nodo
                nodo2 = nodo2['next']
        return nueva_lista
                
                

        

    