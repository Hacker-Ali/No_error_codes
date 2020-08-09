def sleep_end():
	import time
	time.sleep(5)

def scorefunc():
	try:
		with open(f"{clientname}score.txt") as file:
			return int(file.readline())
	except Exception as e:
		with open(f"{clientname}score.txt", "w") as file:
			file.write("0")
			return 0 

def updatescore(newscore):
	with open(f"{clientname}score.txt", "w") as file:
		file.write(str(newscore))
		return

def fastfoodfunc():
	try:
		with open("fastfood.txt") as file:
			return file.readlines()
	except Exception as e:
		return 

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
		print ("\nRecord updated successfully!")

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
		print("\nThis field can't be left empty")
		cn()

def dw():
	global done_what
	done_what = input(f"\n{clientname.upper()} What you want to add to your record :\n").lower()
	done = remove_spaces(done_what)
	if done == "":
		print("\nPlease give some input!")
		dw()

def final():
	global score
	task = input(f"\n{clientname.upper()} TYPE your option (Record or Fetch):\n")
	task = remove_spaces(task)

	if task == "record" :
		dw()
		update(done_what)
		if feature=="exercise" and done_what in exlist:
			print(f"\n{clientname.upper()} You Lost your score for not doing exercise.")
			updatescore(score-10)
			score=scorefunc()
			print(f"\n{clientname.upper()} Your new score is {score}")
		elif feature=="exercise" and done_what not in exlist:
			print(f"\n{clientname.upper()} Your score icreased for doing exercise.")
			updatescore(score+10)
			score=scorefunc()
			print(f"\n{clientname.upper()} Your new score is {score}")
		elif feature=="diet" and done_what not in fastfoodlist:
			print(f"\n{clientname.upper()} Your score increase for eating healthy food.")
			updatescore(score+10)
			score=scorefunc()
			print(f"\n{clientname.upper()} Your new score is {score}")
		elif feature=="diet" and done_what in fastfoodlist:
			print(f"\n{clientname.upper()} You Lost your score for eating fast food.")
			updatescore(score-10)
			score=scorefunc()
			print(f"\n{clientname.upper()} Your new score is {score}")
		else:
			pass
	
	elif task == "fetch":
		try:
			fetch()
		except Exception as error :
			print (f"\n{clientname.upper()} First add something to your record")
		
	else:
		print(f"\n{clientname.upper()} choose correct task")
		final()
		
def rc():
	run_choice = input(f"\n{clientname.upper()} Do you want to run again (y/n)\n")
	run_choice = remove_spaces(run_choice)
	if run_choice == "n" :
		print(f"\n{clientname.upper()} Your Final score is {score}")
		print(f"\nEnjoyed working with you {clientname.upper()}\n Bye!")
		sleep_end()
		quit()
	elif run_choice == "y" :
		pass
	else :		
		print(f"\n{clientname.upper()} Choose correct option") 
		rc()

def cs():
	check_score = input(f"\n{clientname.upper()} Do you want to check you score.(y/n)\n")
	check_score = remove_spaces(check_score)
	if check_score == "y" :
		print(f"\n{clientname.upper()} Your score is {score}")
	elif check_score!="n" :		
		print(f"\n{clientname.upper()} Choose correct option") 
		cs()


if __name__ == '__main__':
	intro()
	cn()
	
	score=scorefunc()
	fastfoodlist=list(map(lambda x: x[:len(x)-1], fastfoodfunc()))
	cs()
	exlist=["nothing", "nope", "not done", "no", "not", "forgot", "forget", "notdone"]
	if fastfoodlist==None:
		print("\nSome Files are missing! Please arrange them before running...")
		rc()

	while True:

		feature = input(f"\n{clientname.upper()} TYPE on which you want to work (Diet or Exercise):\n")
		feature = remove_spaces(feature)
		feature_list = ["diet", "exercise"]
		while feature not in feature_list:
			print(f"\n{clientname.upper()} choose correct feature")
			feature= input(f"\n{clientname.upper()} TYPE on which you want to work (Diet or Exercise):\n")

		final()
		rc()
