from flask import Flask, render_template

app = flask(__name__)

@app_route("/")
def incio_sesion():
    return render_template("index.html")

@app_route("/reg")
def recuperar_cuenta():
    return render_template("reg.html")

if __name__ == "__main__":
    app.run(debug=True)