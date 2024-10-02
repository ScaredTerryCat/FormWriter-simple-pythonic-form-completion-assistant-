from keyboard import write
from time import sleep
stringer=""
strings=[]
stringsCount=int(input("Enter strings count:"))
for i in range(stringsCount):
	stringer=input(f"string {i+1} : ")
	strings.append(stringer)
intervalBetween=int(input("Type interval between strings writing: "))
beforeT=int(input("Interval of time before starting: "))
sleep(beforeT)
for i in range(stringsCount):
	write(strings[i])
	sleep(intervalBetween)
	if i+1<stringsCount:
		next=strings[i+1]
		print(f"next: {next}")
	else:
		print("strings over")
