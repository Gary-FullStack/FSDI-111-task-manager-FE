from flask import Flask, render_template
from datetime import datetime
import requests

BACKEND_URL = "http:127.0.0.1:5000"
app = Flask(__name__)


@app.get("/")
def index():
    timestamp = datetime.now().strftime("%F %H:%M:%S")
    return render_template("index.html", server_time=timestamp)


@app.get("/tasks")
def show_tasks():
    url = "%s/tasks" % BACKEND_URL
    resp = requests.get(url)
    if resp.status_code == 200:
        task_list = resp.json().get("tasks")
        render_template("task_list.html", tasks=task_list)
    return render_template("error.html"), resp.status_code    