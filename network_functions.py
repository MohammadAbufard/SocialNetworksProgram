'''CSC108 Assignment 3: Social Networks'''

from typing import List, Tuple, Dict, TextIO


def load_profiles(profiles_file: TextIO, person_to_friends: Dict[str, \
                  List[str]], person_to_networks: Dict[str, List[str]]) -> None:
    '''
    Update the person_to_friends dictionary and the person_to_networks
    dictionary to include data from profiles_file.
    Docstring examples not given since the result depends on input data.
    '''

    for line in profiles_file:
        if "," in line:
            key_name = get_name(line)

        if not key_name in person_to_friends:
            person_to_friends[key_name] = []
        if not key_name in person_to_networks:
            person_to_networks[key_name] = []

        line_len = len(line.strip())
        while line_len != 0:
            line = profiles_file.readline().strip()
            if "," in line:
              value_name = get_name(line)

              if not (value_name in person_to_friends[key_name]):
                  person_to_friends[key_name].append(value_name)
                  person_to_friends[key_name].sort()

            line_len = len(line.strip())
            if not "," in line and line_len != 0:
                  if not (key_name) in person_to_networks[key_name]:
                        person_to_networks[key_name].append(line)
                        person_to_networks[key_name].sort()

    delete_empty_keys(person_to_friends, person_to_networks)


def get_name(line: str)-> str:
    '''
    Return a name (in the lastname-firstname form) based on the
    given a line.

    >>> get_name('Pritchett, Jay')
    'Jay Pritchett'
    >>> get_name('Bale, Gareth\n')
    'Gareth Bale'
    >>> get_name('Ahmed, Mohammad')
    'Mohammad Ahmed'
    >>> get_name('Dunphy, Luke\n')
    'Luke Dunphy'
    '''

    names = (line.split(","))
    names[0], names[1] = names[1].strip(), names[0]
    name = str(names[0]) + " " + str(names[1])

    return name


def delete_empty_keys(person_to_friends: Dict[str, List[str]], \
                  person_to_networks: Dict[str, List[str]]) -> None:
    '''
    Update the person_to_friends dictionary and the
    person_to_networks dictionary by deleting all the
    empty keys (keys with no values).

    >>> person_to_friends = {'Jay Pritchett': ['Claire Dunphy',\
                            'Gloria Pritchett', 'Manny Delgado'],\
                            'Claire Dunphy': ['Jay Pritchett',\
                            'Mitchell Pritchett', 'Phil Dunphy'],\
                            'McDuck Scrooge': [], 'Manny Delgado':\
                            ['Gloria Pritchett', 'Jay Pritchett',\
                            'Luke Dunphy'], 'Mitchell Pritchett':\
                            ['Cameron Tucker', 'Claire Dunphy', \
                            'Luke Dunphy'], 'Alex Dunphy': \
                            ['Luke Dunphy'], 'Cameron Tucker':\
                            ['Gloria Pritchett', \
                            'Mitchell Pritchett'], \
                            'Haley Gwendolyn Dunphy': \
                            ['Dylan D-Money', 'Gilbert D-Cat'],\
                            'Phil Dunphy': ['Claire Dunphy', \
                            'Luke Dunphy'], 'Dylan D-Money': \
                            ['Chairman D-Cat', \
                            'Haley Gwendolyn Dunphy'], \
                            'Gloria Pritchett': ['Cameron Tucker',\
                            'Jay Pritchett', 'Manny Delgado'], \
                            'Luke Dunphy': ['Alex Dunphy', \
                            'Manny Delgado', 'Mitchell Pritchett',\
                            'Phil Dunphy']}
    >>> person_to_networks = {}
    >>> delete_empty_keys(person_to_friends, person_to_networks)
    >>> person_to_friends
    {'Jay Pritchett': ['Claire Dunphy', 'Gloria Pritchett', \
    'Manny Delgado'], 'Mitchell Pritchett': ['Cameron Tucker',\
    'Claire Dunphy', 'Luke Dunphy'], 'Alex Dunphy': ['Luke Dunphy'],\
    'Dylan D-Money': ['Chairman D-Cat', 'Haley Gwendolyn Dunphy'],\
    'Gloria Pritchett': ['Cameron Tucker', 'Jay Pritchett', \
    'Manny Delgado']}
    >>> person_to_networks
    {}
    >>> person_to_friends = {}
    >>> person_to_networks = {'Jay Pritchett': [], 'Claire Dunphy':\
                             ['Parent Teacher Association'], \
                             'McDuck Scrooge': [], 'Manny Delgado':\
                             ['Chess Club'], 'Mitchell Pritchett': [],\
                             'Alex Dunphy': [], 'Cameron Tucker': [],\
                             'Haley Gwendolyn Dunphy': [], 'Phil Dunphy':\
                             [], 'Dylan D-Money': [], 'Gloria Pritchett':\
                             [], 'Luke Dunphy': []}
    >>> delete_empty_keys(person_to_friends, person_to_networks)
    >>> person_to_friends
    {}
    >>> person_to_networks
    {'Claire Dunphy': ['Parent Teacher Association'], \
    'Manny Delgado': ['Chess Club']}
    >>> person_to_friends = {'Karim Benzema': ['Claire Dunphy',\
                            'Paul Pogba', 'Manny Delgado'],\
                            'Gareth Bale': [], 'McDuck Scrooge': \
                            ['Moe Dunphy'], 'Manny Delgado':\
                            ['Mohmmad Ahmed'], 'Mitchell Pritchett':\
                            [], 'Alex Dunphy': [], 'Cameron Tucker':\
                            ['Omar Jay'], 'Haley Gwendolyn Dunphy': \
                            [], 'Phil Dunphy': [], 'Zlatan Ibrahimovic': \
                            [], 'Gloria Pritchett': [], \
                            'Luke Dunphy': ['Lionel Messi']}
    >>> person_to_networks = {'Lionel Messi': [], 'Moe Dunphy': \
                             ['Parent Teacher Association'], \
                             'McDuck Scrooge': [], 'Zlatan Ibrahimovic':\
                             ['Chess Club'], 'Mitchell Pritchett': \
                             ['Law Association'], 'Karim Benzema': \
                             ['Chess Club', 'Orchestra'], 'Cameron Tucker':\
                             ['Clown School', 'Wizard of Oz Fan Club'], \
                             'Gareth Bale': [], 'Omar Jay': \
                             ['Real Estate Association'], 'Dylan D-Money':\
                             [], 'Mohmmad Ahmed': \
                             ['Parent Teacher Association'], 'Luke Dunphy': []}
    >>> delete_empty_keys(person_to_friends, person_to_networks)
    >>> person_to_friends
    {'Karim Benzema': ['Claire Dunphy', 'Paul Pogba', 'Manny Delgado'],\
    'McDuck Scrooge': ['Moe Dunphy'], 'Manny Delgado': ['Mohmmad Ahmed'],\
    'Cameron Tucker': ['Omar Jay'], 'Luke Dunphy': ['Lionel Messi']}
    >>> person_to_networks
    {'Moe Dunphy': ['Parent Teacher Association'], 'Zlatan Ibrahimovic':\
    ['Chess Club'], 'Mitchell Pritchett': ['Law Association'], \
    'Karim Benzema': ['Chess Club', 'Orchestra'], 'Cameron Tucker':\
    ['Clown School', 'Wizard of Oz Fan Club'], 'Omar Jay': \
    ['Real Estate Association'], 'Mohmmad Ahmed': \
    ['Parent Teacher Association']}
    '''

    friends_empty_dic = []
    netwroks_empty_dic = []

    for key in person_to_friends:
        key_len = len(person_to_friends[key])
        if key_len == 0:
            friends_empty_dic.append(key)

    for empty_key in friends_empty_dic:
        person_to_friends.pop(empty_key, None)

    for key in person_to_networks:
        key_len = len(person_to_networks[key])
        if key_len == 0:
            netwroks_empty_dic.append(key)

    for empty_key in netwroks_empty_dic:
        person_to_networks.pop(empty_key, None)


