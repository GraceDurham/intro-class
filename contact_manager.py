# import contact 
from contact import Contact 









def main(): 

	contact_list2=[]
	# contat 1
	_break = None
	while True:
		_break = raw_input("press 2 to break")
		print "let's make a contact list"
		first_name=raw_input ("Please enter a first name")
		last_name= raw_input ("Please enter a last name")
		mobile_number=raw_input ("Please enter a mobile number")
		email=raw_input ("Please enter an email")

		contact_little= Contact(first_name, last_name, mobile = mobile_number, email = email)
		contact_list2.append(contact_little)
		if _break == "2":
			break

	print contact_list2 

	for obj in contact_list2:
		print obj.__dict__




main()









