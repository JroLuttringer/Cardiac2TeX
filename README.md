# Cardiac2TeX

Cardiac2Tex is a simple python program. Given a Cardiac program Input (represented as three arrays: the input, the output and the memory), Cardiac2TeX creates one beamer slide per step to showcase in detail the inner workings of Cardiac. 

The TeX source is printed on the standard output and needs to be redirected to a file if needed. Once done, a simple *pdflatex file* should do the trick in order to get your slide (the LateX compilation is not done by Cardiac2TeX).

# Example 

You can run the program as-is (python3 main.py > example.tex), and then compile the file (pdflatex example.tex) to see 
how Cardiac2TeX translate a simple Cardiac program that computes the sum of 3 numbers.

# Files
## main.py
Contains the main loop that creates the TeX output.
## cardiac.py 
Contains the Cardiac class, which is a representation of the Cardiac computer.
## const.py 
Contains some constants, such as the array containing the Cardiac instruction traductions and the TeX header.
## trad_latex.py
This module is in charge of translating the current state of the Cardiac class to a beamer frame.

# Notes 
Some bugs might still be hidden within the code and there is a lot of room for improvement, but it kinda works !
