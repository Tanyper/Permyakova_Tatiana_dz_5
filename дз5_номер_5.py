src_1=list(set(src))
print(src)
print(src_1)

src_2=[]
for x in src_1:
 if x not in src_2:
 src_2.append(x)
print(src_2)
#я не понимаю, почему не работает
