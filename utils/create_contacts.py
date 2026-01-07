import os
import sys
from datetime import datetime
from pathlib import Path
from random import choice

import django
from django.conf import settings

DJANGO_BASE_DIR = Path(__file__).parent.parent
NUMBER_OF_OBJECTS = 50

sys.path.append(str(DJANGO_BASE_DIR))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
settings.USE_TZ = False

django.setup()

if __name__ == '__main__':
    import faker

    from contact.models import Category, Contact

    Contact.objects.all().delete()
    Category.objects.all().delete()

    fake = faker.Faker('pt_BR')
    categories = ['Family', 'Friends', 'Work', 'Others']

    django_categories = [Category(name=name) for name in categories]

    for category in django_categories:
        category.save()

    django_contacts = []

    for _ in range(NUMBER_OF_OBJECTS):
        profile = fake.profile()
        email = profile['mail']
        first_name, last_name = str(profile['name']).split(' ', 1)
        callsign = last_name.upper()
        saram = str(fake.random_number(digits=7, fix_len=True))
        phone = fake.phone_number()
        message = fake.text(max_nb_chars=200)
        description = fake.text(max_nb_chars=100)
        category = choice(django_categories)

        contact = Contact(
            first_name=first_name,
            last_name=last_name,
            callsign=callsign,
            saram=saram,
            phone=phone,
            email=email,
            message=message,
            description=description,
            category=category
        )
        django_contacts.append(contact)
    if len(django_contacts) > 10:
        Contact.objects.bulk_create(django_contacts)