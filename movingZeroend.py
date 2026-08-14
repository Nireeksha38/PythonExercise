arr=[12,34,5,0,98,0,67,0,4,0]
result=[]
for i in arr:
  if i!=0:
    result.append(i)
for i in arr:
  if i==0:
    result.append(i)
