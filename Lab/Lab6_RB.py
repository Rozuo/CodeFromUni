# Code by: Ross Beaudin
# ID# 3048109
# Lab# 6

# Purpose: This function will take a file name and open the file for reading
# and takes the content of said file into a list while cleaning up unnecessary 
# spaces.
# Parameters: file_name - A string of a file name
# return: name_list
def open_file(file_name):
    try:
        file = open(file_name, "r")
    except:
        print("The file", file_name, "does not exist or is not readable.")
        return None
    file_list = file.readlines()
    name_list = []
    
    for name_spec in file_list:
        name = name_spec.split()
        for i in range(2):
            name_list.append(name[i])
            
    return name_list

# Purpose: This function takes the name list and builds a dictionnary from said 
# list.
# Parameters: names - the list of names
# Return: name_dict
def build_dict(names):
    name_dict = {}
    count = 0   #initiate counts
    for i in range(1, len(names), 2):
        name_dict[names[i].lower()] = names[count]
        count += 2
    return name_dict

# create a helper function for all astericts  at the start the middle and end
# split words that have astericts in the middle kel*ly

# Purpose: The purpose of this function is to look for letters that are after 
# the asterisk and give the names that apply to said criteria
# Parameters: 
# boy_name_list - list of boy names that apply to the name requested
# girl_name_list - list of girl names that apply to the name requested
# boy_dict - a dictionary of the boy names
# girl_dict - a dictionary of the girl names
# name_request - the name requested by the user
# return: boy_name_list and girl_name_list
def starts_with_asterisk(boy_name_list, girl_name_list, boy_dict, girl_dict, name_request):
    name_req_list = list(name_request)
    name_req_list.remove("*")
    endwith = "".join(name_req_list)
    
    for key in boy_dict.keys():
        if key.endswith(endwith):
            boy_name_list.append([key, boy_dict[key]])
    for key in girl_dict.keys():
        if key.endswith(endwith):
            girl_name_list.append([key, girl_dict[key]])  
            
    return None

# Purpose: The purpose of this function is to look for letters that are before 
# the asterisk and give the names that apply to said criteria
# Parameters: 
# boy_name_list - list of boy names that apply to the name requested
# girl_name_list - list of girl names that apply to the name requested
# boy_dict - a dictionary of the boy names
# girl_dict - a dictionary of the girl names
# name_request - the name requested by the user
# return: boy_name_list and girl_name_list    
def ends_with_asterisk(boy_name_list, girl_name_list, boy_dict, girl_dict, name_request):
    name_req_list = list(name_request)
    name_req_list.remove("*")
    startwith = "".join(name_req_list)
    
    for key in boy_dict.keys():
        if key.startswith(startwith.lower()):
            boy_name_list.append([key, boy_dict[key]])
    for key in girl_dict.keys():
        if key.startswith(startwith.lower()):
            girl_name_list.append([key, girl_dict[key]])
            
    return None

# Purpose: The purpose of this function is to look for letters that are before 
# and after the asterisk and give the names that apply to said criteria
# Parameters: 
# boy_name_list - list of boy names that apply to the name requested
# girl_name_list - list of girl names that apply to the name requested
# boy_dict - a dictionary of the boy names
# girl_dict - a dictionary of the girl names
# name_request - the name requested by the user
# return: boy_name_list and girl_name_list
def asterisk_in_middle(boy_name_list, girl_name_list, boy_dict, girl_dict, name_request):
    start_and_end = name_request.split('*')
    start = start_and_end[0].lower()
    end = start_and_end[1]
    for key in boy_dict.keys():
        if key.startswith(start) and key.endswith(end):
            boy_name_list.append([key, boy_dict[key]])
    for key in girl_dict.keys():
        if key.startswith(start) and key.endswith(end):
            girl_name_list.append([key, girl_dict[key]])    
    return None    

# Purpose: This function calls asterisk_in_middle, ends_with_asterisk and starts_with_asterisk and determines how many names are in the two dictionaries
# Parameters: 
# boy_dict - A boy dictionary
# girl_dict - A girl dictionary
# name_request - The name requested by the user
# Return: boy_var and girl_var
def how_many(boy_dict, girl_dict, name_request):
    boy_var = []
    girl_var = []
    if name_request.startswith('*'):
        starts_with_asterisk(boy_var, girl_var, boy_dict, girl_dict, name_request)
    elif name_request.endswith('*'):
        ends_with_asterisk(boy_var, girl_var, boy_dict, girl_dict, name_request)
    elif str((name_request.find("*"))).isdigit():
        asterisk_in_middle(boy_var, girl_var, boy_dict, girl_dict, name_request)
    else:
        try:
            boy_name_rep = [name_request, boy_dict[name_request.lower()]]
            boy_var.append(boy_name_rep)
        except:
            None
        try:
            girl_name_rep = [name_request, girl_dict[name_request.lower()]]
            girl_var.append(girl_name_rep)
        except:
            None
    return boy_var, girl_var
# Purpose: This function prints out how many times the a requested name was 
# given to a baby.
# Parameters: 
# baby_boy - list of baby boy names and the amount of the names given
# baby_girl - list of baby girl names and the amount of the names given
# requested_name - The requested name by the user
# Return: None
def print_counts(baby_boy, baby_girl, requested_name): #baby_name_list
    if baby_boy==[] and baby_girl==[]:
        print("\n\tThere were no babies named",
              requested_name.title(), "in 2016\n")
        return None
    if baby_boy==[]:
        #print()
        print("\nBaby boys\n\tNone\n")
    else:
        print("\nBaby boys")
        #for i in range(len(baby_boy)):
        for item in baby_boy:
            print("\t"+item[0].title(), item[1])
    print()
    if baby_girl==[]:
        print("Baby girls\n\tNone\n")
    else:
        print("Baby girls")
        #for i in range(len(baby_girl)):
        for item in baby_girl:
            print("\t", item[0].title(), item[1])
        print()
    return None

# Purpose: This function calls all the previous functions and ask the user to
# input a name to search and how many times it's been given to babies. If the 
# user inputs 'Q' the program will exit else it will continue asking for names.
# Parameters: None
# Return: None
def main():
    boys_name_list = open_file('2016_Boys.txt')
    girls_name_list = open_file('2016_Girls.txt')
    print("\nAlberta 2016 Baby Name Search\n")
    while True:
        name_request = input("""Enter a name to see how many babies were given that name
in Alberta in 2016. An asterix may be used to indicate 
unknown letters (enter "Q" to quit):

\t""")
        if name_request.lower()=='q':
            print("Goodbye")
            break
        boys_dict = build_dict(boys_name_list)
        girls_dict = build_dict(girls_name_list)
        baby_boy, baby_girl = how_many(boys_dict, girls_dict, name_request)
        print_counts(baby_boy, baby_girl, name_request)
    return None