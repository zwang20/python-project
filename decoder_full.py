
print('Decoder Full by Michael')
print('Includes 320, 330, 350, 360, 370, 380, and 390')

def decode_320(string, password):
    password = int(password)
    outputs = []
    temp = []
    inputs = string.split('-')
    while password < 0:
        password += 100
    while password > 99:
        password -= 100
    for c in inputs:
        c = int(c) - password
        if c < 0:
            c += 100
        c = str(c)
        if len(c) > 2:
            c = str(int(c) - 100)
        if len(c) < 2:
            c = '0' + c
        temp.append(c)
    for c in temp:
        if int(c) in range(1, 26):
            outputs.append(chr(int(c)+96))
        else:
            outputs.append(' ')
    return ''.join(outputs)


def decode_330(string, password):
    password = int(password)
    return decode_320(string, password)

def decode_350(string, password):
    password = int(password)
    outputs = []
    temp = []
    while password < 0:
        password += 100000
    while password > 99999:
        password -= 100000
    for c in inputs:
        c = int(c) - password
        if c < 0:
            c += 100000
        c = str(c)
        if len(c) > 5:
            c = int(c) - 100000
        c = str(c)
        while len(c) < 5:
            c = '0' + c
        c = str(c)
        temp.append(c)
    for c in temp:
        if c in range(0, 65534) and c not in range(55295, 57999):
            outputs.append(chr(int(c)))
    return ''.join(outputs)

def decode_350(string, password):
    return 'todo'

