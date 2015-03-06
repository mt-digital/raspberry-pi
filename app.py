from flask import Flask, render_template

@route('/')
def index():
    """Show the buttons!"""

    return render_template('index.html', form=form)
