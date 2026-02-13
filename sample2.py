ovpay=0
sum=0
for i in range(1,11):
print(&quot;Enter Working Hours of Emp &quot;,i,&quot;:&quot;)
h=int(input())
if(h&gt;40):
extra=h-40
ovpay=extra*12
print(&quot;Over time pay of emp &quot;,i,&quot; is &quot;,ovpay)
sum=sum+ovpay
else:
print(&quot;No Overtime Pay&quot;)

print(&quot;Total Overtime Pay of all employees : &quot;, sum)
