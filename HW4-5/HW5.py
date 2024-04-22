import numbers
import re

# Damien Flutre
# 3/29/2024

#------------------------- 10% -------------------------------------
# Operand Stack List
opstack = []  

# opPop Function
# Pops the top operand from the operand stack and returns it.
def opPop():
    if len(opstack) > 0:
        return opstack.pop()
    else:
        print("Empty operand stack.")
        return None

# opPush Function
# Pushed a value to the operand stack. Does not have to be a number.
def opPush(value):
    opstack.append(value)

#-------------------------- 20% -------------------------------------
# The dictionary stack: define the dictionary stack and its operations
dictstack = []  #assuming top of the stack is the end of the list

# dictPop Function
# Pops the top dictionary from the top of the stack and returns it.
def dictPop():
    if len(dictstack) > 0:
        return dictstack.pop()
    else:
        print("Empty dictionary stack.")
        return None

# dictPush Function
# Pushes a paramerized value to the dictionary stack.
def dictPush(d):
    dictstack.append(d)

# define Function
# Define a name and a value associated with that value., and adds it to the top dictionary.
def define(name, value):
    # If there is no dictionary at all, add an empty one. Makes sure that define always has a dictionary to add to.
    if len(dictstack) == 0:
        dictPush({})
    
    if len(dictstack) > 0:
        first_dict = dictstack[-1]
        first_dict[name] = value
    else:
        print("Empty dictionary stack. Name and value pair cannot be added.")

# lookup Function
# Finds the value within the stack of dictionaries. Starts from the top dictionary and moves down.
def lookup(name):
    # Reversed to start at the top (end of list).
    for dict in reversed(dictstack):
        if name in dict:
            return dict[name]
    
    # Prints that the name was not found if nothing is ever returned.
    print(f"NameNotFoundError: Name '{name}' is not defined in any dictionary.")
    return None

#--------------------------- 10% -------------------------------------
# Arithmetic and comparison operators: add, sub, mul, div, mod, eq, lt, gt
# Make sure to check the operand stack has the correct number of parameters
# and types of the parameters are correct.

# add Function
# Adds the top two operands in the operator stack provided they are both a number type.
def add():
    if len(opstack) >= 2:
        op1 = opPop()
        op2 = opPop()
        # Check if they are both number types
        if isinstance(op1, numbers.Number) and isinstance(op2, numbers.Number):
            opPush(op1 + op2)
        else:
            # Can make this else statement more detailed by also printing the type(s) of op1 and op2 (for Part 2).
            # Have to push them back to make sure the stack stays the same after error.
            
            # Another implementation would be to check the type BEFORE popping them from the stack,
            # I just didn't do it that way. Might switch it to that for Part 2 if it ends up being easier.
            opPush(op2)
            opPush(op1)
            print("Invalid operand type for add operator.")
    else:
        print("Invalid size for add operator: Less than 2 operands.")

# sub Function
# Subtracts the first operand from the second operand on the stack provided they are both a number type.
def sub():
    if len(opstack) >= 2:
        op1 = opPop()
        op2 = opPop()
        # Check for number type
        if isinstance(op1, numbers.Number) and isinstance(op2, numbers.Number):
            opPush(op2 - op1)
        else:
            opPush(op2)
            opPush(op1)
            print("Invalid operand type for sub operator.")
    else:
        print("Invalid size for sub operator: Less than 2 operands.")

# mul Function
# mul multiplies the first and second operand on the operator stack provided they are both a number type.
def mul():
    if len(opstack) >= 2:
        op1 = opPop()
        op2 = opPop()
        # Check for number type
        if isinstance(op1, numbers.Number) and isinstance(op2, numbers.Number):
            opPush(op2 * op1)
        else:
            opPush(op2)
            opPush(op1)
            print("Invalid operand type for mul operator.")
    else:
        print("Invalid size for mul operator: Less than 2 operands.")

# div Function
# div divides the second operand on the stack by the first operand provided they are both a number type.
def div():
    if len(opstack) >= 2:
        op1 = opPop()
        op2 = opPop()
        # Check for number type
        if isinstance(op1, numbers.Number) and isinstance(op2, int):
            opPush(op2 / op1)
        else:
            opPush(op2)
            opPush(op1)
            print("Invalid operand type for div operator.")            
    else:
        print("Invalid size for div operator: Less than 2 operands.")

# mod Function
# mod applies the modulo function provided both operands are a number type.
def mod():
    if len(opstack) >= 2:
        op1 = opPop()
        op2 = opPop()
        # Check for number type
        if isinstance(op1, numbers.Number) and isinstance(op2, numbers.Number):
            opPush(op2 % op1)
        else:
            opPush(op2)
            opPush(op1)
            print("Invalid operand type for mod operator.")     
    else:
        print("Invalid size for mod operator: Less than 2 operands.")

