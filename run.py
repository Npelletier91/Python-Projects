from connexion import AsyncApp

app = AsyncApp(__name__)

def post_greeting(name: str):
    return f"Hello {name}", 200

app.add_api("example.yaml")