def sleep_end():
	import time
	time.sleep(5)

def intro():
	print("\nWelcome to the Heath Management Program ! \nDeveloved by HAMMAD ALI ")
	print("In this program you can record your diet and exercise and can also view them when required. ")
	print("So lets get started!") 
	print("NOTE: YOUR INPUT IS NOT CASE SENSITIVE AND SPACES ARE ALSO NOT CONSIDERED\ni.e. ABC=abc=a b c")

def getdatetime():
	import datetime
	a = datetime.datetime.now()
	b = a.strftime('[%d/%m/%y %H:%M:%S]')
	return b

def update(x):
	with open(f"{clientname}{feature}.txt" , "a") as file:
		file.write(getdatetime())
		file.write(f"\t{x}\n")
		print ("Record updated successfully!\n")

def fetch():
	with open(f"{clientname}{feature}.txt") as file:
		print("")
		for line in file :
			print(line , end="")

def remove_spaces(str):
	str1 = ""
	for letter in str:
		if letter == " ":
			str1 += ""
		else:
			str1 += letter
	return str1.lower()

def cn():
	global clientname
	clientname = input("\nTYPE your name : \n")
	clientname = remove_spaces(clientname)
	if clientname == "":
		print("This field can't be left empty")
		cn()

def final():

	task = input(f"\n{clientname.upper()} TYPE your option (Record or Fetch):\n")
	task = remove_spaces(task)

	if task == "record" :
				
		def dw():
			global done_what
			done_what = input(f"\n{clientname.upper()} What you want to add to your record :\n")
			done = remove_spaces(done_what)
			if done == "":
				print("Please give some input!")
				dw()
		dw()
						
		update(done_what)
		
	elif task == "fetch":
		try:
			fetch()
		except Exception as error :
			print (f"\n{clientname.upper()} First add something to your record\n")
		
	else:
		print(f"\n{clientname.upper()} choose correct task\n")
		final()
		
def rc():
	run_choice = input(f"{clientname.upper()} Do you want to run again (y/n)\n")
	run_choice = remove_spaces(run_choice)
	if run_choice == "n" :
		print(f"\nEnjoyed working with you {clientname.upper()}\n Bye!")
		sleep_end()
		xyz == False
	elif run_choice == "y" :
		xyz == True
	else :		
		print(f"\n{clientname.upper()} Choose correct option\n") 
		rc()



if __name__ == '__main__':
	xyz = True
	intro()
	cn()
	
	while xyz == True:

		feature = input(f"\n{clientname.upper()} TYPE on which you want to work (Diet or Exercise):\n")
		feature = remove_spaces(feature)
		feature_list = ["diet", "exercise"]
		while feature not in feature_list:
			print(f"\n{clientname.upper()} choose correct feature \n")
			feature= input(f"\n{clientname.upper()} TYPE on which you want to work (Diet or Exercise):\n")

		final()
		rc()
