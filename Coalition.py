import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("/Users/avi/Documents/the-coalition-firebase-adminsdk-prmz5-e1205054d3.json")
default_app = firebase_admin.initialize_app(cred)

db = firestore.client()

print("SERVER GO")

user_total = {}
user_count = 0
user_coalitions = {}
coalitions_dict = {}
coalitions_count = 0


class Coalition:
    def __init__(self, name, user, description, story):
        self.name = name
        self.stories = {}
        self.admin_user = user
        self.subscribers = [User]
        self.count = len(self.subscribers)
        self.description = description
        global coalitions_count
        self.coalition_id = coalitions_count
        coalitions_dict[coalitions_count] = self
        coalitions_count+=1
        self.doc_ref = db.collection(u'Coalitions').document(self.name)

    def add_user(self, user2):
        self.subscribers.append(user2)
        user2.join_coalition(self)
        self.count += 1
        for i in self.subscribers:
            print(i.username)
    def add_story(self, story):
        self.stories[story.story_id] = story
        story_doc_ref = db.collection(u'Stories').document(story.title)
        story_doc_ref.set({
            u'Author': story.user.username,
            u'Title': story.title,
            u'Body': story.body,
            u'Coalition': story.coalition
        })
        self.doc_ref.update({
            u'Story': story.title
        })



story_dict = {}
story_count = 0


class Story:
    def __init__(self, title, body, user, coalition_type):
        self.title = title
        self.body = body
        self.user = user
        self.coalition = u''
        self.likes = 0
        if coalition_type == u'Equality':
            self.coalition = u'Equality'
        elif coalition_type == u'Environment':
            self.coalition = u'Environment'
        elif coalition_type == u'Education':
            self.coalition = u'Education'
        elif coalition_type == u'Worker\'s Rights':
            self.coalition = u'Worker\'s Rights'
        else:
            self.coalition = u'Other'
        global story_count
        self.story_id = story_count
        story_dict[story_count] = self
        story_count += 1
        self.doc_ref = db.collection(u'Stories').document(self.title)
        self.stories = []
        for i in story_dict.items():
            if i[1].coalition == self.coalition:
                self.stories.append(i[1].title)
        print("Title: " + self.title + "\nBody: " + self.body + "\nCoalition: " + self.coalition)
        print(u'\n\nAll this information has been uploaded to the database.')


    def up_like(self):
        self.likes += 1


stringKeys = u''
def make_string(list):
    global stringKeys
    for i in list:
        stringKeys += str(i) + u' '
    print(type(stringKeys))
    return stringKeys


def make_list(string):
    list = []
    for i in range(len(string)):
        if string[i] == u' ':
            continue
        else:
            list.append(int(string[i]))
    return list


class User:
    passwordNumber = 0
    def __init__(self, username, bio):
        self.username = username
        self.password = self.passwordNumber
        self.passwordNumber += 1
        self.bio = bio
        self.stories = []
        self.coalitions_made = []
        self.coalitions = []
        global user_count
        self.user_id = user_count
        self.doc_ref = db.collection(u'User').document(username)
        user_total[user_count] = self
        user_count += 1
        self.none_or_not = u''
        if len(self.stories) == 0:
            self.none_or_not = u'They have no stories.'
        self.dict = {
            u'Username': u'' + self.username,
            u'Password': u'' + self.password,
            u'Bio': u'' + self.bio,
            u'Stories': self.none_or_not
        }
        self.doc_ref.set(self.dict)
        print(u'User has been created:' +
              u'\n' + self.dict[u'Username'] + u' is the username,' +
              u'\n' + self.dict[u'Password'] + u' is the password,' +
              u'\nThe person\'s bio:\n' + self.bio +
              u'\n' + self.dict[u'Stories'] + u' are the stories belonging to this User' +
              u'\n\nThese have all been updated to the database.')

    """def update(self, key, newValue):
        for i in self.dict.keys():
            if i == key:
                self.dict[i] = newValue
            print(self.dict)"""

    """def join_coalition(self, coalition_id):
        self.coalitions.append(coalition_id)
        self.doc_ref.update({
            u'Coalitions Part Of': make_string(self.coalitions)
        })

    def add_coalitionMade(self, coalition_id):
        self.coalitions_made.append(coalition_id)
        for i in self.coalitions_made:
            print(i)
        self.doc_ref.update({
            u'CoalitionsPartof': make_string(self.coalitions_made)
        })
    """

    def add_story(self, story):
        print(self.stories)
        for i in self.stories.keys():
            print(i)

request_count = 0

boolean = True
while boolean:
    if db.collection(u'Request').document(u'' + str(request_count)).get().exists or \
            db.collection(u'Request').document(u'' + str(request_count+1)).get().exists:
        share_ref = db.collection(u'Request').document(u'' + str(request_count))
        doc = share_ref.get().to_dict()
        doc_name = doc[u'DocRef']
        if "Story" in str(doc[u'Header']):
            story_doc_ref = db.collection(u'Stories').document(doc_name)
            story_doc = story_doc_ref.get().to_dict()
            story = Story(story_doc[u'Title'], story_doc[u'Body'], story_doc[u'Author'], story_doc[u'Coalition_Type'])
        elif "User" == str(doc[u'Header']):
            user_doc_ref = db.collection(u'User').document(doc_name)
            user_doc = user_doc_ref.get().to_dict()
            user = User(user_doc[u'Username'], user_doc[u'Bio'])
        else:
            stories = []
            for i in story_dict.items():
                if i[1].coalition == doc_name:
                    stories.append(i[1])
        request_count += 1
    else:
        stall = str(input("Are u done?: "))
        if stall == "kill":
            boolean = False