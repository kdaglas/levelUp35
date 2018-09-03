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

# def registration_checker(name):
#     return checker(name)

def registration_checker():

    ### Search through the vip and ordinary lists
    ### Check if the user is registered

    vip = the_vip_list()
    ordinary = the_ordinary_list()

    # print(the_vip_list())
    # print('--------------------------------')
    # print(the_ordinary_list())
    # print('--------------------------------')

    print("Enter the name: ")
    username = input()
    print('--------------------------------')

    # if username in vip:
    #     print("Client registered")
    # elif username in ordinary:
    #     print("Client is registered")
    # else:
    #     print("Client is not registered")

    # Loop through the lists,
    # Compare with the user input
    # If there is, then return that clients name and catergory
    # If not return user not registered

    for s in vip or ordinary:
        if username.lower() in s.lower():
            if len(username) > 0:
	            print(s + "\n VIP")

    for r in ordinary:
        if username.lower() in r.lower():
            if len(username) > 0:
	            print(r + "\n Ordinary")

    # if s not in username:
    #     print("Client not registered")

    print('--------------------------------')
    print('')

registration_checker()
