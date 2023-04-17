from flask import Flask
from app import db, DevelopmentConfig
from app.controllers.partner import partner_blueprint
from app.controllers.csv import csv_blueprint

app = Flask(__name__)

app.register_blueprint(partner_blueprint)
app.register_blueprint(csv_blueprint)

app.config.from_object(DevelopmentConfig)

db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        db.session.commit()

    app.run(host='0.0.0.0')