def get_average_friend_count(person_to_friends: Dict[str, List[str]]) -> float:
    '''
    Return the average number of friends that the keys (profiles) in the given
    person_to_friends dictionary have.

    >>> param = {'Jay Pritchett': ['Claire Dunphy', 'Manny Delgado'],\
                'Cameron Tucker': ['Claire Dunphy', 'Manny Delgado', \
                'Gloria Pritchett']}
    >>> get_average_friend_count(param)
    2.5
    >>> param = {'Jay Pritchett': ['Luke Dunphy'], 'Luke Dunphy': \
                 ['Jay Pritchett']}
    >>> get_average_friend_count(param)
    1.0
    >>> param = {'Claire Dunphy': ['Alex Dunphy', 'Manny Delgado', \
                'Mitchell Pritchett', 'Haley Gwendolyn Dunphy',  \
                'Luke Dunphy', 'Gilbert D-Cat']}
    >>> get_average_friend_count(param)
    6.0
    >>> param = {}
    >>> get_average_friend_count(param)
    0.0
    >>> param = {'Jay Pritchett': ['Claire Dunphy', 'Gloria Pritchett',\
                'Manny Delgado'], 'Claire Dunphy': ['Jay Pritchett',  \
                'Mitchell Pritchett', 'Phil Dunphy'], 'Manny Delgado': \
                ['Gloria Pritchett', 'Jay Pritchett', 'Luke Dunphy'],  \
                'Mitchell Pritchett': ['Cameron Tucker', 'Claire Dunphy',\
                'Luke Dunphy'], 'Alex Dunphy': ['Luke Dunphy'], \
                'Cameron Tucker': ['Gloria Pritchett', \
                'Mitchell Pritchett'], 'Haley Gwendolyn Dunphy': \
                ['Dylan D-Money', 'Gilbert D-Cat'],'Phil Dunphy': \
                ['Claire Dunphy', 'Luke Dunphy'], 'Dylan D-Money': \
                ['Chairman D-Cat', 'Haley Gwendolyn Dunphy'],\
                'Gloria Pritchett': ['Cameron Tucker', 'Jay Pritchett',\
                'Manny Delgado'], 'Luke Dunphy': ['Alex Dunphy',\
                'Manny Delgado', 'Mitchell Pritchett', 'Phil Dunphy']}
    >>> get_average_friend_count(param)
    2.5454545454545454
    '''

    num_of_profiles = 0
    num_of_friends = 0

    for key in person_to_friends:
        num_of_profiles += 1
        num_of_friends += len(person_to_friends[key])

    if num_of_profiles == 0:
        return 0.0

    else:
        avg_friends = (num_of_friends / num_of_profiles)
        return avg_friends


