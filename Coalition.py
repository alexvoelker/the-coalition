class User:
    def __init__(self, username, password, bio):
        self.username = username
        self.password = password
        self.coalitions = []
        self.coalitions_made = []
        self.bio = bio
        self.stories = []
        self.dict = {
            u'Username': u'' + self.username,
            u'Password': u'' + self.password,
            u'Bio': u'' + self.bio
        }
        print("Username: " + self.username
              "\nPassword: " + self.password
              "\nBio: " + self.bio)

    def update(self, key, newValue):
        for i in self.dict.keys():
            if i == key:
                self.dict[i] = newValue
        print(self.dict)
    
    def add_coalition(self, coalition):
        self.coalitions.append(coalition)
        for i in self.coalitions:
            print(i.name)
            
    
    def add_story(self, story):
        self.stories.append(story)
        for i in self.stories:
            print(i.title)
            
    def make_coalition(self, cTitle, cDescription):
        self.coalitions_made.append(Coalition(cTitle, self, cDescription))
        for i in self.coalitions_made:
            print(i.name)
        
class Coalition:
    def __init__(self, name, user_main, description):
        self.name = name
        self.admin_user = user_main
        self.subscribers = [User]
        self.count = len(self.subscribers)
        self.description = description
        print("Name: " + self.name
              "\nAdminUser: " + self.admin_user.username
              "\nCount: " + self.count
              "\nDescription: " + description)
        
    def add_user(self, user):
        self.subscribers.append(user)
        self.count += 1
        for i in self.subscribers:
            print(i.name)

class Story:
    def __init__(self, title, body):
        self.title = title
        self.body = body
        print("Title: " + self.title + "\nBody: " + self.body) 
