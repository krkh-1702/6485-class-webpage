# Import Flask

from flask import Flask, render_template, redirect, url_for

webpage = Flask(__name__)


@webpage.route('/')
def index():
    return render_template('index.html')


@webpage.route('/project')
def project():
    return render_template('project.html')


@webpage.route('/emotion_augmenter')
def emotion_augmenter():
    return render_template('emotionAugmenter.html')

@webpage.route('/food')
def food():
    return render_template('food.html')

@webpage.route('/ui')
def ui():
    return render_template('ui.html')

@webpage.route('/styliart')
def styliart():
    return render_template('styliart.html')

@webpage.route('/urban')
def urban():
    return render_template('urban.html')

@webpage.route('/carbon')
def carbon():
    return render_template('carbon.html')

@webpage.route('/kinder')
def kinder():
    return render_template('kinder.html')

@webpage.route('/female')
def female():
    return render_template('female.html')

@webpage.route('/horse')
def horse():
    return render_template('horse.html')