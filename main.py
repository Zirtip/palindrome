inputtext = input('input - ')

def palindrome(text: str):
    halflength = len(text)//2
    chars = list(text)
    x = 0
    for i in range(halflength):
        if chars[0+i] == chars[-1-i]:
            x += 1
    if x == halflength:
        print('True')
    else:
        print('False')

palindrome(inputtext)