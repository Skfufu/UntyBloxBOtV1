from flask import Flask, render_template, request, redirect, url_for
import os
import sys
import subprocess
import signal
import logging


app = Flask(__name__)
bot_process = None

def get_main_path():
    return os.path.join(os.path.dirname(__file__), "main.py")

def start_bot():
    global bot_process
    if bot_process and bot_process.poll() is None:
        return
    script = get_main_path()
    if os.name == "nt":
        # Nouveau groupe de processus pour pouvoir envoyer Ctrl-Break
        bot_process = subprocess.Popen([sys.executable, script], creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
    else:
        # Nouveau session id pour pouvoir tuer le groupe sur Unix
        bot_process = subprocess.Popen([sys.executable, script], preexec_fn=os.setsid)

def stop_bot(timeout=5):
    global bot_process
    if not bot_process or bot_process.poll() is not None:
        bot_process = None
        return
    try:
        if os.name == "nt":
            # Envoie un CTRL_BREAK_EVENT à la console du processus (équivalent d'un "graceful" interrupt)
            bot_process.send_signal(signal.CTRL_BREAK_EVENT)
        else:
            # Envoie SIGINT au groupe de processus
            os.killpg(os.getpgid(bot_process.pid), signal.SIGINT)
        try:
            bot_process.wait(timeout=timeout)
        except subprocess.TimeoutExpired:
            # Si pas mort, demander terminaison puis kill si nécessaire
            bot_process.terminate()
            try:
                bot_process.wait(timeout=2)
            except subprocess.TimeoutExpired:
                bot_process.kill()
                bot_process.wait()
    finally:
        bot_process = None

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    action = request.form.get("action")
    if action == "start":
        start_bot()
    elif action == "stop":
        stop_bot()
    elif action == "restart":
        stop_bot()
        start_bot()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
