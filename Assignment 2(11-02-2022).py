Sno=int(input('enter student no:'))
Sname=input('enter student name:')
Sgroup=input('enter student group:') 
S1=int(input('maths marks'))
S2=int(input('chemistry marks'))
S3=int(input('computers marks'))
S4=int(input('english marks'))
S5=int(input('telugu marks'))
S6=int(input('OB marks'))
Total=S1+S2+S3+S4+S5+S6
Average=Total/6
if Average>=91: 
       print("O-grade")
elif Average>=81:
       print ("A-grade")
elif Average>=71: 
       print ("B-grade")
elif Average>=61: 
       print("C-grade")
elif Average>=51: 
       print("D-grade")
else:
       print("FAIL")
