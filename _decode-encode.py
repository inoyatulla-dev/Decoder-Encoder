def findPosition(data, i):
    return data.index(i)


def add(text, k, a=0, p=1):
    data = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']
    result = ''
    n = 26
    a_text = ''

    if a == 1:
        a_text = 'Decoded text'
        k = k - (k + k)
    else:
        a_text = 'Encoded text'
        k = k
    for e in text:
        if e == ' ':
            result = result + ' '
        else:
            position = findPosition(data, e)
            index = (position - k) % n
            if index < 0:
                result = result + data[n + index]
            else:
                result = result + data[index]

    print(a_text + ':"' + result + '"')


# enCode('ENTER', 5, 1, 0)
# JSYJW
while True:
    a = int(input('Enter action (Encode: 0, Decode: 1): '))
    text = input('Enter text: ')
    k = int(input('Enter key: '))
    add(text.upper(), k, a)
    print('Do you want to continue? (yes/no)')
    if input() == 'no':
        break
    else:
        continue
