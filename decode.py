b64_rtable={'A': '0', 'B': '1', 'C': '2', 'D': '3', 'E': '4', 'F': '5', 'G': '6', 'H': '7', 'I': '8', 'J': '9', 'K': '10', 'L': '11', 'M': '12', 'N': '13', 'O': '14', 'P': '15', 'Q': '16', 'R': '17', 'S': '18', 'T': '19', 'U': '20', 'V': '21', 'W': '22', 'X': '23', 'Y': '24', 'Z': '25', 'a': '26', 'b': '27', 'c': '28', 'd': '29', 'e': '30', 'f': '31', 'g': '32', 'h': '33', 'i': '34', 'j': '35', 'k': '36', 'l': '37', 'm': '38', 'n': '39', 'o': '40', 'p': '41', 'q': '42', 'r': '43', 's': '44', 't': '45', 'u': '46', 'v': '47', 'w': '48', 'x': '49', 'y': '50', 'z': '51', '0': '52', '1': '53', '2': '54', '3': '55', '4': '56', '5': '57', '6': '58', '7': '59', '8': '60', '9': '61', '÷': '62', '/': '63'}
new_val=''
def d_b(num):
    bin=''
    if num ==0:
        return '0'
    else:
        while num >=1:
            r=num%2
            num=num//2
            bin=str(r)+bin
    return str(bin)
def b_d(num):
    dec=0
    for i in range (0,len(str(num))):
        val=int(str(num)[i])
        power=len(str(num))-(i+1)
        dec=dec+val*2**power
    return dec
encoded=input('The encoded Base64 string? ')
for items in encoded:
    if items !='=':
        new_val=new_val+items
    else:
        continue
c_b=''
for items in (new_val):
    try:
        x=int(b64_rtable.get(items))
    except TypeError:
        print("Invaild Base64 value")
        exit()
    x=d_b(x)
    #print(x)
    if len(x)%6!=0:
        while len(x)%6!=0:
            x='0'+x
    #print(x)
    c_b=c_b+x
while len(c_b) % 8!=0:
    c_b=c_b[0:len(c_b)-1]
final=''
for i in range(0,(len(str(c_b))),8):
    part=str(c_b)[i:i+8]
    dec=str(b_d(int(part))) 
    char=chr(int(dec))
    final=final+char
print(final)