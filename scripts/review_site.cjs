// Copyright 2026 Juan Pablo Traverso Gianini. SPDX-License-Identifier: Apache-2.0
// Requires Playwright and a browser. Start the local server described in WEB_PUBLICATION.md.
const { chromium } = require('playwright');
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
(async () => {
  const root = path.resolve(__dirname, '..');
  const output = path.join(root, 'publication', 'web-qa');
  fs.mkdirSync(output, { recursive: true });
  const browser = await chromium.launch({
    headless: true,
    ...(process.env.BROWSER_PATH ? { executablePath: process.env.BROWSER_PATH } : {})
  });
  const rows = [];
  try {
    for (const [label, width, height] of [['desktop', 1280, 900], ['mobile', 390, 844]]) {
      const page = await browser.newPage({ viewport: { width, height } });
      for (const [name, url] of [['series', '/'], ['paper-I', '/preprints/PAPER_I/index.html'], ['paper-II', '/preprints/PAPER_II/index.html']]) {
        const response = await page.goto('http://127.0.0.1:8765' + url, { waitUntil: 'networkidle' });
        if (response.status() !== 200) throw new Error('HTTP error for ' + url);
        const dimensions = await page.evaluate(() => ({
          viewport: window.innerWidth,
          scroll: document.documentElement.scrollWidth,
          imagesMissing: [...document.images].filter(i => !i.complete || i.naturalWidth === 0).length
        }));
        if (dimensions.scroll > dimensions.viewport || dimensions.imagesMissing) {
          throw new Error('Layout issue: ' + JSON.stringify(dimensions));
        }
        const filename = `${name}-${label}.png`;
        await page.screenshot({ path: path.join(output, filename), fullPage: true });
        rows.push({ page: url, viewport: { width, height }, dimensions,
          screenshot: `publication/web-qa/${filename}`,
          html_sha256: crypto.createHash('sha256').update(fs.readFileSync(path.join(root, url === '/' ? 'index.html' : url.slice(1)))).digest('hex'),
          css_sha256: crypto.createHash('sha256').update(fs.readFileSync(path.join(root, 'assets/style.css'))).digest('hex'),
          sha256: crypto.createHash('sha256').update(fs.readFileSync(path.join(output, filename))).digest('hex') });
      }
      await page.close();
    }
  } finally {
    await browser.close();
  }
  fs.writeFileSync(path.join(output, 'checks.json'), JSON.stringify({
    status: 'PASS_BROWSER_LAYOUT_CHECKS', browser: 'Chromium', rows,
    scope: 'HTTP, viewport overflow, missing images and screenshots; visual interpretation recorded separately.'
  }, null, 2) + '\n');
  console.log('PASS: six desktop/mobile page checks; screenshots recorded.');
})();
