import base64
from Ejercicio6 import des_decrypt

def FuerzaBruta(target_b64, wordlist):
    cipher_bytes = base64.b64decode(target_b64)
    #Convierte ese bloque de texto largo en una lista individual de palabras.
    keys = [k.strip() for k in wordlist.strip().split('\n') if k.strip()]
    
    for word in keys:
        #Si la palabra de la lista tiene 5 letras, le añade espacios al final
        adj_key = word.ljust(8)[:8]
        key_int = int.from_bytes(adj_key.encode('ascii'), "big")
        
        try:
            res = des_decrypt(cipher_bytes, key_int)
            text = res.decode('ascii')
            if text.isprintable():
                return word, text
        except:
            continue
    return None

c_text = "h+F7XMoHpF0="
lista = """
root#001
admin@02
exploit$
buffer%1
shell&01
kernel*1
hacker+1
crack=01
patch?01
bug!0001
zero^001
ovfl~001
malw@001
trojan<1
worm>001
virus/01
payld:01
script;1
sql_inj1
inject-1
brute#01
force@01
hash$001
salt%001
cipher&1
crypto*1
key+0001
lock=001
token?01
cookie!1
phish^01
spoof~01
spam|001
botnet<1
ddos>001
flood/01
nmap:001
burp@001
zap-0001
proxy#01
tunnel@1
vpn$0001
tor%0001
onion&01
dark*001
net+0001
deep=001
web?0001
rootkit1
backdr^1
keylog~1
sniff|01
trace<01
forge>01
mask/001
cloak:01
stealth1
breach01
leak-001
dump#001
scan@001
port$001
firew%01
IDS&0001
IPS*0001
SIEM+001
sPyWar3?
alert=01
log?0001
audit!01
secure^1
safe~001
vault|01
shield<1
guard>01
protect1
defense1
code;001
binary01
sudo-001
passwd01
ssh@0001
cert$001
tls%0001
ssl&0001
hash*001
enc+0001
dec=0001
xor?0001
key!0001
auth^001
token~01
user|001
root<001
admin>01
sys/0001
net:0001
hack;001
vuln_001
exploit1
"""

found = FuerzaBruta(c_text, lista)
if found:
    print(f"Llave: {found[0]} -> Mensaje: {found[1]}")