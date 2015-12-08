## Advanced Python
## Regular Expressions

import csv
import re
from collections import Counter

# Read given file and return a list of lists for each row:
def read_data(filename):
    with open(filename, 'rb') as csvfile:
        content = csv.reader(csvfile)
        # Ignore the first line header in the csv file
        next(content)
        # Store the read csv data into a list of list.
        return list(content)


# This function takes the written data of faculty listing as input,
# find degrees that matches 2 regular expressions that captures
# various form of degree suffixes, and return the number of unique degrees
def find_degrees(data):
    degree_list = []

    for line in data:
        #print line

        ## Find all strings that have 1 or 2 characters followed by a period that
        ## repeats 2 to 3 times, and add them to my list of degrees.
        ## This willl capture degrees such as Ph.D., Ph.D, and B.S.ED.
        degree_list.extend(re.findall(r'\b((?:[\w]{1,2}[.]){2,3})\W', str(line)))

        ## Also add strings that are 1 uppercase letter followed by combo of
        ## 1 upper, 1 lower + 1 upper, or 2 uppercase letters.
        ## e.g.: JD, MD, PhD, ScD, MPH
        degree_list.extend(re.findall(r'\b[A-Z][a-z]{0,1}[A-Z]{1,2}', str(line)))

    ## Now I have the issue where the same degrees are punctuated differently.
    ## To try to capture all of variations, I change the list into all uppercase
    ## and strip any periods.
    formatted_list = [x.upper() for x in degree_list]
    formatted_list = [re.sub(r'\.', '', x) for x in formatted_list]
    #print formatted_list

    ## Now use collections Counter to find and count the unique degrees.
    degree_count = Counter(formatted_list)

    ## Print the number of different degrees in a given list
    print 'Number of different degrees: ', len(set(degree_count))

    ## Print the degrees with their frequencies
    print degree_count


## This function takes the written data of faculty listing as input,
## find titles that matches 1 regular expressions that captures
## various type of titles, and return the number of unique titles.
def find_titles(data):
    title_list = []

    for line in data:
        ## Use regex to find all titles and add them to the list. We know that
        ## titles end in Biostatistcs and will include any typos.
        title_list.extend(re.findall(r'(\b(?:(?:\w+\s){0,3})Biostatistics)', str(line)))

    ## Find all unique titles and return the number of unique titles.
    title_count = Counter(title_list)

    ## Print the number of different titles in the list
    print 'Number of different titles: ', len(set(title_count))

    ## Print the titles with their frequencies
    print title_count


## This function takes the written data of faculty listing as input,
## find email address with a regular expressions and return a list of all email addresses.
def search_for_email(data):
    email_list = []

    for line in data:
        #print line
        #print re.findall(r'(\w+@(?:(?:\w+.){2,4}))\W', str(line))

        email_list.extend(re.findall(r'(\w+@(?:(?:\w+.){2,4}))\'', str(line)))


    return email_list

# This function takes the data of faculty listing as input, calls the search_for_email
# function to get a list of email address and then use regular expressions to
# isolate the email domains, and return an unique set of domains
def number_of_domains(data):
    email_list = search_for_email(data)
    domain_list = []
    for email in email_list:
        domain_list.extend(re.findall(r'@((?:\w+.){2,4})', email))

    domain_set = set(domain_list)
    print len(domain_set)
    return domain_set

## Main function area:
faculty = read_data('faculty.csv')
find_degrees(faculty)
find_titles(faculty)
print 'List of faculty emails: ', search_for_email(faculty)
print 'List of all unique domains: ', number_of_domains(faculty)
