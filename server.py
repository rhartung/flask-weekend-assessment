from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined


app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


@app.route("/")
def go_home():
    """Returns home page"""

    return render_template("index.html")


@app.route("/application-form")
def apply():
    """Page to apply to work at RobynCorp"""

    return render_template("application-form.html")


@app.route("/application-success", methods=["POST"])
def submit_application():
    """Confirmation page for user's application submission"""

    first_name = request.form["firstname"]
    last_name = request.form["lastname"]
    job = request.form["job"]
    salary = float(request.form["salary"])

    return render_template("application-response.html",
                        firstname=first_name,
                        lastname=last_name,
                        job=job,
                        salary=salary)



# YOUR ROUTES GO HERE


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
