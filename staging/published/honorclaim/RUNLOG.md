# HonorClaim RUNLOG

## 2026-10-13 — build (subagent)
- Built single-file app at `staging/honorclaim/index.html` (~1,400 lines).
- Reused proven MileSentry patterns: header (More Apps pill, flask, dark, sound), localStorage schema, sample snapshot/restore, sounds, toast, modal, donut/hbar chart helpers, CSV/JSON import/export.
- Features: dashboard (clickable cards/lists), conditions + 6-item evidence checklists, symptom timeline, C&P exam organizer (prep + bring lists), claims tracker (stages, deadlines), VA combined-rating calculator with step-by-step math + bilateral toggle, personal/buddy statement planners (generate/copy/print/save), charts tab (rating donut, evidence hbars, claim-stage vbars, severity line), reports tab (printable claim packet, CSV/JSON, contacts).
- Liability: visible disclaimer (not legal advice, not VA-affiliated, VA decides claims alone, VSO/attorney off-ramp) on main + footer + print packet.
- Fixed during build: `esc()` had a wrong `"&lt;"` key instead of `"<"` — would have emitted "undefined" for `<` in names. Fixed before first test.

## Test results (all in real Chromium, 2026-10-13)
- Load: title, brand, 9 tabs, zero page errors.
- Sample data: 6 conditions load; dash cards render (6 total / 5 claimed / 67% evidence / next deadline).
- Dashboard clicks: card 1 → conditions tab; combined-rating card → calc tab; deadline rows scroll+highlight target.
- Calculator: conditions (50/10/20/10) → 70% combined, correct VA math; manual 50/30/10 → 70%; bilateral toggle computes factor and shows note.
- Donut: center "total rating pts / 90" → click PTSD slice → "PTSD / 50%" → re-click restores. (Playwright bbox-center click hit the donut hole on a >180° slice, so dispatch_event was used for segment clicks — a test artifact, not an app bug.)
- hbar: bar y/width identical before/after select (10/145); highlight band appears.
- vbar: bar y/height identical before/after select (247/3).
- Severity line: point click shows detail panel (date, condition, severity, notes).
- Chart symmetry: card bottoms [976,976,1571,1571] — rows line up.
- Statements: generate (personal) includes name + disclaimer line; save → 3 saved; view works.
- Exams: open, toggle prep, add notes → persisted on reopen.
- Claims: add deadline (with date), advance stage (evidence gathering → decision review), deadline checkbox.
- Dark mode: theme attr = dark, toggles show .on state; sound toggle off state verified.
- Export/import: CSV 21 rows (conditions + timeline); JSON has all 8 keys; import round-trip 6→5→6.
- Empty states render on fresh load (no sample).
- Mobile 390×844@2x: header wraps, tabs usable, donut center swap works, zero errors.
- Screenshots: /tmp/hc-dash.png, /tmp/hc-dash-dark.png, /tmp/hc-charts.png, /tmp/hc-mobile-dash.png, /tmp/hc-mobile-charts.png.

## 2026-10-13 bench fixes (parent adjudication)
API bench: 7/7 legs complete (Gemini/Groq/OpenRouter functional, Gemini/Groq copy/SEO, Gemini + free-vision images). MD5 reviewed: 8daf7ba19e4bddb05a38d18037087983.
Fixes applied:
1. MAJOR bilateral factor 3.5% -> 10% (38 CFR 4.26) at calcOut + label; dead combineWithBilateral (never called) deleted.
2. REAL BUG found in parent re-test (bench missed it): calcOut mapped {v, b:r.bilat} but read o.bilat — bilateral path NEVER executed. Fixed to {v, bilat:!!r.bilat}. Verified: 60+50 bilateral -> 80% x10% = +8% -> 88% -> rounded 90%.
3. Import IDs sanitized (cleanId strips [^a-zA-Z0-9_-]) in all sanitize fns — self-XSS via data-* attrs closed.
4. load() reads honorclaim.schema version.
5. renderAll no longer wipes calcRatings (was silently emptying hand-entered ratings on every save).
6. Corrupt-JSON recovery: raw copy stashed to honorclaim.corrupt-backup + downloadable from Reports tab.
7. Float rounding: raw rounded to 1 decimal before final nearest-10.
8. Charts tab bar labels: two-line word wrap instead of mid-word truncation (wrapLabel).
9. Mobile: tabs row scrolls horizontally <=640px instead of wrapping to 4 rows.
10. Next-deadline card: word-boundary truncation (wordCut) instead of mid-word slice.
Regression: my first edit dropped renderAll's closing brace (whole script failed to parse, caught by node parse check + tab test). Fixed and re-verified.
New MD5: 01e57ae0d1d802ef8a098cbe28187f54. Verified in Chromium: bilateral 90%, calc state kept 2->2, donut PTSD/50% select -> total on release, mobile tabs nowrap, zero page errors.
Outstanding: ChatGPT hands-on, Grok hands-on, Perplexity copy/SEO (browser legs).

## 2026-10-13 ChatGPT hands-on findings fixed (parent)
- BUG: condition dialog "Evidence checklist" tab did nothing — ct-ev click handler had hidden flags inverted (ev-pane hidden=true, det-pane hidden=false). Fixed. Verified in Chromium: evidence pane shows 6 checkboxes on click, details switches back; zero errors.
- UX: severity-line points got invisible r=16 hit circles (were 5px dots, hard to tap).
- New MD5: 630b54399f38f5645fc615a4755ea1d9.

## 2026-10-13 Grok hands-on findings (parent)
- Full report saved to app-pipeline/bench/honorclaim/functional/grok.md: 7/9 PASS, print-dialog confirmed modal-open (test-env limitation), import blocked in their session.
- FIX: Evidence Complete dashboard card now sorts Conditions tab neediest-first (evPct ascending), resets when user filters/searches. Verified: first row 17% after card click.
- Import round-trip verified by parent in Chromium: export JSON -> delete condition -> import -> 6 conditions, 12 events, 2 exams, 2 claims restored. Zero page errors.
- New MD5: 897ba6da047bd31d9b69126cb7af4ca1.
