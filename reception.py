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
            vip.append({names, 'ORDINARY'})
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

    print("Enter your username: ")
    username = input()

    print('--------------------------------')
    
    if username in vip or ordinary:
        print('User is registered')
    else:
        print('User not registered')

    print('--------------------------------')
    print('')

registration_checker()
