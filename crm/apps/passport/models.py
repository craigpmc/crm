import datetime
from crm.db import db, BaseModel


class Passport(db.Model, BaseModel):

    __tablename__ = "passports"

    passport_fullname = db.Column(
        db.String(255),
        nullable=False,
        index=True
    )

    passport_number = db.Column(
        db.Text(),
        index=True,
        nullable=False
    )

    issuance_date = db.Column(
        db.Date(),
        default=datetime.date(1990, 1, 1),
        nullable=False
    )
    expiration_date = db.Column(
        db.Date(),
        default=datetime.date(2020, 1, 1),
        nullable=False
    )
    country_id = db.Column(
        db.String(5),
        db.ForeignKey('countries.id')
    )

    contact_id = db.Column(
        db.String(5),
        db.ForeignKey('contacts.id')
    )

    def __str__(self):
        return "Passport {}".format(self.passport_fullname)
