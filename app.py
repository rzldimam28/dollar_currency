from flask import Flask, render_template, request
import requests as req

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
  if request.method == 'POST':
    frm = request.form['from']
    to = request.form['to']
    url = 'https://www.freeforexapi.com/api/live?pairs='
    flag_frm = frm[0:2].lower()
    flag_to = to[0:2].lower()
    res = req.get(f'{url}{frm}{to}')
    if 'rates' in res.json():
      response = res.json()["rates"][f"{frm}{to}"]["rate"]
    else:
      response = 'You are typing a wrong format currency:('
    return render_template('index.html', response=response, frm=frm, to=to, flag_frm=flag_frm, flag_to=flag_to)
  else:
    return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)