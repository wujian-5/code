class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None

    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before

    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after

    def getBefore(self):
        return self.before

    def getAfter(self):
        return self.after

    def myName(self):
        return self.name


eric = Frob('eric')
andrew = Frob('andrew')
ruth = Frob('ruth')
fred = Frob('fred')
martha = Frob('martha')


def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob: a Frob with no links
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    
    """
    while atMe != None and atMe.myName() <= newFrob.myName():
        before = atMe
        atMe = atMe.getAfter()
        after = atMe
    while atMe != None and atMe.myName() > newFrob.myName():
        after = atMe
        atMe = atMe.getBefore()
        before = atMe

    if before != None:
        newFrob.setBefore(before)
        before.setAfter(newFrob)
    if after != None:
        newFrob.setAfter(after)
        after.setBefore(newFrob)


insert(eric, andrew)
insert(eric, ruth)
insert(eric, fred)
insert(ruth, martha)

