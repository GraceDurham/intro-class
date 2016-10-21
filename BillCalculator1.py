

def calculate_tip(bill_amount,tip_percent):
    tip = bill_amount *(float(tip_percent)/100)
    return tip    

print calculate_tip(20,10)

def calculate_total_bill(tip_amount, bill_amount):
    total_money=tip_amount + bill_amount
    return total_money



print calculate_total_bill(20,10)    

def calculate_tip(bill_amount,tip_percent):
    tip = bill_amount *(float(tip_percent)/100)
    return tip    

print calculate_tip(20,10)

def split_bill(bill_amount, num_people):
    split = bill_amount/num_people
    return split

print split_bill(100,10)

def main():    
    print "Welcome to bill calculator"    
    original_bill_amount=float(raw_input("Please enter the original bill amount"))
    tip_percentage=int(raw_input("Please enter the tip percentage"))

    choice_1 = int(raw_input("Please choose from choice 1 or 2 choice 1 is calculate tip")) 
    if choice_1 == 1:

        tip_amount=original_bill_amount * tip_percentage/100
        print tip_amount
    choice_2= int(raw_input("Please enter number"))   
    if choice_2==2:
        total_bill_amounts=int(raw_input("Please enter total bill amount")) 
        number_of_people_split=int(raw_input("How many people would you like to split the bill with "))






if __name__ == '__main__':
    main()

