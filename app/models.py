from . import db

class Service(db.Model):
    id = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    incidents = db.relationship('Incident', backref='service', lazy=True)

class Incident(db.Model):
    id = db.Column(db.String(64), primary_key=True)
    service_id = db.Column(db.String(64), db.ForeignKey('service.id'), nullable=False)
    status = db.Column(db.String(64), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

class Team(db.Model):
    id = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    services = db.relationship('Service', secondary='team_services', lazy='subquery',
    backref=db.backref('teams', lazy=True))

class EscalationPolicy(db.Model):
    id = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(128), nullable=False)

team_services = db.Table('team_services',
    db.Column('team_id', db.String(64), db.ForeignKey('team.id'), primary_key=True),
    db.Column('service_id', db.String(64), db.ForeignKey('service.id'), primary_key=True)
)
