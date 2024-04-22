import numbers

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
        # Check for number type
        if isinstance(op1, numbers.Number) and isinstance(op2, numbers.Number):
            opPush(op2 == op1)
        else:
            opPush(op2)
            opPush(op1)
            print("Invalid operand type for eq operator.")     
    else:
        print("Invalid size for eq operator: Less than 2 operands.")

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
                opPush(string[index:index + count + 1] + ")")
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

# Can't figure this out for the life of me, sorry
def roll():
    pass

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
    if len(opstack) >= 2 and len(dictstack) > 0:
        value = opPop()
        name = opPop()
        # Use define given that there is a dictionary and a name and value pair.
        define(name, value)
    else:
        # Can maybe separate this
        print("Invalid name and value or no dictionary present.")