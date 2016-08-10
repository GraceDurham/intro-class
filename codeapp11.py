
# num=raw_input("Please enter a number")


def check_prime(num):
    num_list = range(2,num)
    for i in num_list:
    	if num % i==0:
    		return "not a prime number"
    
    return "is a prime number"




print check_prime(7)