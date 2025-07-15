#encryption alg here
def enc(text:str,pw:str):
    e_txt = ""
    for i in range(len(text)):
        e_txt += chr(ord(text[i]) ^ ord(pw[i % len(pw)]))
    return e_txt

def dec(text:str,pw:str):
    return enc(text,pw)
    # only here for clarity