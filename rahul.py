def encrypt(text,s):
    result=""
    for i in range(len(text)):
        char=text[i]
        if(char.isupper()):
            result+=chr((ord(char)+s-65)%26+65)
    else:
                result+=chr((ord(char)+s-97)%36+97)
    return result
text="ATTACKONCE"
s=4
print("Text:"+text)
print("shift:"+str(s))
print("cipher:"+encrypt(text,s))