from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# initialize our db
db = SQLAlchemy()

bcrypt = Bcrypt()

from .User import User, UserSchema
from .ParkingSlot import ParkingSlot