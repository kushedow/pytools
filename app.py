from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cheatsheet/')
def show_cheatsheet():
    return render_template('cheatsheet.html')

@app.route('/map/')
def show_map():
    return render_template('map.html')

if __name__ == '__main__':
  app.run()

