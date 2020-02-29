class User:
    def __init__(self, username, password, bio):
        self.username = username
        self.password = password
        self.coalitions = []
        self.bio = bio
        self.stories = []
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
        print(self.dict)
    
    def add_coalition(self, coalition):
        self.coalitions.append(coalition)
    
    def add_story(self, story):
        self.stories.append(story)
        
        
class Coalition:
    def __init__(self, user_main, description):
        self.admin_user = user_main
        self.subscribers = [User]
        self.count = len(self.subscribers)
        self.description = description

    def add_user(self, user):
        self.subscribers.append(user)
        self.count += 1
        print(self.subscribers + " and the user count is " + self.count)

class Story:
    def __init__(self, title, body):
        self.title = title
        self.body = body
