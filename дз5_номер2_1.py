
n = int(input("Введите число :" ))
nums = (x for x in range(n+1) if x%2 !=0)
i=0
while i!=n:                                
    print('next(n): ',next(nums))
    i+=1