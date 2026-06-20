# The Parlour — A Private Games Concierge

A single-page Father's Day surprise. The recipient scans a QR code, opens a
"sealed dossier," and taps to reveal the gift (Balatro) — framed as a
white-glove video-game concierge service.

- **Live page:** https://spearw.github.io/the-concierge/
- **Tech:** one self-contained `index.html` (inline CSS/JS, Google Fonts). No build step.
- **Hosting:** GitHub Pages (deploys from `main`, root).
- **QR codes:** `qr.png` / `qr.svg` (classic black/white), `qr-themed.svg` (navy on cream).

## Personalize before gifting

Search `index.html` for `class="ph"` (placeholders, shown with a dashed gold underline):

1. `[ his name ]` — on the cover card
2. `[ A personal line about why Balatro suits him ]` — "Why this one, for you"
3. `[ your name ]` — in service step III and the sign-off (two spots)
4. `[ When & where ]` — the itinerary

Commit + push to update the live page (Pages redeploys automatically).
