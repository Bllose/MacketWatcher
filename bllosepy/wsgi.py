
from flask import Flask
from myOkx import myOkx

app = Flask(__name__)
m = myOkx()

@app.route("/")
def hello_world():
    return "<p> Hello World </p>"

@app.get("/volume")
def okx_volume_taker():
    m.volume_map = {}
    m.volume_taker()
    return m.volume_map

@app.get("/volume/continue")
def okx_volume_taker_continue():
    if not m.volume_map:
        return "还未初始化数据!"
    
    data_holded = m.volume_map
    return m.volume_taker(start = data_holded["BTC"]["max_time_stamp"])

@app.get("/env/<string:env>")
def okx_check(env):
    if env == 'pro':
        m = myOkx("pro")
        return "<p> CHECK TO PRO </p>"
    else :
        m = myOkx()
        return "<p> CHECK TO TEST </p>"



if __name__ == "__main__":
    app.run(host="localhost")