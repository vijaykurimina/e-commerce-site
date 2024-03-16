# a=float(input("enter a value"))
# b=float(input("enter b value"))
# c=int(a)
# d=int(b)
# e=c**d
# print(e)



# a=15
# b=1.5
# c="abcd"
# d="15>13"
# e=15+3j
# print(type(a),type(b),type(c),type(d),type(e))



# marks=int(input("enter a marks"))
# if marks>35:
#     print("cheated")
# elif marks==35:
#     print("pass")
# else:
#     print("fail")   



# number= int(input("enter the number:"))
# if number%3==0 and number%6==0:
#     print("good number")
# elif number%2 and number%7:
#     print("average number")
# elif number%4==0 or number%9==0:  
#     print("awesome number")  
# else:
#     print("bad number")        


# year=int(input("enter the leap year"))
# if year%4==0 and year%100!=0:
#     print(year," is a leap year:")
# elif year%400==0:
#     print(year,"is a leaf year")    
# else:
#     print(year,"is not a leaf year")



# s1=int(input("enter the side1:"))
# s2=int(input("enter the side2:"))
# s3=int(input("enter the side3:"))

# if(s1==s2==s3):
#     print("it is equelateral")
# elif (s1==s2) or (s2==s3) or (s3==s1):
#     print("Isoloesess")
# else:
#     print("scalar")                

# fact=1
# for i in range(1,8):
#      fact=fact*i
#      print(fact)


# a=0
# b=1
# print(a)
# print(b)
# for i in range(3,11):
#     c=a+b
#     a=b
#     b=c
#     print(c)


# n=int(input())
# if n% range(2,n)==0 and n% range()==0:
#     print("prime")


# n=13
# flag=0
# for i in range(2,0):
#     if n%i==0:
#         flag=1
#         break
# if flag==1:
#         print("not")
# else:
#      print("prime")

# n=int(input("enter a number:"))
# flag=0
# for i in range(2,0):
#     if n%i==0:
#         flag=1
#         break
# if flag==1:
#     print("not")
# else:
#     print("prime")        


# n=int(input("enter a number"))
# while n>0:
    

# rows=int(input("enter the no of rows:"))

# for i in range(1,rows+1):
#     for j in range(1,6):
#         print("*",end="  ")
#     print()


# rows=int(input("enter the no of rows:"))

# for i in range(1,rows+1):
#     for j in range(1,6):
#         print("*",end="  ")
#         print()

# rows=int(input("enter the no of rows:"))

# for i in range(1,6):
#     for space in range(rows-i+1):
#            for j in range(1,6):
#             print("*",end="  ")
#     print()


# rows=int(input("enter no of rows:"))
# for i in range(1,5):
#     for j in range(1,5):
#         if (i==1 or i==4 or j==1 or j==4):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()        


# rows=int(input("enter no of rows:"))
# num=1
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print(num,end=" ")
#         num+=1
#     print()    


# rows=int(input("enter no of rows:"))
# num=1
# for i in range(1,rows+1):
#     for space in range(rows-i+1):
#         print(" ",end=" ")
#     for j in range(1,2*i):
#           print("*",end=" ")
#     print()    



# rows=int(input("enter no of rows:"))
# num=1
# for i in range(1,5):
#     for j in range(1,7):
#         if(i==)
#         print(" ",end=" ")
#     for j in range(1,2*i):
#           print("*",end=" ")
#     print()    



# choice=int(input("enter the numbers:"))

# while choice>0:
#     rem=choice%10
#     print(rem)
#     choice=choice//10



# choice=int(input("enter the numbers:"))
# count=0
# while choice>0:
#     choice=choice//10
#     count+=1
# print(count)    




# choice=int(input("enter the numbers:"))
# sum=0
# while choice>0:
#     rem=choice%10
#     sum=sum+rem
#     choice=choice//10
# print(sum)    



# choice=int(input("enter the numbers:"))
# mul=1
# while choice>0:
#     rem=choice%10
#     mul=mul*rem
#     choice=choice//10
# print(mul)    
  


# n=int(input("enter the numbers":))
# s=0
# while n>0:
#     digit=n%10
#     s=s+digit//10
# print(s)    



# choice=int(input("enter the numbers:"))
# sum=0
# while choice>0:
#     rem=choice%10
#     sum=sum+rem
#     choice=choice//10
# if choice/sum==0:
#     print("it is divisible by",sum)
# else:
#     print("it is not divisible by",sum)       



# choice=int(input("enter the numbers:"))
# sum=0
# temp=choice
# for i in range(1,choice//2+1):
#     if choice%i==0:
#         sum=sum+i
#         if temp>sum:
#             print("no")
#         else:
#             print("yes")    


# run=int(input("enter the numbers:"))
# sum1=0
# sum2=0
# for i in range(1,31):
#     if i%6==0:
#         sum1=sum1+i
#     else:
#         sum2=sum2+i
# print(sum1)
# print(sum2)
# print("Difference:",sum2-sum1)            




# choice=int(input("enter the number:"))
# temp=choice
# num=0
# while choice>0:
#     rem=choice%10
#     num=num*10+rem
#     choice=choice//10
# print(num)
# if temp==num:
#     print("Yes")
# else:
#     print("No")    

# armstrong

# choice=int(input("enter the number:"))
# temp=choice
# count=len(str(choice))
# arm=0
# while choice>0:
#     rem=choice%10
#     arm=arm+rem**count
#     choice=choice//10
# print(arm)
# print(count)
# if temp==arm:
#     print("Yes")
# else:
#     print("No")



# choice=int(input("enter the number:"))
# ar=0
# c=0
# while temp1>0:
#     c=c+1
#     temp1=temp1//10
# print(c)
# while choice>0:
#     rem=choice%10
#     ar=ar+rem**c
#     c=c-1
#     choice=choice//10
# print(ar)




# functions

def typecast(a,b):
    a=int(a)

    p=a*b
    rem=p%10
    print(rem)
typecast(11,12)