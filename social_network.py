class User:
    """User Class"""
    def __init__(self, name):
        self.name= name
        self.iden = 0
        self.connections = []

    def user_name(self, iden):
        self.iden = iden

    def add_friends(self, connections):
        self.connections.append(connections)

user1= User("Bob")
print(user1.name)

user1.add_friends("Robert")
print(user1.connections)
user1.add_friends("Ruby")
print(user1.connections)

user2= User("Sophie")
print(user2.name)


class Network:
    def __init__(self):
        self.us = []

    def set_users(self):
        return len(self.us)


    def add_user(self,us):
        if login not in self.us:
            self.us.append(us)
            print(self.us)
        else:
            print("Invalid username. Try again.")

    def getUserID(self,name):
        found = False
        for b in self.us:
            if name == b :
                found = True

        if found == True:
            print(iden)

    def addconnection(self,user1,user2):
        self.user1 = user1
        self.user2 = user2
        for c in self.connections:
            if user2.iden in self.connections:
                print("You are connected to", user1)
            else:
                print("You are not connected to", user1)
                answer = input("Do you want to be connected?")
                if answer == "yes":
                    user2.append(connections)
                else:
                    print("Sucks to be you!")

    def printConnections(self,iden):
        print(connections)


net = Network()
beginning=input("Hello! Would you like to create a username? 'Yes' or 'No':")
if beginning == "Yes":
    login = input("Username:")
    net.add_user(login)
else:
    print("Goodbye!")
