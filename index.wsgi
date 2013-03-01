import sae
from index import app
from about import app2

application = sae.create_wsgi_app(app)
application = sae.create_wsgi_app(app2)
