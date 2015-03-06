from flask import Flask, request, render_template
#from flask_wtf import Form, SubmitField

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<led_idx>', methods=['GET', 'POST'])
def toggle_led(led_idx):
    """Show the buttons!"""

    #if not request.json or 'ledIdx' not in request.json:
        #led_idx = None
    #else:
        #led_idx = request.json['ledIdx']
    #if led_idx:

    return render_template('index.html', led_idx=led_idx)

def _toggle_led(led_idx):
    pass

#class LEDButtonsForm(Form):
    #"""Buttons to make the LEDs light up!
    #"""

    #b1 = SubmitField('LED 1')
    #b2 = SubmitField('LED 2')
    #b3 = SubmitField('LED 3')



if __name__ == '__main__':
    app.run(debug=True, port=8000)
