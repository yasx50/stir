from flask import Flask, render_template, jsonify, request
from model import TrendData
from dbConnection import connectDB
from login import login
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import datetime
import time
from trending import getdata

app = Flask(__name__)

chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")  # Disable sandbox
chrome_options.add_argument("--disable-dev-shm-usage")  # Prevent shared memory issues
chrome_options.add_argument("--disable-gpu")  # Disable GPU

def mainScript():
    service = Service(ChromeDriverManager().install())
    
    driver = webdriver.Chrome(options=chrome_options)

    login(driver)
    getdata(driver)  
    
    driver.quit()  

def run_script():
    mainScript()
    latest_trend = TrendData.objects.order_by('-end_time').first()

    if latest_trend:
        return {
            "trend1": latest_trend.trend1,
            "trend2": latest_trend.trend2,
            "trend3": latest_trend.trend3,
            "trend4": latest_trend.trend4,
            "trend5": latest_trend.trend5,
            "end_time": latest_trend.end_time.strftime('%Y-%m-%d %H:%M:%S'),
            "ip_address": latest_trend.ip_address,
            "unique_id": latest_trend.unique_id
        }
    return {"message": "No data found"}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_script', methods=['POST'])
def run_script_endpoint():

    data = run_script()
    return jsonify(data)

@app.route('/run_again', methods=['POST'])
def run_again_endpoint():
    
    data = run_script()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