def get_families(person_to_friends: Dict[str, List[str]]) -> \
                Dict[str, List[str]]:
    '''
    Return a dictionary in the form of lastnames to first names; where
    the keys are unique lastnames and the values are lists of all unique
    firstnames who share the same lastname with one another sorted
    alphabetically based on the give person_to_friends dictionary.
    The returned dictionary contains all the people in the
    person_to_friends dictionary as a key or in a value list.

    >>> param = {}
    >>> get_families(param)
    {}
    >>> param = {'Jay Pritchett': ['Claire Dunphy', 'Manny Delgado'],\
                 'Alex Pritchett': ['Claire Dunphy', 'Manny Delgado']}
    >>> get_families(param)
    {'Pritchett': ['Alex', 'Jay'], 'Dunphy': ['Claire'], \
    'Delgado': ['Manny']}
    >>> param = {'Luke Dunphy': ['Haley Gwendolyn Dunphy'], \
                'Moe Dunphy': ['Luke Dunphy']}
    >>> get_families(param)
    {'Dunphy': ['Haley Gwendolyn', 'Luke', 'Moe']}
    >>> param = {'Jay Pritchett': ['Jay Pritchett'], \
                'Manny Delgado': ['Manny Delgado'], 'Claire Dunphy': \
                ['Claire Dunphy']}
    >>> get_families(param)
    {'Pritchett': ['Jay'], 'Delgado': ['Manny'], 'Dunphy': ['Claire']}
    >>> param = {'Jay Pritchett': ['Claire Dunphy','Manny Delgado'], \
                'Cameron Tucker': ['Dylan D-Money', 'Gilbert D-Cat'], \
                'Cristiano Ronaldo': ['Lionel Messi', \
                'Zlatan Ibrahimovic', 'Diego Maradona'], 'Paul Pogba': \
                ['David Beckham', 'Gareth Bale', 'Karim Benzema']}
    >>> get_families(param)
    {'Pritchett': ['Jay'], 'Dunphy': ['Claire'], 'Delgado': ['Manny'], \
    'Tucker': ['Cameron'], 'D-Money': ['Dylan'], 'D-Cat': ['Gilbert'], \
    'Ronaldo': ['Cristiano'], 'Messi': ['Lionel'], Ibrahimovic': ['Zlatan'], \
    'Maradona': ['Diego'], 'Pogba': ['Paul'], 'Beckham': ['David'], \
    'Bale': ['Gareth'], 'Benzema': ['Karim']}
    '''

    names_list = []

    for key in person_to_friends:
        for value in person_to_friends[key]:
            if not (key in names_list):
                names_list.append(key)
            if not (value in names_list):
                names_list.append(value)
    return get_families_helper_function(names_list)


def get_families_helper_function(names_list: Dict[str, List[str]]) -> \
                        Dict[str, List[str]]:
    '''
    Return a dictionary in the form of lastnames to first names by converting
    the list names_list into a dictionary where the keys are unique lastnames
    and the values are lists of all unique firstnames who share the same
    lastname with one another sorted alphabetically.

    >>> param = {}
    >>> get_families_helper_function(param)
    {}
    >>> param = ['Jay Pritchett', 'Claire Dunphy', 'Manny Delgado', \
                'Alex Pritchett']
    >>> get_families_helper_function(param)
    {'Pritchett': ['Alex', 'Jay'], 'Dunphy': ['Claire'], 'Delgado': ['Manny']}
    >>> param = ['Luke Dunphy', 'Haley Gwendolyn Dunphy', 'Moe Dunphy']
    >>> get_families_helper_function(param)
    {'Dunphy': ['Haley Gwendolyn', 'Luke', 'Moe']}
    >>> param = ['Jay Pritchett', 'Manny Delgado', 'Claire Dunphy']
    >>> get_families_helper_function(param)
    {'Pritchett': ['Jay'], 'Delgado': ['Manny'], 'Dunphy': ['Claire']}
    >>> param = ['Jay Pritchett', 'Claire Dunphy', 'Manny Delgado', \
                'Cameron Tucker', 'Dylan D-Money', 'Gilbert D-Cat', \
                'Cristiano Ronaldo', 'Lionel Messi', 'Zlatan Ibrahimovic', \
                'Diego Maradona', 'Paul Pogba', 'David Beckham', \
                'Gareth Bale', 'Karim Benzema']
    >>> get_families_helper_function(param)
    {'Pritchett': ['Jay'], 'Dunphy': ['Claire'], 'Delgado': ['Manny'], \
    'Tucker': ['Cameron'], 'D-Money': ['Dylan'], 'D-Cat': ['Gilbert'], \
    'Ronaldo': ['Cristiano'], 'Messi': ['Lionel'], Ibrahimovic': ['Zlatan'], \
    'Maradona': ['Diego'], 'Pogba': ['Paul'], 'Beckham': ['David'], \
    'Bale': ['Gareth'], 'Benzema': ['Karim']}
    '''

    families_dic = {}

    for name in names_list:
        space_index = name.rfind(" ")
        last_name = name[space_index: len(name)].strip()

    for name in names_list:
        space_index = name.rfind(" ")
        last_name = name[space_index: len(name)].strip()

        if not (last_name in list(families_dic)):
            families_dic[last_name] = []

        for key in families_dic:
            if last_name in key:
                families_dic[key].append(name[0:space_index].strip())
                families_dic[last_name].sort()

    return families_dic


