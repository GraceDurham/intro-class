my_list = []

def add_list():
	choice = raw_input("what do you want to add to the shopping list ").lower()
	if choice in my_list:
		print "you already have it" 
	else:
		my_list.append(choice)
	
	my_list.sort()

#create a function named print_list that uses a for loop to iterate over 
# the array my_list and print each item
def print_list():
	for item in my_list:
		print(item)


def remove_item_from_list():
	choice_remove =raw_input("what would you like to remove from the list ").lower()
	if choice_remove not in my_list:
		print "You don't have that item"		
	else:
		my_list.remove(choice_remove)

	my_list.sort()



def menu():
	while True:
		print("0 - main menu.")
		print("1 - show current list.")
		print("2 - add an item to your shopping list.")
		print("3 - remove an item from your shopping list.")
		print ( "4 - quit the program.\n")

		menu_items = raw_input("Please choose one of the menu options: 0, 1, 2, 3, or 4\n")

		if menu_items =="1":
			print_list()

		elif menu_items == "2":
			add_list()

		elif menu_items == "3":
			remove_item_from_list()

		elif menu_items == "4":
			break		


		else :
			print("Select 0, 1, 2, 3, 4.")
		

		


def main():
	menu()

# def main():
# 	check_list()
# 	remove_item_from_list()



if __name__ == '__main__':
	main()

	



