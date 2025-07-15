#encryption alg here
def enc(text,pw):
    e_txt = ""
    for i in range(len(text)):
        e_txt += chr(ord(text[i]) ^ ord(pw[i % len(pw)]))
    return e_txt

def dec(text,pw):
    return enc(text,pw)