def invert_network(person_to_networks: Dict[str, List[str]]) \
                    -> Dict[str, List[str]]:

    '''
    Return a dictionary in the form of network to people based on the
    given person_to_networks dictionary. The keys of the dictionary
    are unique network names and the values are alphabetically sorted
    lists of people who belong to the network in firstname-lastname format.

    >>> param = {}
    >>> invert_network(param)
    {}
    >>> param = {'Claire Dunphy': ['Parent Teacher Association'], \
                'Manny Delgado': ['Chess Club'], 'Mitchell Pritchett': \
                ['Law Association'], 'Alex Dunphy': ['Chess Club', \
                'Orchestra'], 'Cameron Tucker': ['Clown School', \
                'Wizard of Oz Fan Club'], 'Phil Dunphy': \
                ['Real Estate Association'], 'Gloria Pritchett': \
                ['Parent Teacher Association']}
    >>> invert_network(param)
    {'Parent Teacher Association': ['Claire Dunphy', 'Gloria Pritchett'], \
    'Chess Club': ['Alex Dunphy', 'Manny Delgado'], 'Law Association': \
    ['Mitchell Pritchett'], 'Orchestra': ['Alex Dunphy'], 'Clown School': \
    ['Cameron Tucker'], 'Wizard of Oz Fan Club': ['Cameron Tucker'], \
    'Real Estate Association': ['Phil Dunphy']} \
    >>> param = {'Manny Delgado': ['Chess Club'], 'Cameron Tucker': \
                ['Clown School', 'Wizard of Oz Fan Club'], 'Gloria Pritchett':\
                ['Parent Teacher Association'], 'moe ahmed': \
                ['Parent Teacher Association', 'Law Association', 'Chess Club',\
                'Orchestra', 'Clown School', 'Wizard of Oz Fan Club', \
                'Real Estate Association']}
    >>> invert_network(param)
    {'Chess Club': ['Manny Delgado', 'moe ahmed'], 'Clown School': \
    ['Cameron Tucker', 'moe ahmed'], 'Wizard of Oz Fan Club': \
    ['Cameron Tucker', 'moe ahmed'], 'Parent Teacher Association': \
    ['Gloria Pritchett', 'moe ahmed'], 'Law Association': ['moe ahmed'], \
    'Orchestra': ['moe ahmed'], 'Real Estate Association': ['moe ahmed']} \
    >>> param = {'Manny Delgado': ['Chess Club'], 'Cameron Tucker': \
    ['Clown School'], 'Gloria Pritchett': ['Parent Teacher Association']} \
    >>> invert_network(param)
    {'Chess Club': ['Manny Delgado'], 'Clown School': ['Cameron Tucker'], \
    'Parent Teacher Association': ['Gloria Pritchett']}
    >>> param = {'Manny Delgado': ['Chess Club']}
    >>> invert_network(param)
    {'Chess Club': ['Manny Delgado']}
    '''

    network_names = []
    network_to_people = {}
    for key in person_to_networks:
        if not key in network_names:
            network_names.append(person_to_networks[key])

    for index in network_names:
        for network in index:
            if not network in network_to_people:
                network_to_people[network] = []

    for network in network_to_people:
        for key in person_to_networks:
            if network in person_to_networks[key]:
                network_to_people[network].append(key)
                network_to_people[network].sort()

    return network_to_people


def get_friends_of_friends(person_to_friends: Dict[str, List[str]], \
                           person: str) -> List[str]:
    '''
    Based on the given person_to_friends dictionary and the person
    (in the firstname-lastname form). Return a list (sorted in
    alphabetical order) of people's names in the form of firstname-lastname
    of people who are friends of the person's friends. The returned
    list will not contain the person and the friend of a friend
    will be listed in the returned list once for each mutual friend.

    >>> param = {'Jay Pritchett': ['Claire Dunphy', 'Gloria Pritchett', \
                'Manny Delgado'], 'Claire Dunphy': ['Jay Pritchett', \
                'Mitchell Pritchett', 'Phil Dunphy'], 'Manny Delgado': \
                ['Gloria Pritchett', 'Jay Pritchett', 'Luke Dunphy'], \
                'Alex Dunphy': ['Luke Dunphy'], 'Gloria Pritchett': \
                ['Cameron Tucker', 'Jay Pritchett', 'Manny Delgado']}
    >>> get_friends_of_friends(param , 'Jay Pritchett')
    ['Cameron Tucker', 'Gloria Pritchett', 'Luke Dunphy', \
    'Manny Delgado', 'Mitchell Pritchett', 'Phil Dunphy']
    >>> param = {'Jay Pritchett': ['Claire Dunphy', 'Gloria Pritchett', \
                'Manny Delgado'], 'Claire Dunphy': ['Jay Pritchett', \
                'Mitchell Pritchett', 'Phil Dunphy', 'moe ah'],'Manny Delgado':\
                ['Gloria Pritchett', 'Jay Pritchett', 'Luke Dunphy', 'moe ah'],\
                'Gloria Pritchett': ['Cameron Tucker', 'Jay Pritchett', \
                'Manny Delgado', 'moe ah']}
    >>> get_friends_of_friends(param , 'Jay Pritchett')
    ['Cameron Tucker', 'Gloria Pritchett', 'Luke Dunphy', 'Manny Delgado', \
    'Mitchell Pritchett', 'Phil Dunphy', 'moe ah', 'moe ah', 'moe ah']
    >>> param = {'Jay Pritchett': ['Claire Dunphy', 'Gloria Pritchett', \
                'Manny Delgado'], 'Claire Dunphy': ['Claire Dunphy', \
                'Jay Pritchett', 'Mitchell Pritchett', 'Phil Dunphy', \
                'moe ah'],'Manny Delgado': ['Gloria Pritchett', \
                'Jay Pritchett', 'Luke Dunphy', 'moe ah'], 'Gloria Pritchett':\
                ['Cameron Tucker', 'Jay Pritchett', 'Manny Delgado', 'moe ah']}
    >>> get_friends_of_friends(param, 'Claire Dunphy')
    ['Gloria Pritchett', 'Jay Pritchett', 'Manny Delgado', \
    'Mitchell Pritchett', 'Phil Dunphy', 'moe ah']
    >>> param = {'Claire Dunphy': ['Claire Dunphy', 'Jay Pritchett', \
                'Mitchell Pritchett', 'Phil Dunphy', 'moe ah']}
    >>> get_friends_of_friends(param, 'Claire Dunphy')
    ['Jay Pritchett', 'Mitchell Pritchett', 'Phil Dunphy', 'moe ah']
    '''

    friends_of_friends = []
    friends_lst = []
    final_lst = []
    for key in person_to_friends:
            if key == person:
                for value in person_to_friends[key]:
                    if not (person_to_friends[key] in friends_lst):
                        friends_lst.append(value)

    for friend in friends_lst:
        for x in person_to_friends:
            if friend == x:
                for value in person_to_friends[x]:
                        friends_of_friends.append(value)
                        friends_of_friends.sort()

    for index in  friends_of_friends:
        if index != person:
            final_lst.append(index)
            final_lst.sort()

    return final_lst


