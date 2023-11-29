# Desc: Recursive descent parser for the language
import sys

from Lexer.lexical_analyzer import lexer
debug = False

# Table for the recursive descent parser
ll1_table = {
    # NT: int, (, ), +, -, *, /, $
    "E": {"int": "T E'",
          "(": "T E'",
          "-": "- E E'"},
    "E'": {"+": "+ T E'",
           "-": "- T E'",
           ")": "ε", "$": "ε"},
    "T": {"int": "F T'",
          "(": "F T'"},
    "T'": {"+": "ε",
           "-": "ε",
           "*": "* F T'",
           "/": "/ F T'",
           ")": "ε",
           "$": "ε"},
    "F": {"int": "int",
          "(": "( E )"}
}

non_terminals = ["E", "E'", "T", "T'", "F"]



def llparser(tokens):
    """
    Recursive descent parser for the language
    :param tokens: list of tokens
    :return: True if the expression is accepted, False otherwise

    """

    stack = []  # Stack to store the tokens
    stack.append("$")
    stack.append("E")  # Push the start symbol
    tokens.append("$")  # Push the end of input symbol
    terminals = ["(", ")", "+", "-", "*", "/", "int", "$"]

    # debug output
    if debug:
        print("{:<40}{:<80}{:<40}".format("Stack", "Input", "Action"))
        print("------------------------------")
    
    while len(stack) > 0:
        # x = top of stack
        # a = next input token
        # if x is in T (terminals)
        #   if x==a then pop x and go to the next input token
        #       else error
        # else if x is in N (non-terminals)
        #   if Table[x,a] is not empty
        #      pop x and push Table[x,a] onto the stack
        #   else error
        # end

        x = stack[-1] # Get the top of the stack
        a = tokens[0] # Get the next input token

        # print(f"x: {x}, a: {a}")
        # print(f"stack: {stack}  tokens: {tokens}\n")
        # print without the brackets
        
        if debug:
            stack_str = ""
            stack_str = "".join(stack)
            tokens_str = ""
            tokens_str = "".join(tokens)

        if x in terminals:
            if x == a: # top of the stack is equal to the next input token
                
                stack.pop() # Pop the top of the stack
                tokens.pop(0) # Pop the next input token
                action_str = f"match {x}"
    
                if debug:
                    print("{:<40}{:<80}{:<40}".format(stack_str, tokens_str, action_str))
            
            else: # Reached an invalid production
                if debug:
                    print("Error")
                return False
        else: # x is a non-terminal

            if debug:
                action_str = f"{x}->{ll1_table[x].get(a, '')}"
                print("{:<40}{:<80}{:<40}".format(stack_str, tokens_str, action_str))

            value = ll1_table.get(x, {}).get(a, "")
            # if ll1_table[x][a] != "":
            if value != "": # If the production is not empty
                
                if ll1_table[x][a] != "ε":
                    stack.pop()
                    for i in range(len(ll1_table[x][a].split(" "))):
                        stack.append(ll1_table[x][a].split(" ")[-i - 1])
                else: # If the production is empty
                    stack.pop()
                    continue
            else: # Reached an invalid production
                if debug:
                    print("Error")
                return False
    return True


if __name__ == "__main__":

    while True:
        expression = input("\nEnter the expression: (type 'exit' to leave')\n")
        if expression == "exit":
            break
        else:

            # Access the tokens from the lexer
            token_list = lexer(expression)
            tokens = [token_list[i][0] for i in range(len(token_list))]

            if debug:
                print(f"Tokens: {tokens}")

            # recursive descent parser
            accept_expr = llparser(tokens)
            if accept_expr:
                if debug:
                    print("Expression valid\n")
                # Evaluate the expression
                result = eval(expression)
                print(f"Result = {result}")
            else:
                print("Entered expression is invalid\n")


