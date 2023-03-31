class Person:
    def __init__(self, name):
        self.name = name
        self.friends = []
        

    def add_friend(self, new_friend):
        if new_friend not in self.friends:
            self.friends.append(new_friend)

    