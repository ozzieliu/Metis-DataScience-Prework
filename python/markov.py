#!/usr/bin/env python
# encoding: utf-8

# Write a Markov text generator, [markov.py](python/markov.py). Your program should be called from the command line with two arguments: the name of a file containing text to read, and the number of words to generate. For example, if `chains.txt` contains the short story by Frigyes Karinthy, we could run:
# ```bash
# ./markov.py chains.txt 40
# ```

## Available text for Markov generator:
## - emma.txt (Jane Austen's Emma)
## - eric.txt (Song "Eric, half a bee")
## - delcaration.txt (The Delcaration of Independence)

## Currrently, we are stripping all words from the original text of punctuation and converting it all to lowercase.
## The output would be a string of words of the desired length
## While the desired suffix length is currently set to 3. (1 word + 2 subsequent words). This can be changed in the main function.

## Next steps would be to factor in capitalized words and punctuation.

### Code for creating a histogram of each word in the text:
import string
import random
import sys

### Code to make a dictionary of subsequent words
### Takes input of file name and prefix length
def create_word_dict(filename, prefix_length):
    word_list = []
    word_dict = {}

    ## Open the file...
    with open(filename, "r") as text:
        ## And read each line in text file and store it in an ordered list of all words
        for line in text:
            for word in line.split():
                word = word.strip(string.punctuation + string.whitespace).lower()
                word_list.append(word)

    ## Go through the word list word and make a dictionary of each words' subsequent words
    for index, word in enumerate(word_list):
        ## For each word before the last few
        if index < len(word_list)-prefix_length+1:
            if word not in word_dict:
                word_dict[word] = [word_list[index+1:index+prefix_length]]
            elif word in word_dict:
                word_dict[word].extend([word_list[index+1:index+prefix_length]])

        ## For the last few words
        else:
            ## Add an empty string for the last word if it's not in the dict yet
            if index == len(word_list)-1:
                if word not in word_dict:
                    word_dict[word] = ['']
            ## For the few words before the last one
            else:
                if word not in word_dict:
                    word_dict[word] = [word_list[index+1:]]
                elif word in word_dict:
                    word_dict[word].extend([word_list[index+1:]])

    #print word_dict
    return word_dict

def markov_generator(dictionary, length):
    ## First word:
    text = random.sample(dictionary.keys(), 1)
    #print text


    ## Iterate through subsequent n words:
    while len(text) < length:
        ## find the new word to add:
        new_word = random.sample(dictionary[text[-1]], 1)[0]
        #print new_word
        ## Add that list to the text
        text.extend(new_word)

    ## Cut off additional words if exceeding length limit
    if len(text) > length:
        text = text[:length]

    #print len(text)
    return " ".join(text)

## Main section
def main(argv):
    my_dict = create_word_dict(sys.argv[1], 3)
    #print type(sys.argv[1]), type(sys.argv[2])
    print markov_generator(my_dict, int(sys.argv[2]))

if __name__ == "__main__":
    main(sys.argv[1:])
