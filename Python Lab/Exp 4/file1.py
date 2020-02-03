def calculator(action):
    if action[1] == '+':
        return int(action[0]) + int(action[2])
    elif action[1] == '-':
        return int(action[0]) - int(action[2])
    elif action[1] == '*':
        return int(action[0]) * int(action[2])
    elif action[1] == '/':
        return int(action[0]) / int(action[2])