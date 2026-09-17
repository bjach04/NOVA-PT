from django.shortcuts import render
from .models import Facility, InsuranceProvider


def facility_search(request):
    facilities = None
    zip_code = request.GET.get('zip', '').strip()
    insurance_slug = request.GET.get('insurance', '')

    if zip_code or insurance_slug:
        facilities = Facility.objects.prefetch_related('insurance_accepted').all()
        if zip_code:
            facilities = facilities.filter(zip_code=zip_code)
        if insurance_slug:
            facilities = facilities.filter(insurance_accepted__slug=insurance_slug)
        facilities = facilities.distinct()

    providers = InsuranceProvider.objects.all()

    return render(request, 'finder/search.html', {
        'facilities': facilities,
        'providers': providers,
        'zip_code': zip_code,
        'selected_insurance': insurance_slug,
    })
