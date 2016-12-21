import os


from paste.deploy import loadapp
from waitress import serve

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5300))
    app = loadapp('config:poruction.ini', relative_to='.')

    serve(app, host='0.0.0.0', port=port)
