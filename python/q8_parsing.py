# -*- coding: utf-8 -*-
# The football.csv file contains the results from the English Premier League.
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of
# goals scored for and against each team in that season (so Arsenal scored 79 goals
# against opponents, and had 36 goals scored against them). Write a program to read the file,
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.


import csv

# Open the given file to read and return a list of tuples
def read_data(data):
    with open(data, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        # Ignore the first line header in the csv file
        next(reader)
        # Store the read csv data into a list of tuples. Each tuple represent 1 line.
        return map(tuple, reader)

# Takes an input of the read data, and return the team index with the smallest difference
# I take it that the "smallest difference" in score differential means that the for and against are closest,
#   not that there is the lowest or worst differential

def get_min_score_difference(parsed_data):
    # Set team index and score difference variables to the data in the first team in the file.
    team_index = 0
    smallest_difference = abs(int(parsed_data[0][5])-int(parsed_data[0][6]))

    # Iterate through the other teams to see which team is worse.
    for team in parsed_data:
        difference = abs(int(team[5])-int(team[6]))
        if difference < smallest_difference:
            smallest_difference = difference
            team_index = parsed_data.index(team)

    return get_team(team_index, parsed_data)

# Given the index value of the team in the parsed data, return the team name
def get_team(index_value, parsed_data):
    return parsed_data[index_value][0]

# Main function area to call the functions.
football = read_data('football.csv')
print get_min_score_difference(football)
