from app import db


class Station(db.Model):
    __tablename__ = 'station'

    id = db.Column(db.Integer, primary_key=True)
    ref_id = db.Column(db.String(64))
    name = db.Column(db.String(64))
    owner = db.Column(db.String(64))
    latitude = db.Column(db.Numeric(6, 4))
    longitude = db.Column(db.Numeric(7, 4))
    entries = db.relationship('JournalEntry', backref='station', lazy='dynamic')

    def __repr__(self):
        return '<Station {}>'.format(self.name)


class JournalEntry(db.Model):
    __tablename__ = 'journal_entry'
    __mapper_args__ = {
        'polymorphic_identity':'employee',
        'polymorphic_on': 'entry_type'
    }

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True)
    station_id = (db.Integer, db.ForeignKey('station.id'))
    entry_type = db.Column(db.String(32), nullable=False)

    def __repr__(self):
        return '<Journal Entry {}>'.format(self.timestamp)


class SynopticEntry(JournalEntry):
    __tablename__ = 'synoptic_entry'
    __mapper_args__ = {'polymorphic_identity': 'synoptic'}

    id = db.Column(db.Integer, db.ForeignKey('journal_entry.id'), primary_key=True)

    temperature = db.Column(db.Numeric(3, 1))
    pressure = db.Column(db.Numeric(5, 1))
    humidity = db.Column(db.Numeric(4, 1))
    precipitation = db.Column(db.Numeric(5, 2))
    wind_speed = db.Column(db.Numeric(3, 0))
    wind_azimuth = db.Column(db.Numeric(3, 0))


class HydrologicEntry(JournalEntry):
    __tablename__ = 'hydrologic_entry'
    __mapper_args__ = {'polymorphic_identity': 'hydrologic'}

    id = db.Column(db.Integer, db.ForeignKey('journal_entry.id'), primary_key=True)

    water_level = db.Column(db.Numeric(3, 1))


class AirQualityEntry(JournalEntry):
    __tablename__ = 'air_quality_entry'
    __mapper_args__ = {'polymorphic_identity': 'air_quality'}

    id = db.Column(db.Integer, db.ForeignKey('journal_entry.id'), primary_key=True)

    PM10 = db.Column(db.Numeric(4, 1))
    PM2_5 = db.Column(db.Numeric(4, 1))
    O3 = db.Column(db.Numeric(4, 1))
    NO_ = db.Column(db.Numeric(4, 1))
    NO2 = db.Column(db.Numeric(4, 1))
    NOx = db.Column(db.Numeric(4, 1))
    AQI = db.Column(db.Numeric(3, 0))
    

class IndoorEntry(JournalEntry):
    __tablename__ = 'indoor_entry'
    __mapper_args__ = {'polymorphic_identity': 'indoor'}

    id = db.Column(db.Integer, db.ForeignKey('journal_entry.id'), primary_key=True)

    temperature = db.Column(db.Numeric(3, 1))
    humidity = db.Column(db.Numeric(4, 1))
