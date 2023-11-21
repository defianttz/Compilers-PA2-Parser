# Desc: Recursive descent parser for the language
import sys

from Lexer.lexical_analyzer import lexer

# Table for the recursive descent parser
ll1_table = {
    # NT: int, (, ), +, -, *, /, $
    "E": {"int": "T E'", "(": "T E'"},
    "E'": {"+": "+ T E'", "-": "- T E'", ")": "ε", "$": "ε"},
    "T": {"int": "F T'", "(": "F T'"},
    "T'": {"+": "ε", "-": "ε", "*": "* F T'", "/": "/ F T'", ")": "ε", "$": "ε"},
    "F": {"int": "int", "(": "( E )"}

}

# non_terminals = ["E", "E_p" ,"T", "T_p" "F",]
non_terminals = ["E", "E'", "T", "T'" "F", ]


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

    print("{:<40}{:<80}{:<100}".format("Stack", "Input", "Action"))
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

        x = stack[-1]
        a = tokens[0]
        # print(f"x: {x}, a: {a}")
        # print(f"stack: {stack}  tokens: {tokens}\n")
        # print without the brackets
        stack_str = ""
        for i in range(len(stack)):
            stack_str += stack[i]
        tokens_str = ""
        for i in range(len(tokens)):
            tokens_str += tokens[i]

        # prod_str = f"{x}->{ll1_table[x][a]}"

        if x in terminals:
            if x == a:
                stack.pop()
                tokens.pop(0)
                action_str = f"match {x}"

                print("{:<40}{:<80}{:<100}".format(stack_str, tokens_str, action_str))
            else:
                print("Error")
                return False
        else:

            action_str = f"{x}->{ll1_table[x].get(a, '')}"

            print("{:<40}{:<80}{:<100}".format(stack_str, tokens_str, action_str))

            value = ll1_table.get(x, {}).get(a, "")
            # if ll1_table[x][a] != "":
            if value != "":

                if ll1_table[x][a] != "ε":
                    stack.pop()
                    for i in range(len(ll1_table[x][a].split(" "))):
                        stack.append(ll1_table[x][a].split(" ")[-i - 1])
                else:
                    stack.pop()

                    continue
            else:
                print("Error")
                return False
    return True


if __name__ == "__main__":

    while True:
        expression = input("Enter the expression: (type 'exit' to leave')\n")
        if expression == "exit":
            break
        else:

            # Access the tokens from the lexer
            token_list = lexer(expression)

            # Place int*(int + int)/int into tokens
            # tokens = []
            # tokens.append("int")
            # tokens.append("*")
            # tokens.append("(")
            # tokens.append("int")
            # tokens.append("+")
            # tokens.append("int")
            # tokens.append(")")
            # tokens.append("/")
            # tokens.append("int")
            # TODO: Implement the recursive descent parser

            tokens = [token_list[i][0] for i in range(len(token_list))]
            print(f"Tokens: {tokens}")
            accept_expr = llparser(tokens)
            if accept_expr:
                print("Expression valid")
                print("Result = 0")
            else:
                print("Entered expression is invalid")
            # TODO: Implement Calculator

