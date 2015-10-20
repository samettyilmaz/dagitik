import sys
import os
n = int(sys.argv[2])
s = int(sys.argv[1]) 
l = int(sys.argv[3])
os.getcwd()

def encrypt(argv):
    if (len(sys.argv) != 4):
        sys.exit('Usage: sub.py <s> <n> <l> ')
    


    input_txt=open("metin.txt")
    
    plaintext = list((input_txt.read()).lower())[:l]
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    


    cipher = ''
        
    for c in plaintext:
        if c in alphabet:
            cipher += alphabet[(alphabet.index(c)-s)%(len(alphabet))].upper()
        else :
            cipher +=c

    return cipher
    
output_text=open("crypted_%s_%s_%s.txt" %(s,n,l),"w")
return_value=encrypt(sys.argv[1:])
output_text.write(return_value)



