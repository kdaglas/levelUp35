f = open("VIP.txt", "r")
f = open("ORD.txt", "r")

def Checker():
    print("Enter your username: ")
    username = input()
    if f.mode == 'r':
        names = f.read()
        if username in names:
            print(username)
        else:
            print("User not in list")

if __name__ == "__main__":
    Checker()