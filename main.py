from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from calorie import Calorie
from temp import Temperature

app = Flask(__name__)

class HomePage(MethodView):
    def get(self):
        return render_template("index.html")


class CaloriesFormPage(MethodView):
    def get(self):
        calories_form = CaloriesForm()
        return render_template('calories_form_page.html', caloriesform=calories_form)

    def post(self):
        calories_form = CaloriesForm(request.form)

        temperature, time = Temperature(country=calories_form.country.data, city=calories_form.city.data).get()

        calorie = Calorie(weight=float(calories_form.weight.data), height=float(calories_form.height.data),
                          age=float(calories_form.age.data), temperature=temperature)

        calories = calorie.calculate()

        return render_template("calories_form_page.html", caloriesform=calories_form, calories=calories,
                               l_time=time, result=True)


class CaloriesForm(Form):
    weight = StringField("Weight: ", default=70)
    height = StringField("Height: ", default=175)
    age = StringField("Age: ", default=37)
    country = StringField("Country: ", default="USA")
    city = StringField("City: ", default="New York")
    button = SubmitField("Calculate")


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/calories_form', view_func=CaloriesFormPage.as_view('calories_form_page'))
app.run(debug=True)