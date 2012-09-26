from google.appengine.ext import db

from models.event import Event

class Award(db.Model):
    """
    Awards represent FIRST Robotics Competition awards given out at an event.
    name is a general name and can be seen in /datafeeds/datafeed_usfirst_awards.py
    key_name is like '2012sj_rca'
    """
    name = db.StringProperty() #general name used for sorting
    official_name = db.StringProperty() #the official name used by first
    year = db.IntegerProperty() #year it was awarded
    winner = db.IntegerProperty() #who won the award
    awardee = db.StringProperty() #who won it
    event = db.ReferenceProperty(Event, required=True)
    
    @property
    def key_name(self):
        """
        Returns the string of the key_name of the Award object before writing it.
        """
        return str(self.year) + str(self.event.key_name) + '_' + str(self.name)
    
    @property
    def details_url(self):
        return "/award/%s" % self.get_key_name()

    @classmethod
    def getKeyName(self, event, name):
        return str(event.year) + str(event.key_name) + '_' + str(name)
        