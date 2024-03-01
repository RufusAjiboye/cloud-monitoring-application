import psutil
from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
    cpu_percent = psutil.cpu_percent()
    mem_percent = psutil.virtual_memory().percent
    Message = None
    if cpu_percent > 80 or mem_percent > 80:
        Message = "High CPU or Memory Detected, scale up!!!"

    return render_template("index.html", cpu_percent=cpu_percent, mem_percent=mem_percent, message=Message)
    #f"CPU Utilization is: {cpu_percent} and memory utilization is: {mem_percent}"

if __name__== '__main__':
    app.run(debug=True, host = '0.0.0.0', port=9000)