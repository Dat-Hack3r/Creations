import ast
from flask import Flask, request, render_template, session, send_from_directory  
import logging
from map_generator import *
import os
import random
from screenshot import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

with open('users.txt') as f:
  users = ast.literal_eval(f.read())

nations = ['Yenianorth', 'Nestates Roonbra Territories', 'Ngothe', 'Dodenswe', 'Coconguilla', 'Nivirfrench', 'Western Reale Briwales', 'Ustswa', 'Eastern Viacogi', 'Grobai', 'New Ngagia Ilyi', 'Lapuama Republic']
landforms = ['in a plain', 'in a forest', 'on a hill', 'on a mountain', 'in a swamp', 'in a lake', 'in a valley', 'in a desert', 'on a plateau']
coastal_landforms = ['in the ocean', 'on an island']

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--window-size=1366,768")

driver = webdriver.Chrome(options=chrome_options)

app = Flask(__name__)
app.convert_url_to_file_name = False
app.config['DEBUG'] = True
app.config["SECRET_KEY"] = "&*Gbu8f7d$%f^&vksdfv}sf{sdf]\,df]42g3rfds"
logging.basicConfig(filename='app.log', format='%(asctime)s %(message)s', datefmt='[%Y-%m-%d | %H:%M:%S]', level=logging.DEBUG)

def clean(path):
    while True:
        if path[-1] == "/":
            path = path[:-1]
        else:
            break
    return path

def track():
  global users
  if request.headers['X-Replit-User-Id'] not in users:
    users.append(request.headers['X-Replit-User-Id'])
  with open('users.txt', 'w') as f:
    f.write(str(users))

@app.route('/favicon.ico')
def favicon():
  track()
  return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.png',mimetype='image/vnd.microsoft.icon')

@app.route('/', methods=['GET', 'POST'])
def index():
  track()
  try:
    with open('messages.txt', 'a') as messages:
      messages.write(f"{request.form['Subject']}\n{request.form['Name']} ({request.form['Email']}): {request.form['Message']}\n\n")
  except:
    pass
  all_maps = []
  for (dir_path, dir_names, file_names) in os.walk('maps/'):
    all_maps.extend(file_names)
  return render_template('index.html', user_id=request.headers['X-Replit-User-Id'], map_amount=len(all_maps), user_amount=len(users))

@app.route('/buy')
def bomb():
  track()
  return render_template('bomb.html')

@app.route('/api/<path:path>/<coord>', methods=['GET', 'POST'])
def get_coord(path, coord):
  track()
  if not os.path.exists('maps/' + clean(path)):
    os.makedirs(os.path.dirname('maps/' + clean(path)), exist_ok=True)
    with open('maps/' + clean(path), 'w+') as map_file:
      map_file.write(str(generate_map()))
  with open('maps/' + clean(path)) as map_file:
    if coord == 'map':
      return ast.literal_eval(map_file.read())
    else:
      coords = coord.split(',')
      if request.headers['X-Replit-User-Id']:
        try:
          return ast.literal_eval(map_file.read())[-1-int(coords[1])][int(coords[0])]
        except:
          return "error"
      else:
        return render_template('login.html')

@app.route('/<path:path>', methods=['GET', 'POST'])
def main(path):
  track()
  if 'location' not in session:
    session['location'] = {}
  if clean(path) not in session['location']:
    session['location'][clean(path)] = [0,0]
  if not os.path.exists('maps/' + clean(path)):
    os.makedirs(os.path.dirname('maps/' + clean(path)), exist_ok=True)
    with open('maps/' + clean(path), 'w') as map_file:
      map_file.write(str(generate_map()))
    with open('maps/' + clean(path)) as map_file:
      session['map'] = ast.literal_eval(map_file.read())
      session["map"][-1-session["location"][clean(path)][1]][session["location"][clean(path)][0]]["people"].append(request.headers['X-Replit-User-Name'])
  with open('maps/' + clean(path)) as map_file:
    session['map'] = ast.literal_eval(map_file.read())
    if request.method == 'POST':
      try:
        if request.form.getlist('submit-button') == ['North']:
          print(0)
          session["map"][-1-session["location"][clean(path)][1]][session["location"][clean(path)][0]]["people"].remove(request.headers['X-Replit-User-Name'])
          print(session['location'])
          session['location'][clean(path)] = [session['location'][clean(path)][0],session['location'][clean(path)][1]+1]
          print(session['location'])
          session["map"][-1-session["location"][clean(path)][1]][session["location"][clean(path)][0]]["people"].append(request.headers['X-Replit-User-Name'])
        elif request.form.getlist('submit-button') == ['East']:
          session["map"][-1-session["location"][clean(path)][1]][session["location"][clean(path)][0]]["people"].remove(request.headers['X-Replit-User-Name'])
          session['location'][clean(path)] = [session['location'][clean(path)][0]+1,session['location'][clean(path)][1]]
          session["map"][-1-session["location"][clean(path)][1]][session["location"][clean(path)][0]]["people"].append(request.headers['X-Replit-User-Name'])
        elif request.form.getlist('submit-button') == ['South']:
          session["map"][-1-session["location"][clean(path)][1]][session["location"][clean(path)][0]]["people"].remove(request.headers['X-Replit-User-Name'])
          session['location'][clean(path)] = [session['location'][clean(path)][0],session['location'][clean(path)][1]-1]
          session["map"][-1-session["location"][clean(path)][1]][session["location"][clean(path)][0]]["people"].append(request.headers['X-Replit-User-Name'])
        elif request.form.getlist('submit-button') == ['West']:
          session["map"][-1-session["location"][clean(path)][1]][session["location"][clean(path)][0]]["people"].remove(request.headers['X-Replit-User-Name'])
          session['location'][clean(path)] = [session['location'][clean(path)][0]-1,session['location'][clean(path)][1]]
          session["map"][-1-session["location"][clean(path)][1]][session["location"][clean(path)][0]]["people"].append(request.headers['X-Replit-User-Name'])
      except:
        pass
#    try:
    print('\n\n\n\n\n'+map_file+'\n\n\n\n\n')
    session['map'] = ast.literal_eval(map_file.read())
    session['location_info'] = f'You are in {session["map"][-1-session["location"][clean(path)][1]][session["location"][clean(path)][0]]["nation"]}, {str(session["map"][-1-session["location"][clean(path)][1]][session["location"][clean(path)][0]]["landform"])}, with {str(session["map"][-1-session["location"][clean(path)][1]][session["location"][clean(path)][0]]["people"])}.'
    return render_template('main.html', user_id=request.headers['X-Replit-User-Id'], location_info=session["location_info"])
#    except Exception as e:
#      return 'error'

app.run(host='0.0.0.0', port=81)