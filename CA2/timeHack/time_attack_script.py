# -*- coding: utf-8 -*-
import time
from time_password_checker import check_password
import statistics

class solution():
    def __init__(self) -> None:
        # DO NOT MODIFY THE EXISTED PROPERTY
        # You can add as many properties as you need
        self.password = ""                                              # This is where your guessed password is store
     
    def example(self):
        # The following shows how to get the time spent
        # You can modify it to test your ideas
        
        # If password is correct, check_password will return Correct
        # If password is wrong, check_password will return Wrong
        
        T1 = time.perf_counter()
        result = check_password(self.password)
        T2 = time.perf_counter()
        
        # You can print the output for debug or test.
        print(result)
        print("time spend: ", T2-T1)
        
    # method to analyze the dictionary of data values returned for a particular position in the password 
    def get_stats(self, data):
        char_dict = {}

        # calculate the mean, median and mode of the data values for each character
        for char, value in data.items():
            mean_value = statistics.mean(value)
            med_value = statistics.median(value)
            try:
                mod_value = statistics.mode([int(v*100) for v in value])
            # handle the cases when a single mode does not exist (since typecasted to int) 
            except statistics.StatisticsError:
                mod_value = mean_value
            char_dict[char] = [mean_value, med_value, mod_value]

        # find the character with the highest mean, median and mode
        win_mean = max(char_dict, key=lambda key: char_dict[key][0])
        win_median = max(char_dict, key=lambda key: char_dict[key][1])
        win_mode = max(char_dict, key=lambda key: char_dict[key][2])

        # from the winning characters, find the one occuring the most, otherwise the one with highest numerical time value
        winner = max([win_mean, win_median, win_mode], key=lambda key: (char_dict[key][0], char_dict[key][1], char_dict[key][2]))

        # print(win_mean, win_median, win_mode, winner)
        return winner

    def getPassword(self):
        # Please complete this method
        # It should be the return the correct password in a string
        # GradeScope will import your class, and call this method to get the password you calculated.
        # pass

        # run method for each position n_iter times
        n_iter = 300
        guessPass = ""

        # flag variable to break out of the method when password is found
        found = False

        # maximum length of the password can be 11
        for x in range(12):

            # initializing a character dictionary to store all the time difference values
            max_char = {}
            for c in range(33,127):
                max_char[chr(c)] = []

            # run for n iterations to remove noise
            for _ in range(n_iter):
                
                # try each of the ASCII characters from ! to ~ for the particular position in the password
                for i in range(33,127):
                    T1 = time.perf_counter()
                    result = check_password(guessPass+chr(i))
                    T2 = time.perf_counter()    
                    # break out of this method as soon as 'Correct' is returned by the password checker
                    if(result == "Correct"):
                        guessPass+=chr(i)
                        self.password = guessPass
                        return self.password
                    
                    #store all the values in a dictionary to perform statistical analysis
                    max_char[chr(i)].append((T2-T1)*(100000))
            
            # find the statistically most likely character for that index in the password
            winner_char = self.get_stats(max_char)        
            
            # print("winner after ",x," : ",winner_char)
            guessPass += winner_char

        # print(guessPass)
        self.password = guessPass
        return self.password
    
    
# Write Up
# Please explain your solution
    
# The side channel employed in this attack the absence of any delay in returning the output by a password checker function.
# The later the output is returned, statistically the correct would be the test password.

# In order to attack this noisy system,
# each character is tested as a potential password, and the one with maximum time difference between input and output is deemed 
# the winner at that index in the password.
# In order to remove any noise from the system, each combination is tried for 300 iterations, and a statistical analysis perfomed
# on the time values to find the most likely password combination.

# Statistical analysis:
# For each character, there are n time values stored. The maximum time value would be the winner.
# To find this, mean, median and mode is taken for all the values. For mode, the value is typecasted to an integer to reduce the 
# resolution and have a higher probabalisitc estimate.
# For each of the three methods, a winner character is available. Out of the three characters, the one occuring most times is 
# deemed the winner, otherwise the one with highest numerical value (in order of mean, median and mode) is chosen.
    
# For a more accurate guess, the number of iterations needed should be increased.
    
mySol = solution()
# mySol.example()
myPass = mySol.getPassword()
print(myPass)