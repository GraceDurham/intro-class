# contacts = {"grace": {"name":"gracedurham", "phonenumber":"8168302572"}, "Timea": {"name":"timeaurban", "phonenumber": "6502769342"}, "daniella": {"name":"daniellarivera", "phonenumber":"4152696022"}}

# def add_contacts(): 
# 	pass


# def change_number():
# 	pass 


# def change_name():
# 	pass 

# def menu():
# 	print "Press 1 t"




# def main():
# 	grace =	contacts["grace"]
# 	grace["phonenumber"] = "88888888888"


# if __name__ == '__main__':
# 		main()	


class Contact(object):
	def __init__(self, first_name, last_name, email = "", mobile = "", work = ""):
		self.first_name= first_name
		self.last_name= last_name
		self.email=email 
		self.mobile=mobile 
		self.work=work 

	def send_text(self, message="hi"):
		print "to:  %s - %s" % (self.mobile, message)

	def send_email(self, message):
		print "to: %s - %s"	% (self.email, message)

def main():
	contact_list=[]

	name1=Contact("Jon", "Snow",mobile="8168302572",email="Jonsnow@gmail.com")
	name2=Contact("Tyrion", "Lannister", mobile = "4156995555", email = "tyrion@gmail.com")
	name3 = Contact("Danaerys", "Dragon Lady", mobile = "411211222", email = "dragonlady@gmail.com")
	name1.send_text("You know nothing John snow")
	name1.send_email("You still know nothing John Snow")

	contact_list.append(name1)
	contact_list.append(name2)
	contact_list.append(name3)

	for item in contact_list:
		print item.first_name, item.last_name, item.email, item.mobile
		print item.send_text("Hey everyone in GoT!")



	

if __name__ == '__main__':
	main()	


