# Desc: Recursive descent parser for the language
import sys

from Lexer.lexical_analyzer import lexer

if __name__ == "__main__":


    while True:
        expression = input("Enter the expression: (type 'exit' to leave')\n")
        if expression == "exit":
            break
        else:

            # Access the tokens from the lexer
            tokens = lexer(expression)
            print(tokens)









