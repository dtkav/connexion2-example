from connexion import FlaskApp

app = FlaskApp(__name__)
app.add_api("spec/openapi.yaml")

app.run()
