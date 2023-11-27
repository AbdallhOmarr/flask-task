from datetime import datetime
from flask import render_template, session, redirect, url_for, jsonify, request
from . import main
from database import queries
import numpy as np 
import pandas as pd 

@main.route('/', methods=['GET', 'POST'])
def index():
    results = queries.select_data_table('customer')
    return jsonify({"results": results})

## create customer endpoint

@main.route('/get_customer/', methods=['POST'])
def get_customer():
    customer_id = request.json.get('customer_id')

    if customer_id is None:
        return jsonify({"error": "Missing customer_id parameter"}), 400

    results = queries.select_data_table('customer', filters=[('id', customer_id)])
    return jsonify({"customer data": results})


@main.route('/add_customer/', methods=['POST'])
def add_customer():
    columns = request.json.get('columns')
    values = request.json.get('values')

    if columns is None or values is None:
        return jsonify({"error": "Missing columns or values parameter"}), 400

    table_name = 'customer'
    success = queries.add_data_table(table_name, columns, values)

    if success:
        return jsonify({"message": "Data added successfully"})
    else:
        return jsonify({"error": "Failed to add data"}), 500



@main.route('/update_customer/', methods=['POST'])
def update_customer():
    customer_id = request.json.get('customer_id')
    values = request.json.get('values')
    print(values)
    if customer_id is None or values is None:
        return jsonify({"error": "Missing customer_id or values parameter"}), 400

    results = queries.update_data_table('customer', filters=[('id', customer_id)], columns=values)
    
    return jsonify({"query result": results})


@main.route('/delete_customer/', methods=['POST'])
def delete_customer():
    customer_id = request.json.get('customer_id')

    if customer_id is None:
        return jsonify({"error": "Missing customer_id parameter"}), 400

    results = queries.delete_data_table('customer', customer_id)
    return jsonify({"query result": results})


## customer inquiry for booking a car 

@main.route('/inquiry/',methods=['POST'])
def customer_inquiry():
    # get vehicle type 
    vehicle_type = request.json.get('vehicle_type')
    # check available cars in database 
    all_vehicles = queries.select_data_table('vehicle',filters=[("type",vehicle_type)])
    
    ### check if vehicles id are in booking table 
    # get booking table 
    booking = queries.select_data_table('booking')
    booking_df = pd.DataFrame(booking)
    #loop on all_vehicles and if a vehicle not in booking table then select it as available car return its id 
    for vehicle in all_vehicles:
        if vehicle['id'] in list(booking_df['vehicle_id']):
            print(f"vehicle {vehicle['id']} is booked")
        else:
            return jsonify({"vehicle_id":vehicle['id']})
        
    return jsonify({"vehicle_id": None})


## record customer data if there's car available using add customers


## create the booking 

