/* ==========================================================================
   PathGuide — Admin panel UI: theme, sidebar, search, counters, deep links.
   Page actions (showSection, toggleFeature, backups...) live in the template.
   ========================================================================== */
(function () {
    'use strict';

    const root = document.documentElement;
    const motionOK = !window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const $ = (sel, ctx = document) => ctx.querySelector(sel);
    const $$ = (sel, ctx = document) => Array.from(ctx.querySelectorAll(sel));

    /* ------------------------------------------------------------------
       Theme (light / dark)
       ------------------------------------------------------------------ */
    function applyTheme(theme) {
        root.setAttribute('data-theme', theme);
        $$('[data-theme-set]').forEach((btn) => btn.setAttribute('aria-pressed', btn.dataset.themeSet === theme ? 'true' : 'false'));
        try { localStorage.setItem('pgAdminTheme', theme); } catch (e) {}
        if (typeof window.renderCharts === 'function' && window.Chart) window.renderCharts();
    }

    $$('[data-theme-set]').forEach((btn) => {
        btn.addEventListener('click', () => applyTheme(btn.dataset.themeSet));
    });
    $$('[data-theme-set]').forEach((btn) => btn.setAttribute('aria-pressed', btn.dataset.themeSet === (root.getAttribute('data-theme') || 'light') ? 'true' : 'false'));
    if (root.getAttribute('data-theme') === 'dark' && typeof window.renderCharts === 'function' && window.Chart) window.renderCharts();

    /* ------------------------------------------------------------------
       Mobile sidebar
       ------------------------------------------------------------------ */
    const sidebar = $('#adminSidebar');
    const burger = $('#sidebarToggle');
    const backdrop = $('#sidebarBackdrop');

    function setSidebar(open) {
        root.classList.toggle('a-sidebar-open', open);
        if (burger) {
            burger.setAttribute('aria-expanded', open ? 'true' : 'false');
            burger.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
        }
        if (open) {
            const current = $('.nav-item.active', sidebar) || $('.nav-item', sidebar);
            if (current) current.focus();
        }
    }

    if (burger) burger.addEventListener('click', () => setSidebar(!root.classList.contains('a-sidebar-open')));
    if (backdrop) backdrop.addEventListener('click', () => setSidebar(false));
    document.addEventListener('keydown', (event) => {
        if (event.key === 'Escape' && root.classList.contains('a-sidebar-open')) {
            setSidebar(false);
            if (burger) burger.focus();
        }
    });

    /* ------------------------------------------------------------------
       Count-up numbers + section entrance
       ------------------------------------------------------------------ */
    const counted = new WeakSet();

    function countUp(el) {
        if (counted.has(el)) return;
        counted.add(el);
        const target = parseFloat(el.dataset.count);
        if (!motionOK || !isFinite(target)) return;
        const start = performance.now();
        const duration = 1300;
        const frame = (now) => {
            const t = Math.min(1, (now - start) / duration);
            el.textContent = Math.round(target * (1 - Math.pow(1 - t, 4)));
            if (t < 1) requestAnimationFrame(frame);
        };
        el.textContent = '0';
        requestAnimationFrame(frame);
    }

    function enterSection(section) {
        if (!section) return;
        section.classList.remove('is-entering');
        void section.offsetWidth;
        section.classList.add('is-entering');
        $$('[data-count]', section).forEach(countUp);
    }

    const content = $('#adminMain');

    window.pgAdminOnSection = function (sectionId) {
        const section = document.getElementById(sectionId);
        enterSection(section);
        setSidebar(false);
        if (content) window.scrollTo({ top: 0, behavior: motionOK ? 'smooth' : 'auto' });
        closeSearch();
    };

    /* ------------------------------------------------------------------
       Search (Ctrl + K): sections, cards and settings
       ------------------------------------------------------------------ */
    const searchInput = $('#adminSearch');
    const results = $('#adminSearchResults');
    const index = [];

    $$('.content-section').forEach((section) => {
        const sectionTitle = (section.querySelector('h1, h2') || {}).textContent || section.id;
        const cleanSection = sectionTitle.replace(/\s+/g, ' ').replace('👋', '').trim();
        index.push({ label: cleanSection, where: 'Section', section: section.id, el: null });
        $$('.a-card-head h4, .a-card-head h5, .feature-toggle strong, .a-metric p, .a-stat p, label.form-label', section).forEach((el) => {
            const label = el.textContent.replace(/\s+/g, ' ').trim();
            if (label && !index.some((item) => item.label === label && item.section === section.id)) {
                index.push({ label, where: cleanSection, section: section.id, el });
            }
        });
    });

    let activeIndex = -1;
    let matches = [];

    function closeSearch() {
        if (!results) return;
        results.hidden = true;
        searchInput && searchInput.setAttribute('aria-expanded', 'false');
        activeIndex = -1;
    }

    function escapeHtml(text) {
        return text.replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
    }

    function renderResults(query) {
        const q = query.trim().toLowerCase();
        if (!q) { closeSearch(); return; }
        matches = index.filter((item) => item.label.toLowerCase().includes(q) || item.where.toLowerCase().includes(q)).slice(0, 8);
        if (!matches.length) {
            results.innerHTML = '<div class="a-search-empty">No matches in the admin panel</div>';
        } else {
            results.innerHTML = matches.map((item, i) => `
                <button type="button" class="a-search-item" role="option" id="sr-${i}" data-i="${i}">
                    <i class="fas ${item.el ? 'fa-sliders' : 'fa-folder-open'}"></i>
                    <span><strong>${escapeHtml(item.label)}</strong><small>${escapeHtml(item.where)}</small></span>
                </button>`).join('');
        }
        results.hidden = false;
        searchInput.setAttribute('aria-expanded', 'true');
        activeIndex = -1;
    }

    function openMatch(item) {
        if (!item) return;
        window.showSection(item.section);
        searchInput.value = '';
        closeSearch();
        if (item.el) {
            const card = item.el.closest('.feature-toggle, .a-card, .a-metric, .a-stat') || item.el;
            setTimeout(() => {
                card.scrollIntoView({ block: 'center', behavior: motionOK ? 'smooth' : 'auto' });
                card.classList.remove('is-flash');
                void card.offsetWidth;
                card.classList.add('is-flash');
            }, 120);
        }
    }

    function highlight(i) {
        const items = $$('.a-search-item', results);
        items.forEach((el, n) => el.classList.toggle('is-active', n === i));
        if (items[i]) searchInput.setAttribute('aria-activedescendant', items[i].id);
    }

    if (searchInput && results) {
        searchInput.addEventListener('input', () => renderResults(searchInput.value));
        searchInput.addEventListener('focus', () => { if (searchInput.value) renderResults(searchInput.value); });
        searchInput.addEventListener('keydown', (event) => {
            if (results.hidden) return;
            if (event.key === 'ArrowDown') { event.preventDefault(); activeIndex = Math.min(matches.length - 1, activeIndex + 1); highlight(activeIndex); }
            else if (event.key === 'ArrowUp') { event.preventDefault(); activeIndex = Math.max(0, activeIndex - 1); highlight(activeIndex); }
            else if (event.key === 'Enter') { event.preventDefault(); openMatch(matches[activeIndex >= 0 ? activeIndex : 0]); }
            else if (event.key === 'Escape') { closeSearch(); }
        });
        results.addEventListener('click', (event) => {
            const btn = event.target.closest('.a-search-item');
            if (btn) openMatch(matches[Number(btn.dataset.i)]);
        });
        document.addEventListener('click', (event) => {
            if (!event.target.closest('.a-search')) closeSearch();
        });
        document.addEventListener('keydown', (event) => {
            if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === 'k') {
                event.preventDefault();
                searchInput.focus();
                searchInput.select();
            }
        });
    }

    /* ------------------------------------------------------------------
       Buttons whose editor does not exist yet
       ------------------------------------------------------------------ */
    document.addEventListener('click', (event) => {
        const trigger = event.target.closest('[data-bs-toggle="modal"], [data-soon]');
        if (!trigger) return;
        const targetSel = trigger.getAttribute('data-bs-target');
        if (trigger.hasAttribute('data-soon') || (targetSel && !document.querySelector(targetSel))) {
            event.preventDefault();
            event.stopPropagation();
            const label = trigger.textContent.replace(/\s+/g, ' ').trim();
            window.showAlert('Coming soon', `${label} is not available yet.`, 'info');
        }
    }, true);

    /* ------------------------------------------------------------------
       Small live details
       ------------------------------------------------------------------ */
    const threshold = $('#fcThreshold');
    const thresholdValue = $('#fcThresholdValue');
    if (threshold && thresholdValue) {
        threshold.addEventListener('input', () => { thresholdValue.textContent = threshold.value + '%'; });
    }

    // Spotlight glow that follows the pointer on cards
    if (window.matchMedia('(hover: hover) and (pointer: fine)').matches) {
        document.addEventListener('pointermove', (event) => {
            const card = event.target.closest('.a-card, .a-stat, .a-metric, .a-quick-btn');
            if (!card) return;
            const rect = card.getBoundingClientRect();
            card.style.setProperty('--sx', (event.clientX - rect.left) + 'px');
            card.style.setProperty('--sy', (event.clientY - rect.top) + 'px');
        }, { passive: true });
    }

    // Topbar shadow once the page scrolls
    const header = $('.admin-header');
    const onScroll = () => header && header.classList.toggle('is-scrolled', window.scrollY > 8);
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();

    /* ------------------------------------------------------------------
       Deep links (#analytics etc.) and first paint
       ------------------------------------------------------------------ */
    const initial = window.location.hash.slice(1);
    if (initial && document.getElementById(initial) && document.getElementById(initial).classList.contains('content-section')) {
        window.showSection(initial);
    } else {
        enterSection($('.content-section.active'));
    }

    const lastUpdated = $('#lastUpdated');
    if (lastUpdated) lastUpdated.textContent = new Date().toLocaleTimeString();
})();