# eq Function
# eq compares the first and second operand on the stack. Pushes true if equal, false otherwise onto the stack.
def eq():
    if len(opstack) >= 2:
        op1 = opPop()
        op2 = opPop()
        if op1 == op2:
            opPush(True)
        else:
            opPush(False)
    else:
        print("Invalid size for eq operator: Less than 2 operand    s.")

# lt Function
# lt compares the first and second operand on the stack. True if op2 < op1, false otherwise.
def lt():
    if len(opstack) >= 2:
        op1 = opPop()
        op2 = opPop()
        # Check for number type
        if isinstance(op1, numbers.Number) and isinstance(op2, numbers.Number):
            opPush(op2 < op1)
        else:
            opPush(op2)
            opPush(op1)
            print("Invalid operand type for lt operator.")     
    else:
        print("Invalid size for eq operator: Less than 2 operands.")

# gt Function
# gt compares the first and second operand on the stack. True if op2 > op1, false otherwise.
def gt():
    if len(opstack) >= 2:
        op1 = opPop()
        op2 = opPop()
        # Check for number type
        if isinstance(op1, numbers.Number) and isinstance(op2, numbers.Number):
            opPush(op2 > op1)
        else:
            opPush(op2)
            opPush(op1)
            print("Invalid operand type for gt operator.")
    else:
        print("Invalid size for eq operator: Less than 2 operands.")

#--------------------------- 15% -------------------------------------
# String operators: define the string operators length, get, getinterval, put

# length Function
# length returns the length of a string on the operand stack.
def length():
    if len(opstack) >= 1:
        op1 = opPop()
        # Check if op1 is a string
        if isinstance(op1, str):
            # Strip the parantheses from Post-Script strings.
            opPush(len(op1[1:-1]))
        else:
            opPush(op1)
            print("Invalid operand type for length operator.")
    else:
        print("Empty operand stack. Length operator cannot be done.")

# get Function
# get returns the character at a given index.
def get():
    if len(opstack) >= 2:
        index = opPop()
        string = opPop()
        # Check if operand is a string
        if isinstance(string, str) and isinstance(index, int):
            if 0 <= index < len(string):
            # + 1 for parantheses delimiter
                opPush(ord(string[index + 1]))
            else:
                opPush(string)
                opPush(index)
                print(f"Index '{index}' is out of range.")
        else:
            opPush(string)
            opPush(index)
            print("Invalid type for get operator.")
    else:
        print("Not enough operands. Get operator cannot be done.")

# getInterval Function
# getInterval returns a portion of a string given by a start index and a count of characters.
def getinterval():
    if len(opstack) >= 3:
        count = opPop()
        index = opPop()
        string = opPop()
        # Check that string is in fact a string
        if isinstance(string, str) and isinstance(index, int) and isinstance(count, int):
            if 0 <= index < len(string) - 1 and 0 <= (count + index) <= len(string) - 1:
            # + 1 for parantheses delimiter
                if index == 0:
                    opPush(string[index:index +count + 1] + ")")
                else:
                    new_string = '(' + string[index + 1:index + count + 1] + ')'
                    opPush(new_string)
            else:
                opPush(string)
                opPush(index)
                opPush(count)
                print("Index is out of range.")
        else:
            opPush(string)
            opPush(index)
            opPush(count)
            print("Invalid type for getInterval operator.")
    else:
        print("Not enough operands. getInterval operator cannot be done.")

# put Function
# put replaces a character at a given index with a new character.
def put():
    if len(opstack) >= 3:
        # Turn ASCII value back into character
        new_char = chr(opPop()) 
        index = opPop()     
        string = opPop()    
        # Check that each item is the correct type
        if isinstance(string, str) and isinstance(index, int) and isinstance(new_char, str):
            # -2 for parantheses delimiter on either side
            if 0 <= index < len(string) - 2:
                # From beginning to index + 1, then add the new character, then the rest of the string.
                new_string = string[:index + 1] + new_char + string[index + 2:]
                
                for i in range(len(opstack)):
                    if id(opstack[i]) == id(string):
                        opstack[i] = new_string
                
                for dictionary in reversed(dictstack):
                    for key in dictionary:
                        if id(dictionary[key]) == id(new_string):
                            dictionary[key] = new_string
                
                opPush(new_string)
            else:
                opPush(string)
                opPush(index)
                opPush(ord(new_char))
                print("Error: Index is out of range.")
        else:
            opPush(string)
            opPush(index)
            opPush(ord(new_char))
            print("Error: Invalid operand types for put operator.")
    else:
        print("Error: Not enough operands on the operand stack.")
        
#--------------------------- 25% -------------------------------------
# Define the stack manipulation and print operators: dup, copy, pop, clear, exch, roll, stack

