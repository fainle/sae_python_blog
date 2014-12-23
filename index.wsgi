import sae
from webapp import app

application = sae.create_wsgi_app(app)