from app import db, Users, Cars

db.drop_all()
db.create_all()

testuser = Users(first_name='John',last_name='Wick') # Extra: this section populates the table with an example entry

db.session.add(testuser)
db.session.commit()

car1 = Cars(number_plate="KX12345", owner_id=testuser)

db.session.add(car1)
db.session.commit()