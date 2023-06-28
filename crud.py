from model import db, User, Reservation, connect_to_db

def create_user(username):
    """Create and return a new user."""
    return User(username=username)

def get_user_by_username(username):
    """Get and return a user by their username."""
    return User.query.filter(User.username == username).first()

def create_reservation(user_id, date, time):
    """Create and return a new reservation."""
    return Reservation(user_id=user_id, date=date, time=time)

def get_res_on_date(date):
    """Return all the reservations on a given date."""
    return Reservation.query.filter(Reservation.date == date).all()

def user_booked_on_date(user_id, date):
    """Return whether a user has a res on a given date."""
    if Reservation.query.filter(Reservation.user_id == user_id, Reservation.date == date).first():
        return True
    return False

def slot_is_taken(date, time):
    """Return whether a date and time is already booked."""
    if Reservation.query.filter(Reservation.date == date, Reservation.time == time).first():
        return True
    return False