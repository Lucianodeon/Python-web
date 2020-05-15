import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.init_app(app)

def main():
    f = open("flights.cvs")
    reader=cvs.reader(f)
    for origin, destination, duration in reader:
        flight=Flight(origin=origin, destination=destination, duration=duration)
        db.session.add(flight)
        print(f"Added flight form {origin} to {destination} lasting {duration} minutes.")
    db.session.commit()
if __name__ == '__main__':
    with app.app.context():
        main()
