session=input('File name jisme data save krna he : ')
line1="sun siya satya aasheesh hamaari poojahin mana kaamanaa tumhaaree"
line2= "pravishi nagara keeje sab kaajaa hridaya raakhi kaushalapura raajaa"
line3= "ubare anta na hoyee nibaahoo kaalanemi jimi raavana raahoo"
line4 = "vidhivasha sujana kusangati parihin fanimani samanija guna anusaraheen"
line5= "hoyee hai soyee jo raama rachi raakhaa ko kari tarka barhavahin shaakhaa"
line6= "muda mangalamaya santa samajoo jimi jaga jangama teeratha raajoo"
line7= "garala sudhaa ripu kare mitayi gopada sindhu anala sitalaayi"
line8= "varuna kubera suresha sameera rana sanamukha dhari kaahu na dheera"
line9= "sufala manoratha hoyee tihaare raama lakhana suni bhaye sukhaare"
vowel="aeiou"
conso="bcdfghjklmnpqrstvwxyz"
listl= [line1, line2, line3, line4, line5, line6, line7, line8, line9]
print()
print("                   RAM RAM RAM")
for i in listl:
	print(i)
	
listletters= []
for line in listl:
	for l in line:
		
print()

userl= input("Apne Akshar Likhe : ")
outL=[]
choi=" "
while len(choi) != 0 or choi != "end" or len(choi)==0 :
	
	userl= input("Apne Akshar Likhe : ")
	for line in listletters:
		linecount=1
		count=0
		for l in line:
				for p in userl:
					if l==p:
						count=count+1
		totalletters=len(line)
		percent=(count/totalletters)*100
		count=0
		print(line,"se samroopta", percent,"%")
		perS=str(percent)
		linec=str(linecount)
		out= linec+"se samroopta"+perS+"%"
		outL.append(out)
		linecount +=1
	choi=userl

fi= '/storage/emulated/0/DCIM/Python'+session+'.txt'
print("this is to check filepath is",fi)
try:
    # Attempt to open the file in read mode to check if it exists
    with open(fi, 'r') as file:
        pass
except FileNotFoundError:
    # If the file does not exist, create it and write data to it
    with open(fi, 'w') as file:
        for data in outL:
        	file.write(data)
    print('File not found, so it was created and data was written.')
except IOError:
    print('Error occurred while checking the file.')
else:
    # If the file exists, append data to it
    with open(fi, 'a') as file:
        for data in outL:
        	file.write(data)
    print('File found, so data was appended.')

		