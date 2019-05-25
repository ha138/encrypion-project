from base64 import b64encode, b64decode


def encrypt(text, key):
    output = ''
    out = 0
    key = str(key)
    for item in key:
        out = out + ord(item)
    key = int(out)
    text = b64encode(text.encode()).decode()
    for item in text:
        output = output + str(ord(item) + key) + '.'
    return output


def decrypt(text, key):
    try:
        output = ''
        out = 0
        key = str(key)
        for item in key:
            out = out + ord(item)
        key = int(out)
        text = str(text).split('.')
        for item in text:
            if item == '':
                break
            output = output + chr(int(int(item) - key))
        output = b64decode(output.encode()).decode()
        return output
    except Exception as e:
        print(repr(e))
        return ''


a = encrypt('hello world', '1234')
print('Encrypted text: ' + a)
a = decrypt(a, '1234')
print('Decrypted text: ' + str(a))
