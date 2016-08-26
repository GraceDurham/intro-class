# import contact 
from contact import Contact 









def main(): 

	contact_list2=[]
	# contat 1
	first_name=raw_input ("Please enter a first name")
	last_name= raw_input ("Please enter a last name")
	mobile_number=raw_input ("Please enter a mobile number")
	email=raw_input ("Please enter an email")

	contact_little= Contact(first_name, last_name, mobile = mobile_number, email = email)
	contact_list2.append(contact_little)
	#contact 2
	# first_name="little" #raw_input ("Please enter a first name")
	# last_name="finger" #raw_input ("Please enter a last name")
	# mobile_number="4156666666"#raw_input ("Please enter a mobile number")
	# email="little.finger@evil.com" #raw_input ("Please enter an email")

	print contact_list2 
	print contact_list2[0].__dict__

main()









