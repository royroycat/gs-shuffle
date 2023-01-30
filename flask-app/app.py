from flask import Flask
from flask import send_from_directory
import gspread
import json

app = Flask(__name__)
gc = gspread.service_account()
spreadsheet_file = gc.open("gs-shuffle")
sheet = spreadsheet_file.sheet1

@app.route("/")
def index():
    return send_from_directory('static','index.html')

@app.route("/category")
def get_all_category():
    all_category = sheet.row_values(1)
    this_dict = {"category":all_category}
    return json.dumps(this_dict)

@app.route("/category/<string:category>")
def get_candidate(category):
    all_category = sheet.row_values(1)
    try:
        index = all_category.index(category)
    except ValueError:
        return {"error": "cannot find this category in spreadsheet"}
    all_candidate = sheet.col_values(index+1)
    all_candidate.pop(0) # remove the head row which is category title
    this_dict = {"candidate":all_candidate}
    return json.dumps(this_dict) 