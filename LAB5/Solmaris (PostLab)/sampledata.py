
# Get names
def getNames():
    f_names = open('names_list.txt')
    names_list = []
    for name in f_names:
        names_list.append(name.strip())
    return names_list

# Get last names
def getlastnames():
    l_names = open('last_names_list.txt')
    last_name_list = []
    for l_name in l_names:
        last_name_list.append(l_name.strip())
    return last_name_list
    
# Get states
def getstates():
    state_file = open('state_list.txt')
    state_list = []
    for state in state_file:
        state_list.append(state.strip())
    return state_list

# Get ctities
def getcity():
    city_file = open('city_list.txt')
    city_list = []
    for city in city_file:
        city_list.append(city.strip())
    return city_list


