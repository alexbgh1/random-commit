import json
import random
import requests
import subprocess
import sys

# obtener el número de commits a realizar
if len(sys.argv) < 2:
    print("Debe ingresar la cantidad de commits a realizar.")
    sys.exit(1)
try:
    num_commits = int(sys.argv[1])
except ValueError:
    print("Debe ingresar un número entero como argumento.")
    sys.exit(1)

if (num_commits < 0 or num_commits > 10):
    print("No te pasesxd")
    sys.exit(1)

url = "https://alexbgh1.github.io/cositas/data/data.json"

# Cargar las frases desde la URL
response = requests.get(url)
frases = json.loads(response.text)

# print frases img
print(random.choice( frases )["img"])

# generar los commits
for i in range(num_commits):
    # Elegir una frase al azar
    commit_msg = random.choice(frases)["img"]
    
    # hacer commit vacío con el mensaje elegido
    subprocess.run(["git", "commit", "--allow-empty", "-m", commit_msg])

# hacer push de los cambios al repositorio remoto
subprocess.run(["git", "push"])