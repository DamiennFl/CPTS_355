opstack = [1, 2, 3, 4, 5]

def roll(ttR, num_roll):
    global opstack  # Use the global opstack variable
    roll_stack = opstack[-num_roll:]  # Get top amount to roll. If input is 3, top 3 values will be in this.
    if ttR > 0:
        while ttR > 0:
            roll_stack = roll_stack[-1:] + roll_stack[:-1]
            ttR -= 1
    else:
        while ttR < 0:
            roll_stack = roll_stack[1:] + roll_stack[:1]
            ttR += 1
    opstack[-num_roll:] = roll_stack  # Assign the rolled stack back to the relevant portion of opstack

roll(-2, 4)
print(opstack)
