vip = []
ordinary = []

print('--------------------------------')

with open('vip.txt', 'r') as f:
    data = f.readlines()
    for line in data:
        names = line.strip()
        vip.append(names)

with open('ordinary.txt', 'r') as f:
    data = f.readlines()
    for line in data:
        names = line.strip()
        ordinary.append(names)

def registration_checker():
    print("Enter your username: ")
    username = input()

    print('--------------------------------')
    
    if username in vip:
        print('User is registered')
    else:
        print('User not registered')

    print('--------------------------------')


registration_checker()
