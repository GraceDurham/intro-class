my_list= ["bananas", "apples", "cupcakes", "beer"]

def check_list():
	choice = raw_input("what do you want to add to the shopping list ").lower()
	if choice in my_list:
		print "you already have it" 
	else:
		my_list.append(choice)
	
	my_list.sort()
	print
	
def remove_item_from_list():
	
	choice_remove =raw_input("what would you like to remove from the list ").lower()
	if choice_remove not in my_list:
		print "You don't have that item"		
	else:
		my_list.remove(choice_remove)

	my_list.sort()
	print my_list

def menu():
	menus = range(3)
	items = raw_input("Please choose one of the menu options: 0 - Main Menu 1 - Show current list 2 - Add an item to your shopping list")
	while (True):
		print "0 - Main Menu"

def main():
	check_list()
	remove_item_from_list()



if __name__ == '__main__':
	main()

	



