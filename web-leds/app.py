from flask import Flask, request, render_template, jsonify
#from flask_wtf import Form, SubmitField

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<led_idx>', methods=['GET', 'POST'])
def toggle_led(led_idx):
    """Show the buttons!"""

    print (request.data)
    print(led_idx)

    _toggle_led(led_idx)

    return jsonify(hello="world")

def _toggle_led(led_idx):
    print("not really toggling " + led_idx)

#class LEDButtonsForm(Form):
    #"""Buttons to make the LEDs light up!
    #"""

    #b1 = SubmitField('LED 1')
    #b2 = SubmitField('LED 2')
    #b3 = SubmitField('LED 3')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=2000)
