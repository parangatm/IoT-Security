# Secure and Trustworthy Edge Computing Systems
Coding Assignments for the Secure and Trustworthy Edge Computing Systems class at UCLA in W24 Quarter

[Class Website](https://ssysarch.github.io/ECE_209AS/W24/index.html)

## CA1 - 
[Problem Statement](https://docs.google.com/document/d/1MZKMlGGf100Yp8VwamhDrhcWGSY8oW1mFhgL2KKpDJs/edit)

This assignment introduced the basics of traditional encyrption mechanisms, which are now rendered insecure. It includes implementation of basic ciphers such as Fixed XOR, Single-Byte XOR, Single-Character XOR and Repeating-key XOR. The final part involved breaking repeated-key XOR cipher, the step-by-step approach to which is as follows - 

1. Finding the optimum keysize 
- Divide the ciphertext into slices of keysize length
- For each consecutive slice, calculate the hamming distance between them and normalize it by dividing it with keysize 
- Find the minimum averaged normalized hamming distance and the associated keysize for it

2. Breaking the ciphertext into slices of this guessed keysize length
- Pad the slice with zeros which has fewer number of bytes compared to the other slices (mostly the last slice)

3. Transposing the blocks
- Collect the first byte of each block into first, second byte into second - giving total keysize transposed blocks

4. Solving each block
- Use the single-character XOR cipher function declared in step 3 to find the decoded message with highest English score.
- Best-looking histogram here means the the message which makes a meaninful English sentence
- The key from each of the transposed block is collected

5. Constructing the key
- Concatentate the keys deduced into a single string, and converting it to ascii gives the key

## CA2 - 
[Problem Statement](https://docs.google.com/document/d/1MHAq4nWg8aXMfH0dsgKLeCtkB6RZtNRUFHhPU5qIG3I/edit)

This assignment focused on using side channels to reveal secret information from the communication channel. It had two parts - Memory-Based Side Channel and Time-Based Side Channel attacks. 

### Memory Attack
The side channel utilized in this problem is the fact that length of input string is not compared against the password, but each character is checked with the corresponding character in the password.

To guess each character, the program memory after the position being guessed is blocked. Each of the potential characters are then tested as the password for that position.

The three output scenarios are - 
1. 'Wrong' - The character is not correct for that position in password, and to keep guessing further.
2. 'SEG ERROR' - The character guessed is correct for that position. But after that it accessed the restricted part, meaning there are more characters in the password
3. 'Correct' - The character guessed is correct for that position, and the whole password is guessed, no further step needed.
        
Character 1 - blocked range [1,1023]
```
index:        0-1---------------------------------------------------------------------1023
access type:  |-|--------------------------cannot be accessed----------------------------|
value:        l\0#########################################################################
```

Character 2 - blocked range [2,1023]
```
index:        0--2---------------------------------------------------------------------1023
access type:  |--|--------------------------cannot be accessed----------------------------|
value:        lW\0#########################################################################
```
...

until 

Character 20 - blocked range [20,1023]
```
index:        0------------------20----------------------------------------------------1023
access type:  |-----accessible----|-----------------cannot be accessed--------------------|
value:        lWabcdefghop072ak~2z\0#######################################################
```
### Time Attack

The side channel employed in this attack the absence of any delay in returning the output by a password checker function. The later the output is returned, statistically the correct would be the test password.

In order to attack this noisy system, each character is tested as a potential password, and the one with maximum time difference between input and output is deemed the winner at that index in the password.

In order to remove any noise from the system, each combination is tried for 300 iterations, and a statistical analysis perfomed on the time values to find the most likely password combination.

**Statistical analysis**:

For each character, there are n time values stored. The maximum time value would be the winner. To find this, mean, median and mode is taken for all the values. For mode, the value is typecasted to an integer to reduce the resolution and have a higher probabalisitc estimate.

For each of the three methods, a winner character is available. Out of the three characters, the one occuring most times is deemed the winner, otherwise the one with highest numerical value (in order of mean, median and mode) is chosen.
    
For a more accurate guess, the number of iterations needed should be increased.

## CA3 - 
[Problem Statement](https://docs.google.com/document/d/1dBM1COEOprisRYCKV1poe2jzyVcSY5w_wcNj5Lpy_ng/edit)

A static binary analysis tool was created in this assignment, which could parse a C++ or Assembly program and create the control flow graph.

## CA4 - 
[Problem Statement](https://docs.google.com/document/d/1uXCt5q11kCvqiUvMvDL8GB_41Z7ht2r3UnFFqZtOy54/edit)

In this assignment, software-based remote attestation was studied. A simple attestation protocol with verifier and prover, and an attack scenario with and without noisy communication channel were designed. 

**Verifier**: Creates a nonce, sends the nonce to the prover function, and invokes it. Once the response is received, it locally computes the hash itself and compares it with the response. It passes the test if the two hashes are equal. 

**Prover**: It takes the nonce, reads the memory line-by-line, and computes the hash. It returns the final hash value. 
