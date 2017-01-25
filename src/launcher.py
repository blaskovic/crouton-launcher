from bottle import route, run, redirect
import os
import yaml

def load_config():
    home = os.path.expanduser('~')
    with open(home + "/.crouton.launcher.conf", 'r') as stream:
        try:
            data = yaml.load(stream)
            return data
        except yaml.YAMLError as exc:
            print(exc)

@route('/')
def index():
    out = '<h1>Crouton launcher</h1>'
    out += '<ul>'

    # Show commands from yaml:
    data = load_config()
    for key in data.keys():
        out += '<li><a href="run/'+key+'">'+data[key]['name']+'</a></li>'

    out += '</ul>'

    return out

@route('/run/<key>')
def xiwi(key):
    data = load_config()
    os.system(data[key]['cmd'] + ' & ')
    redirect('/')


run(host='localhost', port=8080, debug=True)
