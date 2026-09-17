document.addEventListener('DOMContentLoaded', function () {

    // ==================== SCROLL ANIMATIONS ====================
    const observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

    document.querySelectorAll('.fade-up, .fade-left, .fade-right').forEach(function (el) {
        observer.observe(el);
    });

    // ==================== NAVBAR SCROLL EFFECT ====================
    var navbar = document.querySelector('.navbar-nova');
    if (navbar) {
        function handleScroll() {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        }
        handleScroll();
        window.addEventListener('scroll', handleScroll, { passive: true });
    }

    // ==================== SMOOTH SCROLL FOR ANCHOR LINKS ====================
    document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
        anchor.addEventListener('click', function (e) {
            var target = document.querySelector(this.getAttribute('href'));
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

    // ==================== QUESTIONNAIRE LOGIC ====================
    var surgeryCheck = document.getElementById('id_had_surgery');
    var surgeryDateGroup = document.getElementById('surgery-date-group');
    if (surgeryCheck && surgeryDateGroup) {
        function toggleSurgeryDate() {
            surgeryDateGroup.style.display = surgeryCheck.checked ? 'block' : 'none';
        }
        toggleSurgeryDate();
        surgeryCheck.addEventListener('change', toggleSurgeryDate);
    }

    var ptStatus = document.getElementById('id_pt_status');
    var facilityGroup = document.getElementById('facility-group');
    if (ptStatus && facilityGroup) {
        function toggleFacility() {
            var show = ptStatus.value === 'currently_in' || ptStatus.value === 'completed';
            facilityGroup.style.display = show ? 'block' : 'none';
        }
        toggleFacility();
        ptStatus.addEventListener('change', toggleFacility);
    }

    // ==================== PAIN SLIDERS ====================
    var painSlider = document.getElementById('id_pain_level');
    var painValue = document.getElementById('pain-value');
    if (painSlider && painValue) {
        painValue.textContent = painSlider.value;
        painSlider.addEventListener('input', function () {
            painValue.textContent = this.value;
        });
    }

    var filterPain = document.getElementById('filter-pain');
    var filterPainValue = document.getElementById('filter-pain-value');
    if (filterPain && filterPainValue) {
        filterPainValue.textContent = filterPain.value;
        filterPain.addEventListener('input', function () {
            filterPainValue.textContent = this.value;
        });
    }

    // ==================== COUNTER ANIMATION ====================
    document.querySelectorAll('[data-count]').forEach(function (el) {
        var target = parseInt(el.getAttribute('data-count'), 10);
        var counted = false;
        var counterObserver = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting && !counted) {
                    counted = true;
                    var current = 0;
                    var step = Math.max(1, Math.floor(target / 40));
                    var timer = setInterval(function () {
                        current += step;
                        if (current >= target) {
                            current = target;
                            clearInterval(timer);
                        }
                        el.textContent = current.toLocaleString() + (el.getAttribute('data-suffix') || '');
                    }, 30);
                    counterObserver.unobserve(el);
                }
            });
        }, { threshold: 0.5 });
        counterObserver.observe(el);
    });
});
