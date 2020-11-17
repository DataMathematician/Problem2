from app import db, session, Base

class BigData(Base):
    __tablename__ = 'csv_reports'                   # имя табл в базе
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(250),nullable=False)
    volume = db.Column(db.Integer,nullable = False)