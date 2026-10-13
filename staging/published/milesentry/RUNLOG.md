# MileSentry — build run log

## 2026-10-13 — build started
- Created work dir ~/workspace/glenerds-microsite/staging/milesentry/.
- Plan: single-file index.html — program register (manual entry), expiry engine (fixed date | inactivity window | never), urgency dashboard, activity log, charts tab (donut / days-remaining bars / at-risk by bucket / activity per month), printable points-at-risk report, JSON+CSV, sample data (10 programs).
- Standards: no prompt/alert/confirm (in-page modals), CSV quotes all fields, validated import + overwrite confirm, ≥15px text incl. SVG, dark mode, WebAudio sounds on by default, no "free" copy.

## Build complete, starting QA
- index.html written (~1300 lines): dashboard, programs, activity, charts, reports tabs.
- Fixed during writing: .tag.safe CSS hex typo (#d9ecd d), delete-handler showing raw id.
- Now: syntax check + hands-on QA in Chromium.

## QA complete — 2026-10-13
All hands-on tests in Chromium (patchright, real clicks, DOM assertions — evaluate() can't see page-script globals):
- Days-remaining math hand-checked vs 2026-10-13: United fixed 10-19 → 6d critical; Southwest inactivity 10-14-2024+24mo → 1d critical; American 11-05-2024+24mo → 23d warning; Hyatt fixed 12-01 → 49d watch; Hilton 12-22-2024+24mo → 70d notice; Delta 02-15-2026+24mo → 490d safe. All correct.
- Add program via modal (fixed date + inactivity + never rules) — works.
- Activity log resets inactivity clock: 2026-01-01+12mo (80d) → logged 2026-10-13 → expiry 2027-10-13, 365d safe. Balance updated 5000→6000.
- Unknown bucket: inactivity rule with no last activity → "?d" tag, "expires log activity".
- Charts: 4 SVGs render; donut/hbar/vbar/act click-spotlight selects (outline + offset) and releases on 2nd click; card bottoms aligned per row (893/893, 1488/1488).
- Dark mode persists across reload (explicit choice, no OS fallback). Sound toggle persists.
- Sample mode: 10 programs load, amber banner, exit restores user data exactly.
- JSON export/import: valid round-trip; garbage JSON and wrong-shape rejected with clear toasts, data intact; overwrite requires in-page confirm modal.
- CSV: all fields quoted, "" escaping verified ('Test ""Quote"", Comma Air').
- Program + activity delete via in-page confirm modal — work.
- Print report tab populates sorted by urgency.
- Zero console/page errors. No prompt()/alert()/confirm() anywhere. No "free" copy. Zero external requests (only More Apps nav links).
- Fixed during QA: .tag.safe CSS hex typo; hbar value-label clipping at right edge (twice — final: value inside bar when w>=52, outside otherwise); delete handler showing raw id; screenshots re-captured (7 viewport shots).
- Gallery: 1-dashboard-light, 2-charts-light, 3-dashboard-dark, 4-charts-dark, 5-mobile-dashboard, 6-mobile-charts, 7-reports-light.
- Known limitations: expiry reminders are visual only (no push/email — offline by design); sample data fixed dates drift over time; donut shows top 8 programs + Other.
- Final MD5: c10d408243ef460a879f42a8c34e720a

## 2026-10-13 pipeline (parent agent run)
- MD5 verified before work: c10d408243ef460a879f42a8c34e720a — matched, proceeded.
- Thumbnail: Glen approved media-generation-milesentry-thumb-g5 (250,000 PTS medallion, plain flat gold lettering, organized card row). Converted to 1080x1080 PNG: ~/workspace/thumb-audit/new/milesentry-APPROVED.png
- Cover 1280x720 derived from thumbnail: ~/workspace/thumb-audit/new/milesentry-cover-1280.png (name top, medallion middle, one plain line bottom). Visually verified.
- Gallery: 8th screenshot added (8-reports-dark.png, dark-mode reports tab, toast-free). All 8 are current app UI.
- Bench (API legs):
  - functional/gemini.md (gemini-3.1-pro-preview): 8 claims, all rejected on code inspection.
  - functional/groq.md (gpt-oss-120b, core functions): 6 claims, all rejected.
  - functional/openrouter.md (Cohere command-a-03-2025 substituted; OpenRouter free models 404, Mistral errored): 1 minor hardening accepted -> effTheme now validates stored value; 9 rejected.
  - Fixes: removed dead activity `note` field; effTheme validation. Targeted Chromium re-verification: zero console errors, activity logging works, theme fallback correct. Final MD5: cf6d04ae2df506573fc3d06a48b8defb
  - copy_seo/gemini.md + groq.md delivered; adjudicated into gumroad-listing.md (no brand in title, no "free", no "spreadsheet").
  - images/gemini.md: thumbnail legible, flat lettering, balanced; 2 minor background artifacts, image unchanged (Glen-approved final).
  - Pending (need live browser): ChatGPT + Grok hands-on legs, Perplexity copy/SEO leg.
- ZIP: milesentry-1.0.0.zip (index.html only); extracted MD5 matches cf6d04ae2df506573fc3d06a48b8defb.
- Moved staging/milesentry -> staging/published/milesentry.
- Done page: MileSentry row added at top with plain-English description; count 68 -> 69. NOTE: Gumroad cell links https://glenerds.gumroad.com/l/milesentry as PLACEHOLDER — replace with real product URL after draft creation.
- Push: push-dir failed (1549-file drift, GitHub 502 on blob upload). Fell back to per-file Contents API PUTs: 13/13 OK (12 new + done page update).
- push-guard: recorded push-20261013-174157; verify --id returned OK.
- Live verification: https://glenerds.github.io/glenerds/staging/published/milesentry/index.html -> 200, MD5 cf6d04ae2df506573fc3d06a48b8defb MATCHES local.
- Old staging URL https://glenerds.github.io/glenerds/staging/milesentry/index.html -> 404 (never pushed).
- Done page live: "69 apps" + milesentry row present.
- REMAINING: Gumroad unpublished draft creation + 8 screenshots + thumbnail upload + publish (needs browser task with Glen's login). Then replace placeholder Gumroad URL on done page + push.
