
value1 = '1~1/2~2/3~3';
value2 = '4,5~4,5/6,7~6,7/8,9~8,9';
value3 = '8,8/8,8/8,8';
for i,j,k in zip(value1.split('/'),value2.split('/'),value3.split('/')):
    for l,m,n in zip(i.split('~'),j.split('~'),k.split('~')):
        print(l + m + n)
        print(i + j + k)
