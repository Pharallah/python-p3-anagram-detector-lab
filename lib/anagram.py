# your code goes here!
import ipdb

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, input_list):
        # Split self.word into a list of its letters
        init_word = [char for char in self.word]
        
        # Split every element in the input_list
        split_strings = [[char for char in word] for word in input_list]

        # Iterate thru split_strings & if there's a match, turn into str and save in a list
        matches = ["".join(word) for word in split_strings if sorted(word) == sorted(init_word)]

        return matches

