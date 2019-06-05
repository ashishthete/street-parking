# src/models/ParkingSlot.py
from geoalchemy2 import Geometry
from sqlalchemy import func

from . import db
import datetime

class ParkingSlot(db.Model):
  """
  Parking Slot Model
  """

  __tablename__ = 'parkingslots'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  location = db.Column(db.String(30))
  longitude = db.Column(db.Float)
  latitude = db.Column(db.Float)
  geo = db.Column(Geometry(geometry_type="POINT"))

  def __repr__(self):
    return "<Parking Slot {name} ({lat}, {lon})>".format(
      name=self.location, lat=self.latitude, lon=self.longitude)

  def get_parking_slots_within_radius(self, radius):
    """Return all cities within a given radius (in meters) of this parking_slot."""
    return ParkingSlot.query.filter(func.ST_Distance_Sphere(ParkingSlot.geo, self.geo) < radius).all()


  @classmethod
  def add_parking_slot(cls, location, longitude, latitude):
    """Put a new parking_slot in the database."""

    geo = 'POINT({} {})'.format(longitude, latitude)
    parking_slot = ParkingSlot(location=location,
                longitude=longitude,
                latitude=latitude,
                geo=geo)

    db.session.add(parking_slot)
    db.session.commit()
