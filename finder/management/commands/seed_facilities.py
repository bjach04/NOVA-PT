from django.core.management.base import BaseCommand
from finder.models import InsuranceProvider, Facility


INSURANCE_PROVIDERS = [
    {'name': 'Aetna', 'slug': 'aetna'},
    {'name': 'Blue Cross Blue Shield', 'slug': 'bcbs'},
    {'name': 'Cigna', 'slug': 'cigna'},
    {'name': 'UnitedHealthcare', 'slug': 'uhc'},
    {'name': 'Humana', 'slug': 'humana'},
    {'name': 'Kaiser Permanente', 'slug': 'kaiser'},
    {'name': 'Anthem', 'slug': 'anthem'},
    {'name': 'Molina Healthcare', 'slug': 'molina'},
    {'name': 'Centene', 'slug': 'centene'},
    {'name': 'Medicare', 'slug': 'medicare'},
    {'name': 'Medicaid', 'slug': 'medicaid'},
    {'name': 'Tricare', 'slug': 'tricare'},
    {'name': 'Oxford Health Plans', 'slug': 'oxford'},
    {'name': 'Horizon BCBS', 'slug': 'horizon'},
    {'name': 'AmeriHealth', 'slug': 'amerihealth'},
]

FACILITIES = [
    {
        'name': 'NOVA Physical Therapy & Wellness',
        'address': '123 Main Street, Suite 200',
        'city': 'Arlington',
        'state': 'VA',
        'zip_code': '22201',
        'phone': '(703) 555-0101',
        'website': 'https://example.com/nova-pt',
        'insurance_slugs': ['aetna', 'bcbs', 'cigna', 'uhc', 'medicare'],
    },
    {
        'name': 'Peak Performance Physical Therapy',
        'address': '456 Oak Avenue',
        'city': 'Fairfax',
        'state': 'VA',
        'zip_code': '22030',
        'phone': '(703) 555-0202',
        'website': 'https://example.com/peak-pt',
        'insurance_slugs': ['bcbs', 'uhc', 'humana', 'anthem', 'medicare'],
    },
    {
        'name': 'Restore Rehab Center',
        'address': '789 Elm Street',
        'city': 'Alexandria',
        'state': 'VA',
        'zip_code': '22314',
        'phone': '(703) 555-0303',
        'website': 'https://example.com/restore',
        'insurance_slugs': ['aetna', 'cigna', 'kaiser', 'tricare', 'medicaid'],
    },
    {
        'name': 'Capital City Physical Therapy',
        'address': '321 Pennsylvania Ave NW',
        'city': 'Washington',
        'state': 'DC',
        'zip_code': '20004',
        'phone': '(202) 555-0404',
        'website': 'https://example.com/capital-pt',
        'insurance_slugs': ['bcbs', 'uhc', 'aetna', 'cigna', 'oxford'],
    },
    {
        'name': 'Bethesda Sports Medicine & PT',
        'address': '555 Wisconsin Ave',
        'city': 'Bethesda',
        'state': 'MD',
        'zip_code': '20814',
        'phone': '(301) 555-0505',
        'website': 'https://example.com/bethesda-sports',
        'insurance_slugs': ['bcbs', 'aetna', 'cigna', 'uhc', 'humana', 'medicare'],
    },
    {
        'name': 'Silver Spring Recovery Center',
        'address': '888 Georgia Ave',
        'city': 'Silver Spring',
        'state': 'MD',
        'zip_code': '20910',
        'phone': '(301) 555-0606',
        'website': '',
        'insurance_slugs': ['medicaid', 'medicare', 'molina', 'centene', 'amerihealth'],
    },
    {
        'name': 'Tysons Corner PT',
        'address': '1900 Tysons Blvd',
        'city': 'McLean',
        'state': 'VA',
        'zip_code': '22102',
        'phone': '(703) 555-0707',
        'website': 'https://example.com/tysons-pt',
        'insurance_slugs': ['aetna', 'bcbs', 'uhc', 'anthem', 'horizon'],
    },
    {
        'name': 'Columbia Physical Therapy',
        'address': '6100 Day Long Lane',
        'city': 'Columbia',
        'state': 'MD',
        'zip_code': '21045',
        'phone': '(410) 555-0808',
        'website': 'https://example.com/columbia-pt',
        'insurance_slugs': ['bcbs', 'cigna', 'uhc', 'kaiser', 'medicare'],
    },
    {
        'name': 'Reston Active Recovery',
        'address': '1800 Reston Pkwy',
        'city': 'Reston',
        'state': 'VA',
        'zip_code': '20190',
        'phone': '(703) 555-0909',
        'website': 'https://example.com/reston-ar',
        'insurance_slugs': ['aetna', 'anthem', 'humana', 'tricare', 'uhc'],
    },
    {
        'name': 'Rockville PT Associates',
        'address': '200 Monroe Street',
        'city': 'Rockville',
        'state': 'MD',
        'zip_code': '20850',
        'phone': '(301) 555-1010',
        'website': '',
        'insurance_slugs': ['bcbs', 'aetna', 'cigna', 'medicare', 'medicaid'],
    },
]


class Command(BaseCommand):
    help = 'Seed the database with insurance providers and PT facilities'

    def handle(self, *args, **options):
        # Seed insurance providers
        ins_created = 0
        providers = {}
        for p in INSURANCE_PROVIDERS:
            obj, was_created = InsuranceProvider.objects.get_or_create(
                slug=p['slug'],
                defaults={'name': p['name']},
            )
            providers[p['slug']] = obj
            if was_created:
                ins_created += 1

        # Seed facilities
        fac_created = 0
        for f in FACILITIES:
            slugs = f.pop('insurance_slugs')
            obj, was_created = Facility.objects.get_or_create(
                name=f['name'],
                zip_code=f['zip_code'],
                defaults=f,
            )
            if was_created:
                fac_created += 1
                for slug in slugs:
                    if slug in providers:
                        obj.insurance_accepted.add(providers[slug])

        self.stdout.write(self.style.SUCCESS(
            f'Seeded {ins_created} insurance providers, {fac_created} facilities'
        ))