def same_lname_point_and_sorting(person: str, person_to_friends: Dict \
                                 [str, List[str]], potential_friends: \
                                 List[str], recommendation_dic: \
                                 Dict[str, List[str]]) \
                                 -> List[Tuple[str, int]]:
    '''
    Return a list of tuples of friend recommendations (sorted from
    highest to lowest score and alphabetically if the scores are
    equal) for the selected person based on the provided
    potential_friends list and the person_to_friends, person_to_networks,
    and the recommendation_dic dictionaries. The first element of the
    returned tuple is a potential friend's name (in the firstname-lastname
    form) and the second element is their score, a person is included
    in the list if and only if their score is greater than zero.

    >>> same_lname_point_and_sorting('Lionel Messi',{'Lionel Messi': \
                                    ['Cristiano Ronaldo'], 'Robert Luis' : \
                                    ['Cristiano Ronaldo']}, ['Robert Luis'], \
                                    {'Robert Luis': [1]})
    [('Robert Luis', 1)]
    >>> same_lname_point_and_sorting('Robert Luis',{'Lionel Messi': \
                                    ['Cristiano Ronaldo'], 'Robert Luis': \
                                    ['Cristiano Ronaldo']}, ['Lionel Messi'],\
                                    {'Lionel Messi': [1]})
    [('Lionel Messi', 1)]
    >>> x = {'Jay Pritchett': ['Claire Dunphy', 'Gloria Pritchett', \
            'Manny Delgado'], 'Claire Dunphy': ['Mitchell Pritchett', \
            'Jay Pritchett', 'Phil Dunphy'], 'Manny Delgado': \
            ['Gloria Pritchett', 'Jay Pritchett', 'Luke Dunphy'], \
            'Mitchell Pritchett': ['Cameron Tucker', 'Gloria Pritchett',\
            'Manny Delgado','Claire Dunphy', 'Luke Dunphy'], 'Alex Dunphy':\
            ['Luke Dunphy'], 'Cameron Tucker': ['Gloria Pritchett', \
            'Mitchell Pritchett'], 'Haley Gwendolyn Dunphy': ['Dylan D-Money',\
            'Gilbert D-Cat'], 'Phil Dunphy': ['Claire Dunphy', 'Luke Dunphy'],\
            'Dylan D-Money': ['Chairman D-Cat', 'Haley Gwendolyn Dunphy'], \
            'Gloria Pritchett': ['Cameron Tucker', 'Jay Pritchett', \
            'Manny Delgado'], 'Luke Dunphy': ['Manny Delgado','Phil Dunphy'], \
            'Mohammad Ahmed': ['Claire Dunphy']}
    >>> potential_friends = ['Alex Dunphy', 'Cameron Tucker', 'Chairman D-Cat',\
                            'Dylan D-Money', 'Gilbert D-Cat', \
                            'Haley Gwendolyn Dunphy', 'Luke Dunphy', \
                            'Mitchell Pritchett', 'Mohammad Ahmed', \
                            'Phil Dunphy']
    >>> recommendation_dic = {'Alex Dunphy': [1, 1], 'Cameron Tucker': [1, 1, 1], \
            'Chairman D-Cat': [], 'Dylan D-Money': [], 'Gilbert D-Cat': [], \
            'Haley Gwendolyn Dunphy': [], 'Luke Dunphy': [1], \
            'Mitchell Pritchett': [1, 1, 1], 'Mohammad Ahmed':\
            [1], 'Phil Dunphy': [1, 1]}
    >>> same_lname_point_and_sorting('Jay Pritchett', x, potential_friends, \
                                    recommendation_dic)
    [('Mitchell Pritchett', 4), ('Cameron Tucker', 3), ('Alex Dunphy', 2), \
    ('Phil Dunphy', 2), ('Luke Dunphy', 1), ('Mohammad Ahmed', 1)]
    '''

    final = []
    pers_first_name = person[0:person.rfind(" ")].strip()
    last_names = get_families(person_to_friends)
    for key in last_names:
        for potenial in potential_friends:
            space_index = potenial.rfind(" ")
            first_name = potenial[0:space_index].strip()
            dic_len = len(recommendation_dic[potenial])
            if first_name in last_names[key] and pers_first_name \
            in last_names[key] and  dic_len != 0:
                    recommendation_dic[potenial].append(1)
    for index in recommendation_dic:
        dic_len = len(recommendation_dic[index])
        if dic_len > 0:
            tup = (index, dic_len)
            final.append(tup)

    # This part of the code was taken from the course notes provided by professor
    # Samir Hamdi
    for tup_values in range(len(final)-1, 0, -1):
        for index in range(tup_values):
            if final[index][1] < final[index+1][1]:
                final[index], final[index+1] = final[index+1], final[index]
    return final


