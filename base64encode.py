final=''
plain=input('Input your text? ')
plain=plain+'\n'
new_b=''
b64_table={'0': 'A', '1': 'B', '2': 'C', '3': 'D', '4': 'E', '5': 'F', '6': 'G', '7': 'H', '8': 'I', '9': 'J', '10': 'K', '11': 'L', '12': 'M', '13': 'N', '14': 'O', '15': 'P', '16': 'Q', '17': 'R', '18': 'S', '19': 'T', '20': 'U', '21': 'V', '22': 'W', '23': 'X', '24': 'Y', '25': 'Z','26': 'a', '27': 'b', '28': 'c', '29': 'd', '30': 'e', '31': 'f', '32': 'g', '33': 'h', '34': 'i', '35': 'j', '36': 'k', '37': 'l', '38': 'm', '39': 'n', '40': 'o', '41': 'p', '42': 'q', '43': 'r', '44': 's', '45': 't', '46': 'u', '47': 'v', '48': 'w', '49': 'x', '50': 'y', '51': 'z','52': '0', '53': '1', '54': '2', '55': '3', '56': '4', '57': '5', '58': '6', '59': '7', '60': '8', '61': '9','62':'÷','63':'/'}
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
for items in plain:
    x=ord(items)
    y=d_b(x)
    if len(y)%8==0:
        new_b=new_b+y
    else:
        while len(y)%8!=0:
            y='0'+y
        new_b=new_b+y
if len(new_b)%6!=0:
    t=0
    while len(new_b)%6!=0:
        new_b=new_b+'0'
        t=t+1
    for i in range(0,(len(str(new_b))),6):
        part=str(new_b)[i:i+6]
        dec=str(b_d(int(part))) 
        char=b64_table.get(dec)
        final=final+char
    if len(final)%4==0:
        print(final)
    else:
        while len(final)%4!=0:
            final=final+'='
        print(final)
else:
    for i in range(0,(len(str(new_b))),6):
        part=str(new_b)[i:i+6]
        dec=str(b_d(int(part)))
        char=b64_table.get(dec)
        final=final+char
    if len(final)%4==0:
        print(final)
    else:
        while len(final)%4!=0:
            final=final+'='
        print(final)