# dup Function
# dup duplicates the item at the top of the operand stack and adds it to the top of the stack.
def dup():
    if len(opstack) >= 1:
        opPush(opstack[-1])
    else:
        print("Empty Operand Stack. Cannot duplicate.")

# copy Function
# copy copies the top n values and adds them to the top of the stack.
def copy():
    if len(opstack) == 0:
        print("Empty list.")
    
    if len(opstack) >= 2:
        n = opPop()
        # Check for number type
        if isinstance(n, int):
            # Use extend function to take the n values (starting from the end, hence the -n) and extend the list.
            opstack.extend(opstack[-n:])
        else:
            print("Invalid type for copy operator.")
    else:
        print("No elements to copy.")
        
# pop Function
# pop pops the top value without returning anything.
def pop():
    # Pop the value without returning anything.
    opPop()

# clear Function
# clear removes everything from the operand stack.
def clear():
    opstack.clear()

# exch Function
# exch switches the top two operands on the operand stack.
def exch():
    if len(opstack) >= 2:
        opstack[-1], opstack[-2] = opstack[-2], opstack[-1]
    else:
        print("Not enough elements to exchange.")

# roll Function
# roll rolls the n top elements i times. Positive means rolled upward/forward, negative means downwards/backwards.
def roll():
    ttR = opPop() # Times to roll (I'm lazy)
    num_roll = opPop()
    global opstack
    roll_stack = opstack[-num_roll:] # Get top amount to roll. If input is 3, top 3 values will be in this.
    if ttR > 0:
        while ttR > 0:
            roll_stack = roll_stack[-1:] + roll_stack[:-1]
            ttR -= 1
    else:
        while ttR < 0:
            roll_stack = roll_stack[1:] + roll_stack[:1]
            ttR += 1
    opstack[-num_roll:] = roll_stack  # Replace part of stack which needed to be rolled with rolled part.    

# stack Function
# Prints the entire stack, starting from the top.
def stack():
    # Slice in reverse order, starting from the end of the sequence and stepping back one each time.
    for operand in opstack[::-1]:
        print(operand)
#--------------------------- 20% -------------------------------------
# Define the dictionary manipulation operators: psDict, begin, end, psDef
# name the function for the def operator psDef because def is reserved in Python. Similarly, call the function for dict operator as psDict.
# Note: The psDef operator will pop the value and name from the opstack and call your own "define" operator (pass those values as parameters).
# Note that psDef()won't have any parameters.

# psDict Function
# psDict adds a new dictionary of size n to the operand stack (not dictionary stack).
def psDict():
    if len(opstack) >= 1:
        # Not sure what size is supposed to do since dictionaries are dynamic.
        size = opPop()
        new_dict = {}
        opPush(new_dict)
    else:
        print("No defined size for dict operand.")

# begin Function
# begin takes a dictionary from the top of the operand stack and adds it to the dictionary stack.
def begin():
    if len(opstack) >= 1:
        dictionary = opPop()
        if isinstance(dictionary, dict):
            dictPush(dictionary)
        else:
            print("Incorrect type for begin operator.")
    else:
        print("Empty stack for begin operator.")

# end Function
# end simply removes the top dictionary from the dictionary stack and does not return anything.
def end():
    dictPop()

# psDef Function
# psDef is an alternate version of define which defines a name and value pair in the top dictionary.
def psDef():
    if len(dictstack) == 0:
        dictPush({})
    if len(opstack) >= 2 and len(dictstack) > 0:
        value = opPop()
        name = opPop()
        dictstack[-1][name] = value
    else:
        print(f"Error: Invalid name and value or no dictionary present.")


#--------------------------Part 2--------------------------

# psIf is the implementation of the "if" function in Postscript.
# If the boolean is true, execute the code. Otherwise, do nothing.
def psIf() :
    code_array = opPop()
    poppedBool = opPop()
    if isinstance(poppedBool, bool) and poppedBool == True: # If true
        interpretSPS(code_array) # Run Code
        

# psIfElse is the implementation of the "ifelse" function in Postscript.
# If the boolean is true, execute code_array1, otherwise, code_array2.
def psIfElse():
    code_array2 = opPop()
    code_array1 = opPop()
    poppedBool = opPop()
    if isinstance(poppedBool, bool) and poppedBool == True: # If true,
        interpretSPS(code_array1) # run code_array1
    else:
        interpretSPS(code_array2) # otherwise, run code_array2.

