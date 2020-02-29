class User:
    def __init__(self, username, password, coalition, bio):
        self.username = username
        self.password = password
        self.coalition = [coalition]
        self.bio = bio
        self.dict = {
            u'Username': u'' + self.username,
            u'Password': u'' + self.password,
            u'Coalitions': u'' + self.coalitions,
            u'Bio': u'' + self.bio
        }

    def update(self, key, newValue):
        for i in self.dict.keys():
            if i == key:
                self.dict[i] = newValue

class Coalition:
    def __init__(self, user_main, description):
        self.admin_user = user_main
        self.subscribers = [user_main]
        self.count = len(self.subscribers)
        self.description = description

    def add_user(self, user):
        self.subscribers.append(user)
        self.count += 1



