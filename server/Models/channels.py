from . import db

class Channels(db.Model):
    __tablename__ = 'channels'
    id = db.Column(db.Integer, primary_key=True)
    channel_id = db.Column(db.Text)
    title = db.Column(db.Text)
    image_link = db.Column(db.Text)
    description = db.Column(db.Text)

    def __init__(self, channel_id, title, image_link, description):
        self.channel_id = channel_id
        self.title = title
        self.image_link = image_link
        self.description = description
