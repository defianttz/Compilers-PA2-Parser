# Compilers-PA1-Lexer
By: Sammy, Liam

# Introduction
This is a brief guide on how to setup and run the lexical_anlyzer.py. 
The program takes an input from the console and produces an output accordingly.

# How to run
Usage: python3 lexical_analyzer.py <source_code_file>

# Example
```
python3 lexical_analyzer.py .\input_sourcecode.txt
```

Output from lexical analyzer
```
tokens          lexemes
________________________
KEYWORD          int
IDENTIFIER       main
Seperator        (
Seperator        )
Seperator        {
KEYWORD          for
Seperator        (
KEYWORD          int
IDENTIFIER       i
Operator         =
INTEGER          22
Punctuation      ;
IDENTIFIER       i
Operator         <=
INTEGER          100
Punctuation      ;
IDENTIFIER       i
Operator         =
IDENTIFIER       i
Operator         +
INTEGER          1
Seperator        )
Seperator        {
KEYWORD          while
Seperator        (
IDENTIFIER       i
Operator         ==
INTEGER          100
Seperator        )
Seperator        {
KEYWORD          cout
Operator         <<
STRING   "Hello World!"
Operator         <<
IDENTIFIER       endl
Punctuation      ;
COMMENT          //print out

Seperator        }
Seperator        }
KEYWORD          return
INTEGER          0
Punctuation      ;
Seperator        }
***
