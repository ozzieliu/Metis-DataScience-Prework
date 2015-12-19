## Dict - part 1
## Last name (string): list of lists:[degrees, title, email]

from advanced_python_regex import read_data
import re
import operator
import pprint

faculty = read_data('faculty.csv')

def professor_dictionary(faculty):
    faculty_dict = {}
    # for each row, gotta get first/last name, degree, title, and email address
    # Each row in file is already for each faculty member
    for person in faculty:
        last_name = person[0].split()[-1]

        degree = re.sub(r'^\W', '', person[1])
        title = re.match(r'\b((?:\w+ ){0,1}(?:\w+)) \w+ Biostatistics', person[2]).group(1)
        email = person[3]
        value = [degree, title, email]

        ## OK, what if the key already exists?
        if last_name in faculty_dict:
            #print type(faculty_dict[last_name])
            faculty_dict[last_name].append(value)
        else:
            faculty_dict[last_name] = [value]

    return faculty_dict


def better_dictionary(faculty):
    faculty_dict = {}
    # for each row, gotta get first/last name, degree, title, and email address
    # Each row in file is already for each faculty member
    for person in faculty:
        last_name = person[0].split()[-1]
        first_name = person[0].split()[0]
        name = (first_name, last_name)
        #print name

        degree = re.sub(r'^\W', '', person[1])
        title = re.match(r'\b((?:\w+ ){0,1}(?:\w+)) \w+ Biostatistics', person[2]).group(1)
        email = person[3]
        value = [degree, title, email]

        faculty_dict[name] = value

    return faculty_dict



## Main area:
#Q1
#pprint.pprint(professor_dictionary(faculty))
#Q2
part2_dict = better_dictionary(faculty)
#pprint.pprint(part2_dict, width = 200)

sorted_dict = sorted(part2_dict.items(), key = lambda x: x[0][1])

pprint.pprint(sorted_dict)
