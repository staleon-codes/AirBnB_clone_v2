#!/usr/bin/python3
"""List of states on HTML states_list"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    from models import storage
    from models.state import State
    sorted_states_list = sorted(storage.all(State).values(), key=lambda x: x.name)
    return render_template("7-states_list.html", sorted_states_list=sorted_states_list)


if __name__ == '__main__':
    """start the server"""
    app.run(host='0.0.0.0', port=5000)