def mutual_friends_newtworks_points(person: str, person_to_friends: \
                                    Dict[str, List[str]], person_to_networks: \
                                    Dict[str, List[str]], potential_friends: \
                                    List[str], recommendation_dic: Dict[str,\
                                    List[str]])-> List[Tuple[str, int]]:
    '''
    Return the result of sendig the person, person_to_friends list,
    potential_friends list and the recommendation_dic dcitionary
    (after of adding a point to the potential friend's score in
    the dic dictionary if they have any mutual friends or if
    they belong to the same network network as the person
    based on the given person_to_friends and person_to_networks
    dictionaries) to the same_lname_point_and_sorting function.

    >>> x = {'Jay Pritchett': ['Claire Dunphy', 'Gloria Pritchett', \
            'Manny Delgado'], 'Claire Dunphy': ['Mitchell Pritchett', \
            'Jay Pritchett', 'Phil Dunphy'], 'Manny Delgado': \
            ['Gloria Pritchett', 'Jay Pritchett', 'Luke Dunphy'], \
            'Mitchell Pritchett': ['Cameron Tucker', 'Gloria Pritchett',\
            'Manny Delgado','Claire Dunphy', 'Luke Dunphy'], 'Alex Dunphy':\
            ['Luke Dunphy'], 'Cameron Tucker': ['Gloria Pritchett', \
            'Mitchell Pritchett'], 'Haley Gwendolyn Dunphy': ['Dylan D-Money',\
            'Gilbert D-Cat'], 'Phil Dunphy': ['Claire Dunphy', 'Luke Dunphy'],\
            'Dylan D-Money': ['Chairman D-Cat', 'Haley Gwendolyn Dunphy'], \
            'Gloria Pritchett': ['Cameron Tucker', 'Jay Pritchett', \
            'Manny Delgado'], 'Luke Dunphy': ['Manny Delgado','Phil Dunphy'], \
            'Mohammad Ahmed': ['Claire Dunphy']}
    >>> z = {'Claire Dunphy': ['Parent Teacher Association'], 'Manny Delgado':\
            ['Chess Club'], 'Mitchell Pritchett': ['Law Association'], \
            'Alex Dunphy': ['Chess Club', 'Orchestra'], 'Cameron Tucker': \
            ['Clown School', 'Wizard of Oz Fan Club'], 'Phil Dunphy': \
            ['Real Estate Association'], 'Gloria Pritchett': \
            ['Parent Teacher Association'], 'Jay Pritchett':\
            ['Parent Teacher Association','Chess Club','Orchestra', \
            'Clown School', 'Wizard of Oz Fan Club','Real Estate Association']}
    >>> potential_friends = ['Alex Dunphy', 'Cameron Tucker', 'Chairman D-Cat',\
                            'Dylan D-Money', 'Gilbert D-Cat', \
                            'Gloria Pritchett', 'Haley Gwendolyn Dunphy', \
                            'Luke Dunphy', 'Manny Delgado', 'Mohammad Ahmed']
    >>> recommendation_dic = {'Alex Dunphy': [], 'Cameron Tucker': [], \
                            'Chairman D-Cat': [], 'Dylan D-Money': [], \
                            'Gilbert D-Cat': [], 'Gloria Pritchett': [], \
                            'Haley Gwendolyn Dunphy': [], 'Luke Dunphy': \
                            [], 'Manny Delgado': [], 'Mohammad Ahmed': []}
    >>> mutual_friends_newtworks_points('Claire Dunphy', x, z, \
                                        potential_friends, recommendation_dic)
    [('Gloria Pritchett', 2), ('Luke Dunphy', 2), ('Cameron Tucker', 1), \
    ('Manny Delgado', 1)]

    >>> x = {'Lionel Messi': ['Cristiano Ronaldo'], \
            'Robert Luis' : ['Cristiano Ronaldo']}
    >>> z = {}
    >>> potential_friends = ['Cristiano Ronaldo', 'Lionel Messi']
    >>> recommendation_dic = {'Cristiano Ronaldo': [], 'Lionel Messi': []}
    >>> mutual_friends_newtworks_points('Robert Luis', x, z, potential_friends,\
                                        recommendation_dic)
    [('Lionel Messi', 1)]
     >>> x = {'George Messi': ['Cristiano Ronaldo', 'Mohammad Ali'], \
             'Robert Luis' : ['William Ronaldo', 'Mohammad Ali', \
             'Cristiano Ronaldo']}
    >>> z = {}
    >>> potential_friends = ['George Messi']
    >>> recommendation_dic = {'George Messi': []}
    >>> mutual_friends_newtworks_points('Robert Luis', x, z, potential_friends,\
                                        recommendation_dic)
    [('George Messi', 2)]
    '''

    friends_lst = []

    for key in person_to_friends:
            if key == person:
                for value in person_to_friends[key]:
                    if not (person_to_friends[key] in friends_lst):
                        friends_lst.append(value)

    for key in person_to_friends:
        if key in potential_friends:
             for index in person_to_friends[key]:
                 if index in friends_lst:
                        recommendation_dic[key].append(1)

    network_to_ppl = invert_network(person_to_networks)

    for key in network_to_ppl:
        for potenial in potential_friends:
            if potenial in network_to_ppl[key]and person in network_to_ppl[key]:
                    recommendation_dic[potenial].append(1)

    return same_lname_point_and_sorting(person, person_to_friends, \
                                        potential_friends, recommendation_dic)


