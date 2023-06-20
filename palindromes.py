f = input('--->')
def palindrome(f):
    if f == f[::-1]:
        return f == f[::-1]
if palindrome(f):
    print('True')
else:
    print('False')