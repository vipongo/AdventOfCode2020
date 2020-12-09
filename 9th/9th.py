e=[int(d) for d in open('input.txt').read().split('\n') if d!='']
def a(e):
 for i in range(25,len(e)):
  p=e[i-25:i]
  def c():
   for j,k in [(j,k) for j in p for k in p]:
    if j!=k and j+k==e[i]:return 1
   return 0
  if not c():return e[i]
def b(e):
 def d():
  z=a(e)
  for i in range(len(e)):
   for j in range(i+1, len(e)):
    if sum(e[i:j+1])==z:return e[i:j+1]
 return min(d())+max(d())
print(a(e),b(e))