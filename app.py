from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def even_odd():

    if request.method == "POST":

        number = int(request.form["number"])

        if number % 2 == 0:
            return "Bu juft son"
        else:
            return "Bu toq son"

    return render_template("index.html")

app.run(debug=True)