def get_potential_friends(person: str, person_to_friends: Dict[str, List[str]],\
                         person_to_networks: Dict[str, List[str]], friends_lst:\
                          List[str]) -> List[Tuple[str, int]]:
    '''
    Return the result of sending the person, person_to_friends
    and person_to_networks dictionaries and the friends_lst as well
    as creating and sending a dictionary with all the person's
    potential friends as keys based the friends_lst list (a list of all the
    person's friends in the firstname-lastname form) and the given
    person_to_friends dictionary, to the mutual_friends_newtworks_points
    function.

    >>> x = {'Jay Pritchett': ['Claire Dunphy', 'Gloria Pritchett', \
            'Manny Delgado'], 'Claire Dunphy': ['Mitchell Pritchett', \
            'Jay Pritchett', 'Phil Dunphy'], 'Manny Delgado': \
            ['Gloria Pritchett', 'Jay Pritchett', 'Luke Dunphy'], \
            'Mitchell Pritchett': ['Cameron Tucker', 'Gloria Pritchett', \
            'Manny Delgado','Claire Dunphy', 'Luke Dunphy'], 'Alex Dunphy': \
            ['Luke Dunphy'], 'Cameron Tucker': ['Gloria Pritchett', \
            'Mitchell Pritchett'], 'Haley Gwendolyn Dunphy': ['Dylan D-Money',\
            'Gilbert D-Cat'], 'Phil Dunphy': ['Claire Dunphy', 'Luke Dunphy'],\
            'Dylan D-Money': ['Chairman D-Cat', 'Haley Gwendolyn Dunphy'], \
            'Gloria Pritchett': ['Cameron Tucker', 'Jay Pritchett', \
            'Manny Delgado'], 'Luke Dunphy': ['Manny Delgado','Phil Dunphy'], \
            'Mohammad Ahmed': ['Claire Dunphy']}
    >>> z = {'Claire Dunphy': ['Parent Teacher Association'], 'Manny Delgado':\
            ['Chess Club'], 'Mitchell Pritchett': ['Law Association'], \
            'Alex Dunphy': ['Chess Club', 'Orchestra'], 'Cameron Tucker': \
            ['Clown School', 'Wizard of Oz Fan Club'], 'Phil Dunphy': \
            ['Real Estate Association'], 'Gloria Pritchett': \
            ['Parent Teacher Association'], 'Jay Pritchett': \
            ['Parent Teacher Association','Chess Club','Orchestra', \
            'Clown School', 'Wizard of Oz Fan Club','Real Estate Association']}
    >>> get_potential_friends('Jay Pritchett', x, z, ['Claire Dunphy', \
                             'Gloria Pritchett', 'Manny Delgado'])
    [('Mitchell Pritchett', 4), ('Cameron Tucker', 3), ('Alex Dunphy', 2), \
    ('Phil Dunphy', 2), ('Luke Dunphy', 1), ('Mohammad Ahmed', 1)]
    >>> get_potential_friends('Lionel Messi', {'Lionel Messi': \
                             ['Cristiano Ronaldo'], 'Robert Messi' : \
                             ['Cristiano Ronaldo']}, {}, ['Cristiano Ronaldo'])
    [('Robert Messi', 2)]
    >>> get_potential_friends('Robert Luis', {'Lionel Messi': \
                             ['Cristiano Ronaldo'], 'Robert Luis' : \
                             ['Cristiano Ronaldo']}, {}, ['Cristiano Ronaldo'])
    [('Lionel Messi', 1)]
    '''

    recommendation_dic = {}
    potential_friends = []

    for name in person_to_friends:
            if not (name in friends_lst) and not (name in potential_friends)\
            and name != person:
                    potential_friends.append(name)
                    potential_friends.sort()
            for value in person_to_friends[name]:
                if not (value in friends_lst) and not \
                (value in potential_friends) and value != person:
                    potential_friends.append(value)
                    potential_friends.sort()

    for index in potential_friends:
        if not (index in recommendation_dic):
            recommendation_dic[index] = []

    return mutual_friends_newtworks_points(person, person_to_friends, \
                                           person_to_networks, \
                                           potential_friends, recommendation_dic)


