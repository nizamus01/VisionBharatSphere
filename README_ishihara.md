Ishihara 24-Plate Fast Test — VisionBharatSphere

What this is
- A single-file local demo (`ishihara_test_index.html`) that implements a fast, preloaded 24-plate Ishihara color vision screening.
- Features: image preloading for instant plate display, keyboard shortcuts (1-4), answer tracking, finish modal with diagnosis, and a simple report download.

How to run
1. Open the file in your browser: `ishihara_test_index.html` (double-click or drag into browser).
2. Wait until the plates finish preloading (you'll see "Loading plates (n/24)").
3. Click "Start Test". Use the numbered buttons or your keyboard to answer quickly. Use Next to go forward.
4. After the final plate, click Finish to see results. Download the report if desired.

Notes & next steps
- This is a static front-end demo. For production integration:
  - Move this into the existing site layout or Next.js page.
  - Hook the results to your backend (FastAPI/Flask) for storage, user accounts, and secure PDF generation.
  - Add server-side image hosting (or a CDN) to ensure fast, reliable plate delivery.

License
- Code included in this workspace is permissively licensed for your use within VisionBharatSphere.

