from datetime import datetime

from flask_swagger_ui import get_swaggerui_blueprint

app = get_swaggerui_blueprint(base_url='/api-docs/frontend',
                              api_url='/static/documents/api.yaml?t={}'.format(
                                  datetime.utcnow().timestamp()),
                              blueprint_name='swagger-ui-frontend',
                              config={'app_name': "Application"})
