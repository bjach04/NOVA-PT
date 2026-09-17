from django.core.management.base import BaseCommand
from accounts.models import Diagnosis


class Command(BaseCommand):
    help = 'Seed the database with common PT diagnoses'

    def handle(self, *args, **options):
        diagnoses = [
            {'name': 'ACL Tear / Reconstruction', 'slug': 'acl-tear', 'body_region': 'Knee'},
            {'name': 'Rotator Cuff Injury', 'slug': 'rotator-cuff', 'body_region': 'Shoulder'},
            {'name': 'Lower Back Pain', 'slug': 'lower-back-pain', 'body_region': 'Back'},
            {'name': 'Ankle Sprain', 'slug': 'ankle-sprain', 'body_region': 'Ankle'},
            {'name': 'Tennis Elbow', 'slug': 'tennis-elbow', 'body_region': 'Elbow'},
            {'name': 'Hip Replacement', 'slug': 'hip-replacement', 'body_region': 'Hip'},
            {'name': 'Meniscus Tear', 'slug': 'meniscus-tear', 'body_region': 'Knee'},
            {'name': 'Frozen Shoulder', 'slug': 'frozen-shoulder', 'body_region': 'Shoulder'},
            {'name': 'Plantar Fasciitis', 'slug': 'plantar-fasciitis', 'body_region': 'Foot'},
            {'name': 'Carpal Tunnel Syndrome', 'slug': 'carpal-tunnel', 'body_region': 'Wrist'},
        ]

        created = 0
        for d in diagnoses:
            _, was_created = Diagnosis.objects.get_or_create(
                slug=d['slug'],
                defaults={'name': d['name'], 'body_region': d['body_region']},
            )
            if was_created:
                created += 1

        self.stdout.write(self.style.SUCCESS(f'Seeded {created} diagnoses ({len(diagnoses) - created} already existed)'))
