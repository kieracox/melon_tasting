import os

import crud
import model
import server
from datetime import datetime

os.system("dropdb reservations")
os.system("createdb reservations")

model.connect_to_db(server.app)
model.db.create_all()

test_user = crud.create_user("kieracox")

test_res = crud.create_reservation(1, datetime.now().date(), datetime.strptime('11:00', '%H:%M').time())

test_res_2 = crud.create_reservation(1, datetime(2023,7,8).date(), datetime.strptime('16:00', '%H:%M').time())

model.db.session.add(test_user)
model.db.session.add(test_res)
model.db.session.add(test_res_2)
model.db.session.commit()