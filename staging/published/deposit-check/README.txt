DepositCheck v1.0.1 — Security Deposit Deduction Auditor
========================================================

WHAT THIS IS
A single-file offline app for renters who just moved out. You key your
landlord's itemized deduction list into a per-category auditor: each line
item is checked against useful-life depreciation math (HUD-style), and the
app computes the fair deduction total versus what was withheld — then
generates a printable dispute letter with the math itemized.

QUICK START
1. Double-click depositcheck.html (or unzip first, then open it).
2. Tap the flask icon in the header to load sample data and explore —
   tap it again to restore your own entries.
3. On the "1 · Deduction Audit" tab, enter your deposit and what was withheld.
4. Click "+ Add line item" for each charge on your landlord's itemization:
   description, category, classification (damage / wear / cleaning), item age,
   the amount charged, and the replacement cost if you know it.
5. Open "2 · Results & Report" for the fair-vs-withheld totals and the
   line-item audit table.
6. Open "3 · Dispute Letter", fill in the parties, and print the letter.
7. "4 · Legal Checklist" covers the generic state-law reminders.
8. "5 · Saved" stores audit snapshots in this browser only. Export all
   (JSON) downloads them as a file; Import JSON loads an export back.
   Useful-life assumptions can be edited per category, or reset to the
   shipped defaults with "Reset to defaults".

THE MATH
Tenant share = replacement cost × remaining useful life.
Remaining life = (expected life − item age) ÷ expected life, floored at 0.
If an item is past its useful life, the tenant owes nothing for it.
If replacement cost is left blank, the landlord's charge is treated as the
full replacement price. Items classified as normal wear & tear always audit
to a fair deduction of $0. Cleaning / non-depreciable charges are not
depreciated.

USEFUL-LIFE FIGURES (judgment calls baked into the app; HUD/Nolo-style)
Interior paint 4 yr · Carpet 8 yr · Vinyl/linoleum 10 yr · Hardwood 20 yr ·
Window blinds 5 yr · Refrigerator/stove 15 yr · Dishwasher 10 yr ·
Light fixtures 15 yr · Bathroom fixtures 20 yr · Countertops 20 yr.

OFFLINE & PRIVATE
No install, no account, no internet needed after download. Saved audits
live in this browser's localStorage only — nothing is uploaded.

DARK MODE & SOUND
Header toggles: dark mode (honors your OS preference on first load; your
choice is remembered) and sound effects (on by default; the mute choice is
remembered). The "More Apps" pill links to the full app catalog.

DISCLAIMER
Guidance only — not legal advice. Deposit rules and deadlines vary by
state; consult a tenant-rights organization or attorney for your situation.