def make_recommendations(person: str, person_to_friends: Dict[str, List[str]],\
                         person_to_networks: Dict[str, List[str]]) \
                         -> List[Tuple[str, int]]:
    '''
    Return a list of tuples of friend recommendations (sorted from highest
    to lowest score and alphabetically if the scores are equal) for the
    selected person based on the provided person_to_friends and
    person_to_networks dictionaries. The first element of the returned
    tuple is a potential friend's name (in the firstname-lastname form)
    and the second element is their score, a person is included in the
    list if and only if their score is greater than zero.

    >>> make_recommendations('Robert Ronald',{},{})
    []
    >>> x = {'Jay Pritchett': ['Claire Dunphy', 'Gloria Pritchett', \
            'Manny Delgado'], 'Claire Dunphy': ['Jay Pritchett', \
            'Mitchell Pritchett', 'Phil Dunphy'], 'Manny Delgado': \
            ['Gloria Pritchett', 'Jay Pritchett', 'Luke Dunphy'], \
            'Mitchell Pritchett': ['Cameron Tucker', 'Claire Dunphy', \
            'Luke Dunphy'], 'Alex Dunphy': ['Luke Dunphy'], 'Cameron Tucker': \
            ['Gloria Pritchett', 'Mitchell Pritchett'], \
            'Haley Gwendolyn Dunphy': ['Dylan D-Money', 'Gilbert D-Cat'], \
            'Phil Dunphy': ['Claire Dunphy', 'Luke Dunphy'], 'Dylan D-Money': \
            ['Chairman D-Cat', 'Haley Gwendolyn Dunphy'], 'Gloria Pritchett': \
            ['Cameron Tucker', 'Jay Pritchett', 'Manny Delgado'], \
            'Luke Dunphy': ['Alex Dunphy', 'Manny Delgado', \
            'Mitchell Pritchett', 'Phil Dunphy']}
    >>> z = {'Claire Dunphy': ['Parent Teacher Association'], \
            'Manny Delgado': ['Chess Club'], 'Mitchell Pritchett': \
            ['Law Association'], 'Alex Dunphy': ['Chess Club', 'Orchestra'], \
            'Cameron Tucker': ['Clown School', 'Wizard of Oz Fan Club'], \
            'Phil Dunphy': ['Real Estate Association'], 'Gloria Pritchett': \
            ['Parent Teacher Association']}
    >>> make_recommendations('Claire Dunphy',x, z)
    [('Luke Dunphy', 3), ('Gloria Pritchett', 2), ('Cameron Tucker', 1), \
    ('Manny Delgado', 1)]
    >>> make_recommendations('Lionel Messi',{'Lionel Messi': \
                            ['Cristiano Ronaldo'], 'Robert Messi': \
                            ['Cristiano Ronaldo']}, {})
    [('Robert Messi', 2)]
    >>> make_recommendations('Lionel Messi',{'Lionel Messi': \
                            ['Cristiano Ronaldo'], 'Robert Luis': \
                            ['Cristiano Ronaldo']}, {})
    [('Robert Luis', 1)]
    >>> x = {'Jay Pritchett': ['Claire Dunphy', 'Gloria Pritchett', \
            'Manny Delgado'], 'Claire Dunphy': ['Claire Dunphy', \
            'Jay Pritchett', 'Mitchell Pritchett', 'Phil Dunphy', \
            'moe ah'],'Manny Delgado': ['Gloria Pritchett', \
            'Jay Pritchett', 'Luke Dunphy', 'moe ah'], 'Gloria Pritchett': \
            ['Cameron Tucker', 'Jay Pritchett', 'Manny Delgado', 'moe ah']}
    >>> z =  {'Manny Delgado': ['Chess Club'], 'Cameron Tucker': \
             ['Clown School', 'Wizard of Oz Fan Club'], 'Gloria Pritchett': \
             ['Parent Teacher Association'], 'moe ahmed': \
             ['Parent Teacher Association', 'Law Association', 'Chess Club', \
             'Orchestra', 'Clown School', 'Wizard of Oz Fan Club', \
             'Real Estate Association']}
    >>> make_recommendations('Manny Delgado', x, z)
    [('Claire Dunphy', 2)]
    >>> x = {'Jay Pritchett': ['Claire Dunphy', 'Gloria Pritchett', \
            'Manny Delgado'], 'Claire Dunphy': ['Mitchell Pritchett', \
            'Jay Pritchett', 'Phil Dunphy'], 'Manny Delgado': \
            ['Gloria Pritchett', 'Jay Pritchett', 'Luke Dunphy'], \
            'Mitchell Pritchett': ['Cameron Tucker', 'Gloria Pritchett',\
            'Manny Delgado','Claire Dunphy', 'Luke Dunphy'], 'Alex Dunphy':\
            ['Luke Dunphy'], 'Cameron Tucker': ['Gloria Pritchett', \
            'Mitchell Pritchett'], 'Haley Gwendolyn Dunphy': \
            ['Dylan D-Money', 'Gilbert D-Cat'], 'Phil Dunphy': \
            ['Claire Dunphy', 'Luke Dunphy'], 'Dylan D-Money': \
            ['Chairman D-Cat', 'Haley Gwendolyn Dunphy'], \
            'Gloria Pritchett': ['Cameron Tucker', 'Jay Pritchett', \
            'Manny Delgado'], 'Luke Dunphy': ['Manny Delgado','Phil Dunphy'], \
            'Mohammad Ahmed': ['Claire Dunphy']}
    >>> z = {'Claire Dunphy': ['Parent Teacher Association'], 'Manny Delgado': \
            ['Chess Club'], 'Mitchell Pritchett': ['Law Association'], \
            'Alex Dunphy': ['Chess Club', 'Orchestra'], 'Cameron Tucker': \
            ['Clown School', 'Wizard of Oz Fan Club'], 'Phil Dunphy': \
            ['Real Estate Association'], 'Gloria Pritchett': \
            ['Parent Teacher Association'], 'Jay Pritchett':\
            ['Parent Teacher Association','Chess Club','Orchestra', \
            'Clown School', 'Wizard of Oz Fan Club','Real Estate Association']}
    >>> make_recommendations('Jay Pritchett', x, z)
    [('Mitchell Pritchett', 4), ('Cameron Tucker', 3), ('Alex Dunphy', 2), \
    ('Phil Dunphy', 2), ('Luke Dunphy', 1), ('Mohammad Ahmed', 1)]
    '''

    friends_lst = []

    for key in person_to_friends:
            if key == person:
                for value in person_to_friends[key]:
                    if not (person_to_friends[key] in friends_lst):
                        friends_lst.append(value)
    return get_potential_friends(person, person_to_friends,\
                                       person_to_networks, friends_lst)


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


##if __name__ == '__main__':
##    # Do not move this code out of the __main__ block, and do not add any other
##    # testing code outside of the __main__ block.
##    import doctest
##    doctest.testmod()