# psFor is the implementation of the "for" function in Postscript.
# for takes code to execute, a final value, incremnet, and an initial value.
# It iterates from the starting to ending value, incrementing by increment until final value.
# The code is executed with each iteration.
def psFor():
    if len(opstack) >= 4:
        code_array = opPop() # Get variables
        final_val = opPop()
        increment = opPop()
        initial_val = opPop()
        if isinstance(final_val, int) and isinstance(increment, int) and isinstance(initial_val, int):
            if increment < 0: # If increment is negative, initial_val will go down to final_val
                while initial_val >= final_val:
                    opPush(initial_val)
                    interpretSPS(code_array)
                    initial_val += increment

            if increment > 0: # If increment is positive, initial_val will climb to final_val
                while initial_val <= final_val:
                    opPush(initial_val)
                    interpretSPS(code_array)
                    initial_val += increment
        else:
            print("Invalid types for \"for\" function operands.")
    else:
        print("Invalid amount of operands for \"for\" function.")
            
# tokenize function for creating list of items.
def tokenize(s):
    return re.findall("/?[a-zA-Z()][a-zA-Z0-9_()]*|[-]?[0-9]+|[}{]+|%.*", s)

# Dictionary of functions and their Postscript names to search through
ops = {
    "add" : add, "sub" : sub, "mul" : mul, "opPop" : opPop, "dictPop" : dictPop, "div" : div,
    "mod" : mod, "eq" : eq, "lt" : lt, "gt" : gt, "length" : length, "get" : get, "getinterval" : getinterval,
    "put" : put, "dup" : dup, "copy" : copy, "pop" : pop, "clear" : clear, "exch" : exch, "roll" : roll,
    "stack" : stack, "def" : psDef, "dict" : psDict, "begin" : begin, "end" : end, "if" : psIf, "ifelse" : psIfElse,
    "for" : psFor 
}


# The it argument is an iterator.
# The sequence of return characters should represent a list of properly nested
# tokens, where the tokens between '{' and '}' are included as a sublist. If the
# parentheses in the input iterator are not properly nested, it returns False.
# UNCHANGED
def groupMatching2(it):
    res = []
    for c in it:
        if c == '}':
            return res
        elif c == '{':
            res.append(groupMatching2(it))
        else:
            res.append(c)
    return False

# isInt Function
# Helper function to identify n as an int.
def isInt(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

# isString Function
# Helper function to identify n as a string.
def isString(n):
    try:
        str(n)
        return True
    except ValueError:
        return False

# parse Function
# Parse checks each item (sometimes recursively!) within the tokenized list of items.
# Each item is added according to the correct type. If it is a list, then parse is called
# recursively to convert items within the list to their correct types, before being added to res (the result list).
def parse(L):
    res = []
    it = iter(L)
    for c in it:
        if c == '}':
            return False
        elif c == '{':
            res.append(parse(groupMatching2(it))) # Parse the groupMatching result, which will be a sublist
        else:
            if isinstance(c, list): # Check if c is a sublist
                res.append(parse(c)) # parse the sublist. This makes sure we hit every item in the entire list
            elif isInt(c): # Check if current value is an integer
                res.append(int(c)) # Convert integers to integers.
            elif c == 'True': # Check for bool BEFORE string, so bools are not added as strings first.
                res.append(True)
            elif c == 'False':
                res.append(False)
            elif isString(c): # Check string last, aka everything without a specific type
                res.append(str(c))
            else: # Else, append. Catch-all, probably isn't used most of the time. Anything hitting this will likely create errors.
                res.append(c)
    return res

# interpretSPS Function
# This function runs the bulk of the code. It checks each value within the list and manipulates the stack
# by calling different operations, adding to the stack, checking types, and strings.
def interpretSPS(code): # code is a code-array
    # Set of operator names
    operator_names = set(ops.keys())
    
    for token in code:
        if isinstance(token, str) and token[0] == '/': # Check for variable declaration
            opPush(token[1:])  # Remove the '/' character
        elif isinstance(token, str) and token[0] == '(': # Check for non-variable declaration string.
            opPush(token)
        elif isinstance(token, str) and token in operator_names: # Check for operation/function
            ops[token]()  # Execute the operator directly
        elif isinstance(token, str): # Check for token in dictionaries
            lookupVal = lookup(token)
            if lookupVal:
                if isinstance(lookupVal, list): # If a list is found with token, recursively do the list.
                    interpretSPS(lookupVal)
                else:
                    opPush(lookupVal) # Else, push the data associated with token.
        elif isinstance(token, list): # If a list is found in general, without being a lookup, add it to stack.
            opPush(token)
        elif isinstance(token, (int, bool)): # If an int or bool, add it to stack.
            opPush(token)
        else:
            print(f"Invalid token type: {type(token)}") # If it is not any of these, then it can't be a Postscript operation.
        
            
# Copy this to your HW5.py file>
def interpreter(s): # s is a string
    interpreterClear()
    return interpretSPS(parse(tokenize(s)))

# interpreterClear Function
# Helper function which clears opstack and dictstack.
def interpreterClear():
    opstack[:] = []
    dictstack[:] = []
    return