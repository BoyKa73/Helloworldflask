# Flask-Anwendung als App = Anwendung initialisieren
# app = Flask(import_name=__name__,
#             static_url_path="/static-content",
#             static_folder="my_static_content",
#             template_folder="my_templates")
app = Flask(__name__)

# Route definieren
@app.route('/api')
def hello_world():
    return 'Hello, World!'

# weitere Route definieren
@app.route('/willkommen')
def hello_fat():
    return "<h1>Hallo</h1>"

## TODO: Definiert eine Route auf den Pfad /25-01 mit einer Funktion, die "Hallo Kurs 25-01" zurückgibt
@app.route('/25-01')
def kurs():
    return "<p>Hallo Kurs 25-01</p>"

## Dies ist die Hundesalon-Seite
@app.route('/info')
def info():
    return "<h>Willkommen bei unserem supersmoothen Hundesalon!</h>"
## Dies ist die About-us Seite des Salons
@app.route('/about')
def about():
    return 'Dies ist eine Info-Seite über unseren Hunde-Salon.Hier findest Du Infos über uns.'


if __name__ == "__main__":
    app.run()
