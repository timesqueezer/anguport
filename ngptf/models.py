from ngptf import db

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    desc = db.Column(db.String(200))
    
    def __init__(self, title, desc):
        self.title = title
        self.desc = desc
    
    def __repr__(self):
        return '<Project %r>' % self.title