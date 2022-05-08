import os
from flask import Flask, render_template
from flask_assets import Environment, Bundle

app = Flask(__name__)
assets = Environment(app)

# create bundle for Flask-Assets to compile scass to css
css = Bundle('src/scss/main.scss',
             filters=['libsass'],
             output='dist/css/styles.css',
             depends='src/scss/*scss')

assets.register("asset_css", css)
css.build()

@app.route('/')
def index():
    name = "Christina"
    return render_template('base.html', name=name)
