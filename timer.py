def is_network_connected(person_to_friends: Dict[str, List[str]]) -> bool:
    '''
    Return whether the social network based on the given
    person_to_friends dictionary is connected. A network
    is connected if and only if every key in the dictionary
    is linked, through a sequence of friends, to every
    other person in the dictionary.

    >>> param = {}
    >>> is_network_connected(param)
    True
    >>> param ={'Jay Pritchett': ['Claire Dunphy', 'Gloria Pritchett', \
           'Manny Delgado'], 'Claire Dunphy': ['Jay Pritchett', \
           'Mitchell Pritchett', 'Phil Dunphy'], 'Manny Delgado':\
           ['Gloria Pritchett', 'Jay Pritchett', 'Luke Dunphy'],\
           'Mitchell Pritchett': ['Cameron Tucker', 'Claire Dunphy',\
           'Luke Dunphy'], 'Alex Dunphy': ['Luke Dunphy'], \
           'Cameron Tucker': ['Gloria Pritchett', 'Mitchell Pritchett'],\
           'Haley Gwendolyn Dunphy': ['Dylan D-Money', 'Gilbert D-Cat'],\
           'Phil Dunphy': ['Claire Dunphy', 'Luke Dunphy'], \
           'Dylan D-Money': ['Chairman D-Cat', 'Haley Gwendolyn Dunphy'],\
           'Gloria Pritchett': ['Cameron Tucker', 'Jay Pritchett', \
           'Manny Delgado'], 'Luke Dunphy': ['Alex Dunphy', \
           'Manny Delgado', 'Mitchell Pritchett', 'Phil Dunphy']}
    >>> is_network_connected(param)
    False
    >>> param = {'Jay Pritchett': ['Claire Dunphy', 'Gloria Pritchett', \
            'Manny Delgado'], 'Claire Dunphy': ['Claire Dunphy', \
            'Jay Pritchett', 'Mitchell Pritchett', 'Phil Dunphy', \
            'moe ah'],'Manny Delgado': ['Gloria Pritchett', \
            'Jay Pritchett', 'Luke Dunphy', 'moe ah'], 'Gloria Pritchett': \
            ['Cameron Tucker', 'Jay Pritchett', 'Manny Delgado', 'moe ah']}
    >>> is_network_connected(param)
    True
    >>> param = {'moe ahmed': ['Karim Benzema']}
    >>> is_network_connected(param)
    True
    >>> param = {'Lionel Messi': ['Cristiano Ronaldo'], 'Robert Luis': \
                ['Cristiano Ronaldo']}
    >>> is_network_connected(param)
    False
    '''
    keys_lst = []
    connected_ppl_lst = []
    connected = True
    for key in person_to_friends:
            if not (person_to_friends in keys_lst):
                    keys_lst.append(key)

    # If the key has on;y one key then the network is connected
    # return True
    if len(keys_lst) == 1:
        return True

    for key_name in keys_lst:
        for key in person_to_friends:
            if key_name == key:
                for value in person_to_friends[key]:
                    if value in keys_lst and not (value in connected_ppl_lst):
                        connected_ppl_lst.append(value)

                for name in connected_ppl_lst:
                    for key1 in person_to_friends:
                          if key1 == name:
                              friends_of_friends_lst = get_friends_of_friends\
                                                       (person_to_friends, name)
                              for index in friends_of_friends_lst:
                                 if index in keys_lst and not (index in \
                                 connected_ppl_lst):
                                     connected_ppl_lst.append(index)

                              for value1 in person_to_friends[key1]:
                                  friends_of_friends_lst = get_friends_of_friends\
                                                            (person_to_friends, value1)
                                  for index2 in friends_of_friends_lst:
                                      if index2 in keys_lst and not (index2 in \
                                      connected_ppl_lst):
                                          connected_ppl_lst.append(index2)

                              for name2 in connected_ppl_lst:
                                  friends_of_friends_lst = get_friends_of_friends \
                                 (person_to_friends, name2)
                                  for index2 in friends_of_friends_lst:
                                        if name2 in keys_lst and not (name2 in \
                                        connected_ppl_lst):
                                              connected_ppl_lst.append(name2)

                if len(connected_ppl_lst) != len(keys_lst):
                    connected = False
                else:
                    del connected_ppl_lst[:]

    return (connected)

def time_listfunc(is_network_connected: Callable[[List[int]], List[int]]) -> float:
    '''Return how many seconds it takes to run function f on a shuffled
    list with n items, on average over m times.
    '''

    import time
    total = 0
    #for i in range(m):
    p2f = make_dict()
    t1 = time.time()
    f(p2f)
    t2 = time.time()
    total += t2 - t1
    return total
print(time_listfunc(is_network_connected))
