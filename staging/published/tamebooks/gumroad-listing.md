# Gumroad listing — TameBooks (published 2026-10-01)

## Product
- Product ID: `qpyije`
- Public URL: https://glenerds.gumroad.com/l/qpyije
- Status: PUBLISHED (live, verified 2026-10-01: HTTP 200, correct title, price 0)

## Title (SEO, no "TameBooks", no "free")
`Simple Bookkeeping Software for Small Business — Offline Accounting App with Invoicing, No Subscription`

## Price
`$0+`, pay-what-you-want enabled ("Name a fair price:"). No "free" wording anywhere.

## Description
SaveTrail format. Source: `~/workspace/app-pipeline/bench/tamebooks/copy_seo/proposed-title-description.md`.

## Thumbnail (1080×1080, true square) — the only custom graphic
- File: `gallery/covers/thumb-32.png`
- Glen's pick #32 (deep-green, invoice + $ badge icon, big "TameBooks" + giant "BOOKKEEPING"),
  approved 2026-10-01: ships exactly as approved, no changes.
- Uploaded to the Gumroad Thumbnail field only — NOT in the gallery.

## Gallery (7 screenshots, 1280×800, all captured from exact final bytes MD5 `0dd5f195`)
Live on the listing, in order:
1. shot-dashboard.png (light)
2. shot-invoices.png (light)
3. shot-pl.png (light)
4. shot-bs.png (light)
5. shot-cf.png (light)
6. shot-dashboard-dark.png (dark mode)
7. shot-pl-dark.png (dark mode)
Dark-mode shots added 2026-10-01 per Glen ("you did not add any dark mode
pictures") — same bytes, same demo data, theme toggled via #btn-theme;
visually verified (contrast, no clipping, charts render). The ledger keeps
the superseded shot-ar.png and shot-tax.png for the record; they are no
longer on the live listing.

## Product file
`tamebooks-1.0.0.zip` (contains only `index.html`; extracted MD5 matches `0dd5f195`).

## Tags (Share → Gumroad Discover, all ≤20 chars)
bookkeeping, accounting, small business, invoicing, offline app

## QA summary
- Round-4 browser-operator hands-on QA on prior bytes found 3 findings:
  - BUG-TYPO-2 ("Liabilitys"/"Equitys") — CONFIRMED, fixed.
  - BUG-INV-3 (inventory sales posted no COGS) — CONFIRMED, fixed (auto-create
    Inventory/COGS accounts, opening-stock journal entry, no silent COGS skips).
  - BUG-ESC-2 (Escape closing stacked modals) — NOT A BUG (false positive).
- Fixes verified by real-click e2e: 15/15 PASS (opening stock posted, accounts
  auto-created, sale relieved $190 COGS, inventory $760, Balance Sheet balanced,
  Escape closes only topmost modal).
- 63/63 node tests pass; inlined JS passes node --check.
- Image gate (Gemini PASS + direct-visual PASS) stands on pixel-identical re-captured shots.
