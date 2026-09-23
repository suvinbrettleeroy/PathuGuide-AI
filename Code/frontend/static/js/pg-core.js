/* ==========================================================================
   PathGuide — shared motion & interactions (every body.pg-ui page)
   Page transitions, scroll reveals, counters, parallax, custom cursor,
   magnetic buttons, 3D tilt, spotlight, scrollspy and small UI helpers.
   Everything degrades to the plain page when motion is reduced or JS fails.
   ========================================================================== */
(function () {
    'use strict';

    const root = document.documentElement;
    const cfg = window.PG_UI || {};
    const motionOK = !window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const finePointer = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
    const introDelay = root.classList.contains('pg-seen') ? 450 : 1500;

    const $ = (sel, ctx = document) => ctx.querySelector(sel);
    const $$ = (sel, ctx = document) => Array.from(ctx.querySelectorAll(sel));

    function toast(message, ok = true) {
        if (typeof window.showLocationToast === 'function') {
            window.showLocationToast(message, ok);
        }
    }

    /* ------------------------------------------------------------------
       Page transitions
       ------------------------------------------------------------------ */
    let leaving = false;

    function navigate(url, pending) {
        if (leaving) return;
        leaving = true;
        const waitForPending = Promise.resolve(pending).catch(() => {});

        if (!motionOK) {
            waitForPending.then(() => { window.location.href = url; });
            return;
        }

        root.classList.add('pg-leaving');
        const curtain = new Promise((resolve) => setTimeout(resolve, 540));
        Promise.all([curtain, waitForPending]).then(() => { window.location.href = url; });

        // If the navigation never happens (offline, cancelled), give the page back.
        setTimeout(() => {
            root.classList.remove('pg-leaving');
            leaving = false;
        }, 8000);
    }

    window.pgNavigate = navigate;

    window.addEventListener('pageshow', (event) => {
        if (event.persisted) {
            root.classList.remove('pg-leaving');
            leaving = false;
        }
    });

    // Play the exit curtain while base.html switches language and reloads.
    if (typeof window.setLanguage === 'function') {
        const baseSetLanguage = window.setLanguage;
        window.setLanguage = function (lang) {
            if (lang === cfg.lang) return;
            if (motionOK) {
                root.classList.add('pg-leaving');
                setTimeout(() => root.classList.remove('pg-leaving'), 6000);
            }
            baseSetLanguage(lang);
        };
    }

    const navMenu = $('#pgNavMenu');
    if (navMenu) {
        navMenu.addEventListener('show.bs.collapse', () => $('#pgNav').classList.add('is-open'));
        navMenu.addEventListener('hidden.bs.collapse', () => $('#pgNav').classList.remove('is-open'));
    }

    function closeMobileMenu() {
        if (navMenu && navMenu.classList.contains('show') && window.bootstrap) {
            window.bootstrap.Collapse.getOrCreateInstance(navMenu).hide();
        }
    }

    // Ctrl + Alt + A opens the admin login (advertised on the login page).
    document.addEventListener('keydown', (event) => {
        if (!(event.ctrlKey && event.altKey && event.code === 'KeyA')) return;
        if (event.target.closest('input, textarea, select, [contenteditable="true"]')) return;
        if (window.location.pathname === '/admin-login') return;
        event.preventDefault();
        navigate('/admin-login');
    });

    // Capture phase so links that stop propagation still get the transition.
    document.addEventListener('click', (event) => {
        if (event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;

        const pathTrigger = event.target.closest('[data-path]');
        if (pathTrigger && typeof window.selectPath === 'function') {
            event.preventDefault();
            closeMobileMenu();
            window.selectPath(pathTrigger.dataset.path);
            return;
        }

        const link = event.target.closest('a[href]');
        if (!link || link.target === '_blank' || link.hasAttribute('download') || link.hasAttribute('data-bs-toggle')) return;

        const url = new URL(link.getAttribute('href'), window.location.href);
        if (url.origin !== window.location.origin) return;

        const samePage = url.pathname === window.location.pathname && url.search === window.location.search;
        if (samePage && url.hash) {
            closeMobileMenu();
            return; // in-page anchor: CSS smooth scroll handles it
        }

        event.preventDefault();
        if (samePage) {
            closeMobileMenu();
            window.scrollTo({ top: 0, behavior: motionOK ? 'smooth' : 'auto' });
            return;
        }
        navigate(url.href);
    }, true);

    /* ------------------------------------------------------------------
       Hero intro clean-up + counters
       ------------------------------------------------------------------ */
    $$('.pg-intro').forEach((el) => {
        el.addEventListener('animationend', (event) => {
            if (event.animationName === 'pgRise') el.classList.remove('pg-intro');
        });
    });

    function runCounter(el) {
        const target = parseFloat(el.dataset.count) || 0;
        const suffix = el.dataset.suffix || '';
        const duration = 1700;
        const start = performance.now();

        function frame(now) {
            const t = Math.min(1, (now - start) / duration);
            const eased = 1 - Math.pow(1 - t, 4);
            el.textContent = Math.round(target * eased) + suffix;
            if (t < 1) requestAnimationFrame(frame);
        }
        requestAnimationFrame(frame);
    }

    if (motionOK) {
        const counters = $$('[data-count]');
        counters.forEach((el) => { el.textContent = '0' + (el.dataset.suffix || ''); });
        setTimeout(() => counters.forEach(runCounter), introDelay);
    }


    /* ------------------------------------------------------------------
       Scroll reveal
       ------------------------------------------------------------------ */
    const revealEls = $$('[data-reveal]');
    revealEls.forEach((el) => {
        if (el.dataset.delay) el.style.setProperty('--rd', el.dataset.delay);
    });

    if (motionOK && 'IntersectionObserver' in window) {
        const revealObserver = new IntersectionObserver((entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('is-in');
                    revealObserver.unobserve(entry.target);
                }
            });
        }, { rootMargin: '0px 0px -8% 0px', threshold: 0.12 });
        // Start once the intro curtain has lifted, so above-the-fold reveals are seen.
        setTimeout(() => revealEls.forEach((el) => revealObserver.observe(el)), Math.max(0, introDelay - 350));
    } else {
        revealEls.forEach((el) => el.classList.add('is-in'));
    }

    /* ------------------------------------------------------------------
       Navbar: scrolled state, hide on scroll down, scrollspy bar
       ------------------------------------------------------------------ */
    const nav = $('#pgNav');
    const progressBar = $('.pg-progress span');
    const topBtn = $('#pgTop');
    const topRing = topBtn ? $('circle', topBtn) : null;
    const spyLinks = $$('.pg-link[data-spy]');
    const allNavLinks = $$('.pg-link');
    const bar = $('.pg-links-bar');
    let activeSpy = 'top';
    let lastY = window.scrollY;
    let heroVisible = true;

    function moveBar(link) {
        if (!bar || !link || !link.offsetWidth) return;
        const style = getComputedStyle(link);
        const padL = parseFloat(style.paddingLeft) || 0;
        const padR = parseFloat(style.paddingRight) || 0;
        bar.style.setProperty('--bx', (link.offsetLeft + padL) + 'px');
        bar.style.setProperty('--bw', (link.offsetWidth - padL - padR) + 'px');
    }

    // Home tracks its sections; other pages keep the bar under their own link.
    const pageLink = $('.pg-link.is-active:not([data-spy])');

    function activeLink() {
        return spyLinks.find((link) => link.dataset.spy === activeSpy) || pageLink;
    }

    allNavLinks.forEach((link) => link.addEventListener('mouseenter', () => moveBar(link)));
    if (bar) bar.parentElement.addEventListener('mouseleave', () => moveBar(activeLink()));

    function updateSpy() {
        if (!spyLinks.length) return;
        const vh = window.innerHeight;
        let current = 'top';
        ['features', 'about'].forEach((id) => {
            const section = document.getElementById(id);
            if (section && section.getBoundingClientRect().top < vh * 0.45) current = id;
        });
        if (window.innerHeight + window.scrollY >= root.scrollHeight - 4) current = 'about';

        if (current !== activeSpy) {
            activeSpy = current;
            spyLinks.forEach((link) => link.classList.toggle('is-active', link.dataset.spy === current));
            moveBar(activeLink());
        }
    }

    if (nav) nav.addEventListener('focusin', () => nav.classList.remove('is-hidden'));

    if (topBtn) {
        topBtn.addEventListener('click', () => window.scrollTo({ top: 0, behavior: motionOK ? 'smooth' : 'auto' }));
    }

    /* ------------------------------------------------------------------
       Scroll parallax (leaves, decorations, banner images)
       ------------------------------------------------------------------ */
    const parallaxItems = motionOK
        ? $$('[data-parallax]').map((el) => ({ el, host: el.parentElement, speed: parseFloat(el.dataset.parallax) || 0 }))
        : [];

    function updateParallax() {
        const vh = window.innerHeight;
        const offsets = parallaxItems.map((item) => {
            const rect = item.host.getBoundingClientRect();
            if (rect.bottom < -200 || rect.top > vh + 200) return null;
            return (rect.top + rect.height / 2 - vh / 2) * item.speed;
        });
        parallaxItems.forEach((item, i) => {
            if (offsets[i] !== null) item.el.style.translate = `0 ${offsets[i].toFixed(1)}px`;
        });
    }

    let scrollTicking = false;

    function onScrollFrame() {
        scrollTicking = false;
        const y = window.scrollY;
        const max = root.scrollHeight - window.innerHeight;
        const progress = max > 0 ? Math.min(1, y / max) : 0;

        if (progressBar) progressBar.style.transform = `scaleX(${progress.toFixed(4)})`;
        if (topRing) topRing.style.strokeDashoffset = String(100 - progress * 100);
        if (topBtn) topBtn.classList.toggle('is-visible', y > 600);

        if (nav) {
            nav.classList.toggle('is-scrolled', y > 16);
            const menuOpen = $('.pg-nav-menu.show', nav) || $('.dropdown-menu.show', nav);
            if (y > 420 && y > lastY + 6 && !menuOpen) nav.classList.add('is-hidden');
            else if (y < lastY - 6 || y <= 420) nav.classList.remove('is-hidden');
        }
        lastY = y;

        updateSpy();
        updateParallax();
        heroVisible = y < window.innerHeight;
    }

    function onScroll() {
        if (!scrollTicking) {
            scrollTicking = true;
            requestAnimationFrame(onScrollFrame);
        }
    }

    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', () => { moveBar(activeLink()); onScroll(); });
    window.addEventListener('load', () => moveBar(activeLink()));
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(() => moveBar(activeLink()));

    /* ------------------------------------------------------------------
       Pointer: custom cursor, aurora follower, hero depth, magnetic, tilt
       ------------------------------------------------------------------ */
    const depthItems = (motionOK && finePointer)
        ? $$('[data-depth]').map((el) => ({ el, depth: parseFloat(el.dataset.depth) || 0 }))
        : [];

    const cursorOn = motionOK && finePointer;
    const dot = $('.pg-cursor-dot');
    const ring = $('.pg-cursor-ring');
    const cursorLabel = $('.pg-cursor-label');
    const follower = $('.pg-aurora .follow');

    let px = -200, py = -200;          // pointer
    let rx = -200, ry = -200;          // lagging ring
    let fx = -400, fy = -400;          // aurora follower
    let mx = 0, my = 0, tmx = 0, tmy = 0; // hero depth (-1..1)
    let rafId = 0;

    function pointerFrame() {
        rafId = 0;
        let busy = false;

        rx += (px - rx) * 0.2;
        ry += (py - ry) * 0.2;
        fx += (px - fx) * 0.06;
        fy += (py - fy) * 0.06;
        mx += (tmx - mx) * 0.08;
        my += (tmy - my) * 0.08;

        if (ring) ring.style.translate = `${rx.toFixed(1)}px ${ry.toFixed(1)}px`;
        if (follower) follower.style.translate = `${fx.toFixed(1)}px ${fy.toFixed(1)}px`;

        if (heroVisible) {
            depthItems.forEach((item) => {
                item.el.style.translate = `${(mx * item.depth).toFixed(2)}px ${(my * item.depth).toFixed(2)}px`;
            });
        }

        if (Math.abs(px - rx) > 0.2 || Math.abs(py - ry) > 0.2 || Math.abs(px - fx) > 0.5 ||
            Math.abs(tmx - mx) > 0.002 || Math.abs(tmy - my) > 0.002) {
            busy = true;
        }
        if (busy) rafId = requestAnimationFrame(pointerFrame);
    }

    function wakePointerLoop() {
        if (!rafId) rafId = requestAnimationFrame(pointerFrame);
    }

    if (cursorOn) {
        root.classList.add('pg-cursor-on', 'pg-cursor-out');

        document.addEventListener('pointermove', (event) => {
            if (event.pointerType !== 'mouse') return;
            px = event.clientX;
            py = event.clientY;
            tmx = (px / window.innerWidth - 0.5) * 2;
            tmy = (py / window.innerHeight - 0.5) * 2;
            if (dot) dot.style.translate = `${px}px ${py}px`;
            root.classList.add('pg-pointer');
            root.classList.remove('pg-cursor-out');

            const target = event.target;
            const textField = target.closest('input, textarea, [contenteditable="true"]');
            const interactive = target.closest('a, button, [role="button"], label, .dropdown-item, .form-check-input');
            const labelHost = target.closest('[data-cursor-text]');
            const showLabel = !!labelHost && (!interactive || interactive === labelHost || !labelHost.contains(interactive));

            root.classList.toggle('pg-cursor-text', !!textField);
            root.classList.toggle('pg-cursor-labeled', showLabel);
            root.classList.toggle('pg-cursor-hover', !showLabel && !!interactive);
            if (showLabel && cursorLabel) cursorLabel.textContent = labelHost.dataset.cursorText;

            wakePointerLoop();
        }, { passive: true });

        document.addEventListener('pointerdown', () => root.classList.add('pg-cursor-down'));
        document.addEventListener('pointerup', () => root.classList.remove('pg-cursor-down'));
        document.addEventListener('mouseout', (event) => {
            if (!event.relatedTarget) root.classList.add('pg-cursor-out');
        });
    }

    if (motionOK && finePointer) {
        $$('[data-magnetic]').forEach((el) => {
            el.addEventListener('pointermove', (event) => {
                const rect = el.getBoundingClientRect();
                const dx = event.clientX - (rect.left + rect.width / 2);
                const dy = event.clientY - (rect.top + rect.height / 2);
                el.style.translate = `${(dx * 0.25).toFixed(1)}px ${(dy * 0.32).toFixed(1)}px`;
            });
            el.addEventListener('pointerleave', () => { el.style.translate = ''; });
        });

        $$('[data-tilt]').forEach((card) => {
            const max = card.classList.contains('pg-eco-card') ? 9 : 5;
            card.addEventListener('pointermove', (event) => {
                const rect = card.getBoundingClientRect();
                const x = (event.clientX - rect.left) / rect.width;
                const y = (event.clientY - rect.top) / rect.height;
                card.style.setProperty('--ry', ((x - 0.5) * max * 2).toFixed(2) + 'deg');
                card.style.setProperty('--rx', ((0.5 - y) * max * 2).toFixed(2) + 'deg');
                card.classList.add('is-tilting');
            });
            card.addEventListener('pointerleave', () => {
                card.style.setProperty('--rx', '0deg');
                card.style.setProperty('--ry', '0deg');
                card.classList.remove('is-tilting');
            });
        });
    }

    $$('[data-spotlight]').forEach((el) => {
        el.addEventListener('pointermove', (event) => {
            const rect = el.getBoundingClientRect();
            el.style.setProperty('--sx', (event.clientX - rect.left).toFixed(0) + 'px');
            el.style.setProperty('--sy', (event.clientY - rect.top).toFixed(0) + 'px');
        });
    });

    // Click ripple on primary buttons
    if (motionOK) {
        document.addEventListener('pointerdown', (event) => {
            const btn = event.target.closest('.pg-btn, .pg-search-btn, .pg-admin, .pg-newsletter-field button');
            if (!btn) return;
            const rect = btn.getBoundingClientRect();
            const ripple = document.createElement('span');
            ripple.className = 'pg-ripple';
            ripple.style.left = (event.clientX - rect.left) + 'px';
            ripple.style.top = (event.clientY - rect.top) + 'px';
            btn.appendChild(ripple);
            ripple.addEventListener('animationend', () => ripple.remove());
        });
    }

    /* ------------------------------------------------------------------
       Footer: newsletter, social, help modal focus
       ------------------------------------------------------------------ */
    const newsletter = $('#pgNewsletter');
    if (newsletter) {
        newsletter.addEventListener('submit', (event) => {
            event.preventDefault();
            const input = $('input', newsletter);
            const email = input.value.trim();
            newsletter.classList.remove('is-invalid');
            void newsletter.offsetWidth;
            if (!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email)) {
                newsletter.classList.add('is-invalid');
                input.focus();
                toast(cfg.newsletterInvalid, false);
                return;
            }
            toast(cfg.newsletterSoon, true);
            newsletter.reset();
        });
    }

    $$('[data-soon]').forEach((btn) => btn.addEventListener('click', () => toast(cfg.socialSoon, true)));

    const helpModal = $('#helpModal');
    if (helpModal) {
        helpModal.addEventListener('shown.bs.modal', (event) => {
            const trigger = event.relatedTarget;
            const focusId = trigger && trigger.dataset ? trigger.dataset.focus : '';
            const block = focusId ? document.getElementById(focusId) : null;
            if (!block) return;
            block.scrollIntoView({ block: 'nearest', behavior: motionOK ? 'smooth' : 'auto' });
            block.classList.add('is-flash');
            setTimeout(() => block.classList.remove('is-flash'), 1400);
        });
    }

    // First paint of scroll-driven state
    onScrollFrame();
    moveBar(activeLink());
})();
