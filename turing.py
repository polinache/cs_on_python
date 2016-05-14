def newTM(filename):
    input = open(filename, 'r')
    string = input.readline()
    string.rstrip()
    state_instruction = {}
    while string:
        state = list(map(str, string.split()))
        if state[0] in state_instruction.keys():
            state_instruction[state[0]].update({state[1]:(state[2], state[3], state[4])})
        else:
            state_instruction.update({state[0]:{state[1]:(state[2], state[3], state[4])}})
        string = input.readline()
        string.rstrip()
    input.close()
    return state_instruction

def action(state, symbol, desc):
    (newstate, newsymbol, act) = desc[state][symbol]
    return newstate, newsymbol, act



input = open('input_t.txt', 'r')
line = list(input.readline())
state = 'q_1'
instructions = newTM('desc.txt')
i = 0
while state != 'Q':
    (a,b,c) = action(state, line[i], instructions)
    line[i] = b
    state = a
    if c == 'R':
        i += 1
    elif c == 'L':
        i -= 1
print(line)










