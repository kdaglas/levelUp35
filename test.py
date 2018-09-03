# # Declare empty lists that shall contain names read from the files
# ordinary_list = []
# vip_list = []

# # Read ordinary file and append names to a list
# ordinary = open("ordinary.txt", "r")
# ordinary_list = [line.rstrip() for line in ordinary.readlines()]


# # Read VIP file and append names to the vip_list
# vip = open("vip.txt", "r")
# vip_list = [line.rstrip() for line in vip.readlines()]

# # Request user to enter their name
# singlename = input("Enter single name:")


# def registration_checker_ordinary(singlename):
#     ''' Function to check if a guest is registered
#      in ordinary list '''
#     return ''.join(name for name in ordinary_list if singlename in name) + ", ORDINARY"


# def registration_checker_vip(singlename):
#     ''' Function to check if a guest is registered
#     in vip_list'''
#     return ''.join(name for name in vip_list if singlename in name) + ", VIP"


# def registration_checker(singlename):
#     ''' Function that checks if the user exists either in ordinary_list
#     or in vip_list'''
#     if singlename in ordinary_list:
#         return registration_checker_ordinary(singlename)
#     elif singlename in vip_list:
#         return registration_checker_vip(singlename)
#     else:
#         return "User not registered"
        
# print(registration_checker(singlename))

# ordinary.close()
# vip.close()


# Load data files
ordinary_file = open("ordinary.txt", "r")
vip_file = open("vip.txt", "r")
# lists for storing names
ord_arr = []
vip_arr = []

# Store names in lists
for o in ordinary_file.readlines():
	ord_arr.append(o)

for v in vip_file:
	vip_arr.append(v)
	
def registration_checker(name):
	print(check_for_name(name))
		
	

# Method checks and returns names if in the lists	
def check_for_name(nm):
    
	# check and return matching names to arrays
	# if no matching names, arrays shall be empty
	# also convert all names to lower case for uniformity
	match_ord = [s for s in ord_arr if nm.lower() in s.lower()]
	match_vip = [s for s in vip_arr if nm.lower() in s.lower()]
	
	# Check length of array and return appropriate response
	if len(match_ord)>0:
		return match_ord[0]+" ORDINARY"
	elif len(match_vip)> 0:
		return match_vip[0]+" VIP"
	else:
		return "Not Registered"
	
name=input("Please enter your first name:")
		
# Call function to test
registration_checker(name)