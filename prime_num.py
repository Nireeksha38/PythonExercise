num=int(input("enter the numebr to check prime or not)
if num<2:
  print("not prime")
else:
  for i in range(2,num):
        if num%i==0:
          print("not a prime")
          break
  else:
        print("Prime")
