# Compilers-PA2-Parser
By: Sammy, Liam

##Rewritten grammar G into G’

G = {
E → E + T | E – T | -E | T
T → T * F | T/F | F
F → int | (E)
}

G’= {
E -> TE' | - E E’		
E' -> + TE' | - TE' | ε	
T -> FT'		
T' -> * FT' | / FT' | ε
F -> int | (E)
}



# Introduction
This project implements an arithmetic expression parser in Python. The input expression is tokenized by the Lexer. The parser is built using the principles of left recursive descent parsing. 

# How to Run
Usage: python3 .\recursive_descent_parser.py

## Requirements
Python 3.x

# Example Input/Output
Ex 1)
Enter the expression: (type 'exit' to leave')
3+5 
Expression valid
Result = 8

Ex 2)
Enter the expression: (type 'exit' to leave')
3+5/ 
Error Entered expression is invalid
