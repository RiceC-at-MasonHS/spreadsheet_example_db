from flask import Flask, render_template
import requests
import csv
import io

app = Flask(__name__)

# Google Sheets CSV export URL - This is allowed for 'public' download
CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTOJSjMWjpTEpNjEcTGwpo_t6gREpp_6tXQhsif1LXgR8tNWVfll7sUYQPS4tNowJLLMhSUzkF093LG/pub?gid=1999930924&single=true&output=csv"
DOWNLOAD_ONCE = requests.get(CSV_URL)

def get_coffee_data():
    response = DOWNLOAD_ONCE
    response.encoding = 'utf-8'
    # Use DictReader to handle headers automatically
    reader = csv.DictReader(io.StringIO(response.text))
    return list(reader)

@app.route('/')
def index():
    try:
        items = get_coffee_data()
        return render_template('index.html', items=items, CSV_URL=CSV_URL)
    except Exception as e:
        return f"Error loading menu: {e}"

if __name__ == '__main__':
    app.run(debug=True)