import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()

Base.prepare(engine, reflect = True)

Measurement = Base.classes.measurement


app = Flask(__name__)

@app.route("/")
def welcome():
    return(
        f"Here are all of the available routes: <br>"
        f"/api/v1.0/precipitation<br>"
        f"/api/v1.0/stations<br>"
        f"/api/v1.0/tobs"
        
    )

@app.route("/api/v1.0/precipitation")
def precip():
    session = Session(engine)

    precip = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= '2016-08-23').all()

    session.close()

    #precip_list = []
    precip_dict = {}
    for date, prcp in precip:
        precip_dict[date] = prcp
        # precip_dict[prcp] = precip
        # precip_list.append(precip_dict)

    return jsonify(precip_dict)


# @app.route("/api/v1.0/precipitation")
# def precip():
#     session = Session(engine)

#     precip = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= '2016-08-23').all()

#     session.close()

#     precip_list = list(np.ravel(precip))


#     for date, prcp in precip:
#         precip_dict = {}
#         precip_dict["date"] = date
#         precip_dict["prcp"] = precip
#         precip_list.append(precip_dict)

#     return jsonify(precip_list)


@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)

    stations = session.query(Measurement.station).group_by(Measurement.station).all()

    session.close()

    station_list = list(np.ravel(stations))

    return jsonify(station_list)


@app.route("/api/v1.0/tobs")
def active_station():
    session = Session(engine)

    station_temp = session.query(Measurement.tobs).filter(Measurement.date >= '2016-08-23').\
    filter(Measurement.station == 'USC00519281').all()

    session.close()

    station_temp_list = list(np.ravel(station_temp))

    return jsonify(station_temp_list = station_temp_list)



@app.route("/api/v1.0/<start>")
def start_date():




if __name__ == '__main__':
    app.run(debug=True)