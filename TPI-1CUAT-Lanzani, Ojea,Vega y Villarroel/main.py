from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
  conn = sqlite3.connect("baseDeDatos.db")
  q = f"""SELECT * FROM Personas"""
  resu = conn.execute(q)
  topPuntajes = []
  for fila in resu:
    topPuntajes.append(fila)
  conn.close()
  return str(topPuntajes)

app.run(host='0.0.0.0', port=81)

#  conn=sqlite3.connect("baseDeDatos.db")
#  q=f"""INSERT INTO Personas (nombre, puntaje)  
#                VALUES ('Bruno', 100)
#  """