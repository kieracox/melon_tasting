from model import db, User, Reservation, connect_to_db
from datetime import datetime, timedelta

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

def calculate_available_slots(reservations, start_time=None, end_time=None, ):
    if start_time:
        start_time = datetime.strptime(start_time, '%I:%M %p')
    else:
        start_time = datetime.strptime('12:00 AM', '%I:%M %p')
    if end_time:
        end_time = datetime.strptime(end_time, '%I:%M %p')
    else:
        end_time = datetime.strptime('11:59 PM', '%I:%M %p')
    
    available_slots = []

    current_time = start_time
   
    while current_time + timedelta(minutes=30) <= end_time:
        slot_start = current_time
        slot_end = current_time + timedelta(minutes=30)

        slot_overlaps = any(
            reservation_start <= slot_start < reservation_end or
            reservation_start < slot_end <= reservation_end
            for reservation_start, reservation_end in reservations
        )

        if not slot_overlaps:
            available_slots.append({
                'start': slot_start.strftime('%I:%M %p'),
                'end': slot_end.strftime('%I:%M %p')
            })
        
        current_time += timedelta(minutes=30)
    
    return available_slots