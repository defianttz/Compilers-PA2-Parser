import sys

# Keyword
keywords = ["if", "else", "while", "for", "int", "float", "double", "char", "string", "bool",
            "void", "return", "cout", "cin", "continue", "break", "true", "false"]
# Operators
operators = ["+" ,"++", "-", "*", "/", "%", "=", "<", "<<", ">>", "!", "&", "|"]

comments = ["//", "/*", "*/"]


# Separators
separators = ["(", ")", "{", "}", ";"]

# Punctuators
punctuation = [";"]

class TokenType:
    KEYWORD = 'KEYWORD'
    IDENTIFIER = 'IDENTIFIER'
    OPERATOR = 'OPERATOR'
    INTEGER = 'INTEGER'
    SEPARATOR = 'SEPARATOR'
    COMMENT = 'COMMENT'
    STRING = 'STRING'
    


def scan_num(line):
    num = ""
    for c in line:
        if not c.isdigit():
            break
        num += c
    return TokenType.INTEGER, int(num), len(num)

def scan_str(line):
    delimiter = line[0]
    string = ''
    for c in line[1:]:
        if c == delimiter:
            break
        string += c
    # Add delimiter back to the string
    string = delimiter + string + delimiter
    return TokenType.STRING, string, len(string)

def scan_id(line):
 
    id = ''
    for c in line:
        if not c.isdigit() and not c.isalpha() and c != '_':
            break
        id += c

    if id in keywords:
        return TokenType.KEYWORD, id, len(id)
    else:
        return TokenType.IDENTIFIER, id, len(id)
def scan_operator(line):
    op = ''
    for c in line:
        if c not in operators or c in comments:
            break
        op += c
    return TokenType.OPERATOR, op, len(op)


def scan_comment(line):

    # Check for single line comment
    if line[0] == '/' and line[1] == '/':
        comment = line[0:2]
        for c in line[2:]:
            if c == '\n':
                comment += c
                break
            comment += c
    elif line[0] == '/' and line[1] == '*':
        comment = line[0:2]
        for c in line[2:]:
            if c == '*' and line[line.index(c) + 1] == '/':
                comment += c + '/'
                break
            comment += c

    return TokenType.COMMENT, comment, len(comment)


def lexer(line):
    lexeme_count = 0
    tokens = []
    while lexeme_count < len(line):
        lexeme = line[lexeme_count]

        # Check for integers (state 1)
        if lexeme.isdigit():
            typ, tok, consumed = scan_num(line[lexeme_count:])
            lexeme_count += consumed
            tokens.append((typ, tok))
        #  Check for strings (state 3)
        elif lexeme == '"' or lexeme == "'":
            typ, tok, consumed = scan_str(line[lexeme_count:])
            lexeme_count += consumed + 1  # +1 to skip the closing quote
            tokens.append((typ, tok))
        # Check for identifiers
        elif lexeme.isalpha() or lexeme == '_':
            typ, tok, consumed = scan_id(line[lexeme_count:])
            lexeme_count += consumed
            tokens.append((typ, tok))
        elif lexeme == '/':
            typ, tok, consumed = scan_comment(line[lexeme_count:])
            lexeme_count += consumed
            tokens.append((typ, tok))

        elif lexeme in punctuation:
            tokens.append(('Punctuation', lexeme))
            lexeme_count += 1
        # Check for operators
        elif lexeme in operators:
            typ, tok, consumed = scan_operator(line[lexeme_count:])

            tokens.append(('Operator', tok))
            lexeme_count += consumed
        # Check for separators
        elif lexeme in separators:
            tokens.append(('Seperator', lexeme))
            lexeme_count += 1
        else:
            lexeme_count += 1

    return tokens


if __name__ == "__main__":


    if len(sys.argv) != 2:
        print("Usage: python3 lexical_analyzer.py <source_code_file>")
        sys.exit(1)
    # "input_sourcecode.txt"
    source_code_file = sys.argv[1]
    with open(source_code_file, "r") as fp:
        source_code = fp.read()


    # Scan the source code and print the tokens
    tokens = lexer(source_code)
    print("\ntokens    \tlexemes")
    print("________________________")
    for token in tokens:
        #print(f"token: {token[0]}  lexeme: {token[1]}")
        print(f"{token[0]} \t {token[1]}")
