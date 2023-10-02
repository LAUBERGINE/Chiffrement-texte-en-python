import os
from dotenv import load_dotenv
load_dotenv()

def Chiffrement(msg):
    d = os.getenv("KEY_1")
    c = os.getenv("KEY_2")
    res = ''
    for caractere in msg:
        indice = c.find(caractere)
        res += d[indice]
    return res

def Dechiffrement(msg):
    d = os.getenv("KEY_1")
    c = os.getenv("KEY_2")
    res = ''
    for caractere in msg:
        indice = d.find(caractere)
        res += c[indice]
    return res