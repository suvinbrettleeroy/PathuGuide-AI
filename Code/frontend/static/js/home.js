/* ==========================================================================
   PathGuide — Home page extras (search routing, typewriter placeholder).
   Shared motion lives in pg-core.js.
   ========================================================================== */
(function () {
    'use strict';

    const root = document.documentElement;
    const cfg = window.PG_HOME || {};
    const motionOK = !window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const introDelay = root.classList.contains('pg-seen') ? 450 : 1500;

    const $ = (sel, ctx = document) => ctx.querySelector(sel);

    function toast(message, ok = true) {
        if (typeof window.showLocationToast === 'function') {
            window.showLocationToast(message, ok);
        }
    }

    if (typeof window.updateClock === 'function') window.updateClock();

    /* ------------------------------------------------------------------
       Hero search: route to the matching path
       ------------------------------------------------------------------ */
    const searchForm = $('#pgSearch');
    const searchInput = $('#pgSearchInput');
    const examWords = [
        'tnpsc', 'group', 'exam', 'govt', 'government', 'tnusrb', 'police', 'constable', 'trb', 'tet',
        'vao', 'tangedco', 'tneb', 'mrb', 'sub inspector', 'fireman', 'fire service', 'jail', 'warder',
        'syllabus', 'mock', 'notification', 'teacher', 'fitness',
        'தேர்வு', 'அரசு', 'காவல்', 'ஆசிரியர்', 'பாடத்திட்டம்'
    ];

    if (searchForm && searchInput) {
        searchForm.addEventListener('submit', (event) => {
            event.preventDefault();
            const query = searchInput.value.trim().toLowerCase();
            if (!query) {
                searchForm.classList.remove('is-shake');
                void searchForm.offsetWidth;
                searchForm.classList.add('is-shake');
                searchInput.focus();
                toast(cfg.searchEmpty, false);
                return;
            }
            const isExam = examWords.some((word) => query.includes(word));
            window.selectPath(isExam ? 'govt_exam' : 'career');
        });
        searchForm.addEventListener('animationend', (event) => {
            if (event.animationName === 'pgShake') searchForm.classList.remove('is-shake');
        });

        // Typewriter placeholder cycling through example searches
        const phrases = Array.isArray(cfg.placeholders) ? cfg.placeholders : [];
        if (motionOK && phrases.length > 1) {
            let phraseIndex = 0;
            let charIndex = phrases[0].length;
            let deleting = true;

            const tick = () => {
                if (document.activeElement === searchInput || searchInput.value) {
                    setTimeout(tick, 1200);
                    return;
                }
                const phrase = phrases[phraseIndex];
                if (deleting) {
                    charIndex -= 1;
                    searchInput.placeholder = phrase.slice(0, Math.max(0, charIndex));
                    if (charIndex <= 0) {
                        deleting = false;
                        phraseIndex = (phraseIndex + 1) % phrases.length;
                        setTimeout(tick, 320);
                    } else {
                        setTimeout(tick, 26);
                    }
                } else {
                    charIndex += 1;
                    searchInput.placeholder = phrase.slice(0, charIndex);
                    if (charIndex >= phrase.length) {
                        deleting = true;
                        setTimeout(tick, phraseIndex === 0 ? 4200 : 2200);
                    } else {
                        setTimeout(tick, 55);
                    }
                }
            };

            searchInput.addEventListener('focus', () => { searchInput.placeholder = phrases[0]; });
            setTimeout(tick, introDelay + 4000);
        }
    }
})();
