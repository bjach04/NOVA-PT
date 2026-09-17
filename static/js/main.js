document.addEventListener('DOMContentLoaded', function () {

    // Questionnaire: show/hide surgery date based on surgery checkbox
    const surgeryCheck = document.getElementById('id_had_surgery');
    const surgeryDateGroup = document.getElementById('surgery-date-group');
    if (surgeryCheck && surgeryDateGroup) {
        function toggleSurgeryDate() {
            surgeryDateGroup.style.display = surgeryCheck.checked ? 'block' : 'none';
        }
        toggleSurgeryDate();
        surgeryCheck.addEventListener('change', toggleSurgeryDate);
    }

    // Questionnaire: show/hide facility field based on PT status
    const ptStatus = document.getElementById('id_pt_status');
    const facilityGroup = document.getElementById('facility-group');
    if (ptStatus && facilityGroup) {
        function toggleFacility() {
            const show = ptStatus.value === 'currently_in' || ptStatus.value === 'completed';
            facilityGroup.style.display = show ? 'block' : 'none';
        }
        toggleFacility();
        ptStatus.addEventListener('change', toggleFacility);
    }

    // Pain level slider label
    const painSlider = document.getElementById('id_pain_level');
    const painValue = document.getElementById('pain-value');
    if (painSlider && painValue) {
        painValue.textContent = painSlider.value;
        painSlider.addEventListener('input', function () {
            painValue.textContent = this.value;
        });
    }

    // Exercise filter: pain level slider on exercise list
    const filterPain = document.getElementById('filter-pain');
    const filterPainValue = document.getElementById('filter-pain-value');
    if (filterPain && filterPainValue) {
        filterPainValue.textContent = filterPain.value;
        filterPain.addEventListener('input', function () {
            filterPainValue.textContent = this.value;
        });
    }
});
