vip = []
ordinary = []

print('--------------------------------')

def the_vip_list():

    ### Search through the vip file
    ### Add the names to the vip list

    with open('vip.txt', 'r') as f:
        data = f.readlines()
        for line in data:
            names = line.rstrip('\n')
            vip.append(names)
        return vip

def the_ordinary_list():

    ### Search through the ordinary file
    ### Add the names to the ordinary list

    with open('ordinary.txt', 'r') as f:
        data = f.readlines()
        for line in data:
            names = line.rstrip('\n')
            ordinary.append(names)
        return ordinary

def registration_checker():

    ### Search through the vip and ordinary lists
    ### Check if the user is registered

    vip = the_vip_list()
    ordinary = the_ordinary_list()

    # Loop through the lists,
    # Compare with the user input
    # If there is, then return that clients name and catergory
    # If not return user not registered

    for s in vip:
        if username.lower() in s.lower():
            print(s + "\n VIP")
    # if username.lower() not in s.lower():
    #         print("Client is not registered")

    for r in ordinary:
        if username.lower() in r.lower():
	        print(r + "\n Ordinary")

    print('--------------------------------')
    print('')

print("Enter the name: ")
username = input()
print('--------------------------------')

registration_checker()
