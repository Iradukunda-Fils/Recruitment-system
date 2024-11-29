// company javascript------------------------------------------------------------------------------



document.addEventListener('DOMContentLoaded', function() {
    const menuToggle = document.getElementById('menu-toggle');
    const sidebar = document.getElementById('sidebar');
    const spinner = document.getElementById('spinner');

    // Menu toggle functionality
    menuToggle.addEventListener('click', function() {
        sidebar.classList.toggle('show');
    });

    // Close sidebar when clicking outside on mobile
    document.addEventListener('click', function(event) {
        const isClickInside = sidebar.contains(event.target) || 
                            menuToggle.contains(event.target);
        
        if (!isClickInside && window.innerWidth <= 768 && 
            sidebar.classList.contains('show')) {
            sidebar.classList.remove('show');
        }
    });

    // Handle window resize
    window.addEventListener('resize', function() {
        if (window.innerWidth > 768) {
            sidebar.classList.remove('show');
        }
    });

    // Show spinner on page navigation
    document.addEventListener('click', function(event) {
        const link = event.target.closest('a');
        if (link && !link.hasAttribute('data-no-spinner') && 
            link.href && !link.href.includes('#')) {
            spinner.style.display = 'flex';
        }
    });

    // Form submission spinner
    document.querySelectorAll('form').forEach(form => {
        form.addEventListener('submit', function() {
            if (!this.hasAttribute('data-no-spinner')) {
                spinner.style.display = 'flex';
            }
        });
    });
});


// search javascript--------------------------------------------------------------------------------


document.addEventListener('DOMContentLoaded', function() {
    // Toggle filters
    const toggleFilters = document.getElementById('toggleFilters');
    const filtersRow = document.getElementById('filtersRow');
    
    toggleFilters.addEventListener('click', function() {
        filtersRow.classList.toggle('active');
        toggleFilters.classList.toggle('active');
    });

    // Animated card entrance
    const cards = document.querySelectorAll('.card');
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '20px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    cards.forEach(card => {
        observer.observe(card);
    });

    // Enhanced search interaction
    const searchInput = document.querySelector('.search-input');
    searchInput.addEventListener('focus', function() {
        this.parentElement.classList.add('focused');
    });

    searchInput.addEventListener('blur', function() {
        this.parentElement.classList.remove('focused');
    });
});
        