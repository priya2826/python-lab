d=int(input("Enter Number of days: "))
fine=0
if(<=5):
fine=d*0.50
print("Fine : ",float(fine))
elif(d&gt;5 and d&lt;=10):
i=d-5
fine=(i*1)+(5*0.5)
print("Fine : ",float(fine))
elif(d&gt;10 and d&lt;=30):
i=d-10
fine=(i*5)+(5*0.5)+(5*1)
print(";Fine : ",float(fine))
else:
i=d-10
fine=(i*5)+(5*0.5)+(5*1)
print("Your Membership is cancelled")
print("Fine amount (Rs): ",float(fine))
