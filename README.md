# Compilers-PA2-Parser
**Authors:** Sammy, Liam

# Introduction
This project implements an arithmetic expression parser in Python. The input expression is tokenized by the Lexer. The parser is built using the principles of left recursive descent parsing. 

## Grammar Transformation
The given grammar `G` is transformed into a revised grammar `G'`.

**Given Grammar (G):**

    E → E + T | E – T | -E | T
    T → T * F | T/F | F
    F → int | (E)

**Revised Grammar (G'):**

    E -> TE' | - E E’		
    E' -> + TE' | - TE' | ε	
    T -> FT'		
    T' -> * FT' | / FT' | ε
    F -> int | (E)


## Usage
Run the parser with the following command:

    python3 .\recursive_descent_parser.py

### Run-time Instructions

1. Choose whether to display the parser productions (for debug or visualization)
    ```
    Show the parsing productions? (y or n)
    n
    ```
2. Enter the expression and view the result
    ```
    Enter the expression: (type 'exit' to leave')
    (5 + 5)/2
    Result = 5.0
    ```
3. Enter `exit` to leave the program
    ```
    Enter the expression: (type 'exit' to leave')
    exit
    ```
#

## Requirements
- Python 3.x

## Example Input/Output
**Example 1:**

    Show the parsing productions? (y or n)
    n

    Enter the expression: (type 'exit' to leave')
    3+5 
    Expression valid
    Result = 8

**Example 2:**

    Show the parsing productions? (y or n)
    n
    Enter the expression: (type 'exit' to leave')
    3+5/ 
    Error: Entered expression is invalid

**Example 3: With Productions**

1. Choose whether to display the parser productions (for debug or visualization)
    ```shell
    Show the parsing productions? (y or n)
    y
    ```
2. Enter the expression and view the result
    ```shell
    Enter the expression: (type 'exit' to leave')
    7*(5-3)/2
    ```
3. View the parsing productions
    ```shell
    Tokens: ['int', '*', '(', 'int', '-', 'int', ')', '/', 'int']
    ```
    | Stack                | Input                | Action               |
    |----------------------|----------------------|----------------------|
    | $E                   | int*(int-int)/int$   | E->T E'              |
    | $E'T                 | int*(int-int)/int$   | T->F T'              |
    | $E'T'F               | int*(int-int)/int$   | F->int               |
    | $E'T'int             | int*(int-int)/int$   | match int            |
    | $E'T'                | *(int-int)/int$      | T'->* F T'           |
    | $E'T'F*              | *(int-int)/int$      | match *              |
    | $E'T'F               | (int-int)/int$       | F->( E )             |
    | $E'T')E(             | (int-int)/int$       | match (              |
    | $E'T')E              | int-int)/int$        | E->T E'              |
    | $E'T')E'T            | int-int)/int$        | T->F T'              |
    | $E'T')E'T'F          | int-int)/int$        | F->int               |
    | $E'T')E'T'int        | int-int)/int$        | match int            |
    | $E'T')E'T'           | -int)/int$           | T'->ε                |
    | $E'T')E'             | -int)/int$           | E'->- T E'           |
    | $E'T')E'T-           | -int)/int$           | match -              |
    | $E'T')E'T            | int)/int$            | T->F T'              |
    | $E'T')E'T'F          | int)/int$            | F->int               |
    | $E'T')E'T'int        | int)/int$            | match int            |
    | $E'T')E'T'           | )/int$               | T'->ε                |
    | $E'T')E'             | )/int$               | E'->ε                |
    | $E'T')               | )/int$               | match )              |
    | $E'T'                | /int$                | T'->/ F T'           |
    | $E'T'F/              | /int$                | match /              |
    | $E'T'F               | int$                 | F->int               |
    | $E'T'int             | int$                 | match int            |
    | $E'T'                | $                    | T'->ε                |
    | $E'                  | $                    | E'->ε                |
    | $                    | $                    | match $              |