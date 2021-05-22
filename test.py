# import json
# import requests
# import json
# import requests
#
# from flask import Flask, request, Response
# from webargs import fields, validate
# from webargs.flaskparser import use_kwargs
#
# # from formatters import format_list
# # from utils import gen_password, fetch_bitcoin_rate
# # from parsers import parse_length, parse_chars, parse_currency, parse_str
# # from db import execute_query, get_customer_names
#
# app = Flask(__name__)
#
# from flask import jsonify
# # Return validation errors as JSON
# @app.errorhandler(422)
# @app.errorhandler(400)
# def handle_error(err):
#     headers = err.data.get("headers", None)
#     messages = err.data.get("messages", ["Invalid request."])
#     if headers:
#         return jsonify({"errors": messages}), err.code, headers
#     else:
#         return jsonify({"errors": messages}), err.code
#
#
# def fetch_bitcoin_rate(currency):
#     url = 'https://bitpay.com/api/rates'
#     response = requests.get(url=url)
#     rates = json.loads(response.text)
#     for rate in rates:
#         if rate['code'] == currency:
#             return str(rate['rate'])
#     return 'N/A'
#
#
# @app.route('/password')
# @use_kwargs({
#     "length": fields.Int(
#         required=True,
#         # missing=100,
#         validate=lambda x: 5 < x < 25
#     )},
#     location="query"
# )
# def get_random(length):
#
#     return '42'*length
#
#
#
# @app.route('/bitcoin')
# def get_bitcoin_rate():
#     return '42'
#     # try:
#     #     currency = parse_currency(request)
#     # except Exception as ex:
#     #     return Response(str(ex), status=400)
#     # return fetch_bitcoin_rate(currency)
#
#
# if __name__ == '__main__':
#     app.run(host='127.0.0.1', port=8003, debug=True)
import json

import csv
from faker import Faker
from flask import Flask, jsonify
from pprint import pprint as pp


app = Flask(__name__)

@app.route("/avr_data")
def get_avr_data():
    height_ls = []
    weight_ls = []

    with open("hw.csv", newline="") as csv_file:
        fieldnames = ["Student №", "Height(cm)", "Weight(kg)"]
        reader = csv.DictReader(csv_file, fieldnames=fieldnames)

        for row in reader:
            height_ls.append(row["Height(cm)"])
            weight_ls.append(row["Weight(kg)"])

        h_avr = sum(map(float, height_ls)) / len(height_ls)
        w_avr = sum(map(float, weight_ls)) / len(weight_ls)
    return "Average height of  25,000 students: " + str(h_avr) + " cm | " + "Average weight of  25,000 students: " + str(w_avr) + " kg"

@app.route("/requirements")
def get_requirements():
    with open("requirements.txt", newline="") as requirements:
        reader = requirements.read()
    return str(reader)

@app.route("/random_students")
def get_random_students():
    fake = Faker(['uk_UA'])
    fake_n = []
    result = {}
    for i in range(10):
        # fake_n.append(fake.name())
        result[fake.name()] = fake.phone_number()
    return json.dumps(result) #, ensure_ascii=False)
    # return '<br>'.join(fake_n)

pp(app.config)
print()
app.run(debug=True, port=5011)