import base64
import json
import os

import django
import requests
from django.template.loader import render_to_string
from django_rq import job

from сreating_check.settings import MEDIA_ROOT
from .models import Check

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE', 'сreating_check.settings'
)
django.setup()


@job
def pdf_generation(order_data, check_type):
    """Функція генерації PDF-файлу чека."""
    url = 'http://127.0.0.1:55000/'
    pdf_file_name = 'file.pdf'
    order_id = order_data.get('id')

    if check_type == 'kitchen_check':
        pdf_file_name = f'{order_id}_kitchen.pdf'
        html = render_to_string('kitchen_check.html', context=order_data)
        current_check = Check.objects.filter(
            order=order_data,
            type='kitchen'
        )
    elif check_type == 'client_check':
        pdf_file_name = f'{order_id}_client.pdf'
        html = render_to_string('client_check.html', context=order_data)
        current_check = Check.objects.filter(
            order=order_data,
            type='client'
        )
    else:
        html, current_check = None, None

    if html:
        html = base64.b64encode(bytes(html, 'utf-8'))
        data = json.dumps(
            {'contents': str(html)[2:-1]}
        )
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, data=data, headers=headers)

        with open(os.path.join(MEDIA_ROOT, 'pdf', pdf_file_name), 'wb') as f:
            f.write(response.content)

        current_check.update(
            pdf_file=os.path.join('pdf', pdf_file_name),
            status='rendered'
        )
