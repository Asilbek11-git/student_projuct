"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_asgi_application()



iha strukturasi
student_portal/
|-- config/
| |-- settings.py
| `-- urls.py
|-- accounts/
| |-- models.py
| |-- forms.py
| |-- views.py
| `-- urls.py
|-- courses/
| |-- models.py
| |-- views.py
| `-- urls.py
|-- templates/
| |-- base.html
| |-- accounts/
| `-- courses/
`-- static/
`-- css/style.css