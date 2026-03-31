# Precinct 1 Website Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a no-build GitHub Pages website for Brookline Precinct 1 with a civic visual system, a practical homepage, a public Town Meeting Members page, an election information page, placeholder content pages, and a curated links directory.

**Architecture:** The site will be a hand-authored multi-page static website with shared CSS and lightweight JavaScript. Every HTML file will include the same navigation, footer, type system, and responsive layout, while a single Python smoke-test script verifies required files, public content, and the omission of private TMM contact details.

**Tech Stack:** HTML5, CSS3, vanilla JavaScript, Python 3 standard library for validation

---

## File Structure

- Create: `/Users/robschoen/Dropbox/CC/P1/index.html`
- Create: `/Users/robschoen/Dropbox/CC/P1/tmms.html`
- Create: `/Users/robschoen/Dropbox/CC/P1/election-information.html`
- Create: `/Users/robschoen/Dropbox/CC/P1/about.html`
- Create: `/Users/robschoen/Dropbox/CC/P1/warrant-may-2026.html`
- Create: `/Users/robschoen/Dropbox/CC/P1/events.html`
- Create: `/Users/robschoen/Dropbox/CC/P1/links.html`
- Create: `/Users/robschoen/Dropbox/CC/P1/styles.css`
- Create: `/Users/robschoen/Dropbox/CC/P1/script.js`
- Create: `/Users/robschoen/Dropbox/CC/P1/tests/check_site.py`
- Create: `/Users/robschoen/Dropbox/CC/P1/README.md`

## Task 1: Add the Validation Harness

**Files:**
- Create: `/Users/robschoen/Dropbox/CC/P1/tests/check_site.py`

- [ ] **Step 1: Write the failing validation script**

```python
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "index.html",
    "tmms.html",
    "election-information.html",
    "about.html",
    "warrant-may-2026.html",
    "events.html",
    "links.html",
    "styles.css",
    "script.js",
    "README.md",
]

PAGE_NEEDLES = {
    "index.html": [
        "Brookline Precinct 1",
        "Election Information",
        "Precinct Maps",
        "TMMs P1",
        "Links",
    ],
    "tmms.html": [
        "Town Meeting Members",
        "Ana Albuquerque",
        "Robert Schoen",
        "Term expires",
    ],
    "election-information.html": [
        "Election Information",
        "43 Hawes Street",
        "Where Do I Vote",
    ],
    "about.html": ["About Precinct 1", "This page will be expanded soon"],
    "warrant-may-2026.html": ["May 2026 Warrant", "This page will be expanded soon"],
    "events.html": ["P1 Events", "This page will be expanded soon"],
    "links.html": [
        "Brookline PAX",
        "Budget Central",
        "Brookline Town Meeting - current files",
    ],
}

FORBIDDEN_TMM_STRINGS = [
    "@",
    "617",
    "24 Euston Street",
    "79 Carlton Street",
]


def read_text(path_str: str) -> str:
    path = ROOT / path_str
    assert path.exists(), f"Missing file: {path_str}"
    return path.read_text(encoding="utf-8")


def main() -> None:
    for path_str in REQUIRED_FILES:
        assert (ROOT / path_str).exists(), f"Missing file: {path_str}"

    for page, needles in PAGE_NEEDLES.items():
        html = read_text(page)
        for needle in needles:
            assert needle in html, f"{page} is missing: {needle}"

    tmms_html = read_text("tmms.html")
    for forbidden in FORBIDDEN_TMM_STRINGS:
        assert forbidden not in tmms_html, f"Forbidden public detail found in tmms.html: {forbidden}"

    print("All site checks passed.")


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Run the validation script to verify it fails**

Run: `python3 tests/check_site.py`

Expected: FAIL with an assertion like `Missing file: index.html`

- [ ] **Step 3: Save the validation script exactly as written**

```bash
mkdir -p tests
```

- [ ] **Step 4: Re-run the validation script and confirm it still fails for missing site files**

Run: `python3 tests/check_site.py`

Expected: FAIL with `Missing file: index.html`

- [ ] **Step 5: Commit the validation harness scaffold when the repository exists**

```bash
git add tests/check_site.py
git commit -m "test: add static site smoke checks"
```

## Task 2: Build Shared Styles and Shared Page Chrome

**Files:**
- Create: `/Users/robschoen/Dropbox/CC/P1/styles.css`
- Create: `/Users/robschoen/Dropbox/CC/P1/script.js`
- Create: `/Users/robschoen/Dropbox/CC/P1/index.html`
- Create: `/Users/robschoen/Dropbox/CC/P1/about.html`
- Create: `/Users/robschoen/Dropbox/CC/P1/warrant-may-2026.html`
- Create: `/Users/robschoen/Dropbox/CC/P1/events.html`

- [ ] **Step 1: Expand the validation script to check shared navigation labels**

```python
PAGE_NEEDLES = {
    "index.html": [
        "Brookline Precinct 1",
        "Election Information",
        "Precinct Maps",
        "TMMs P1",
        "Links",
        "About Precinct 1",
        "May 2026 Warrant",
        "P1 Events",
    ],
    "about.html": ["About Precinct 1", "Welcome", "Links"],
    "warrant-may-2026.html": ["May 2026 Warrant", "Welcome", "Links"],
    "events.html": ["P1 Events", "Welcome", "Links"],
}
```

- [ ] **Step 2: Run the validation script to verify the new checks fail**

Run: `python3 tests/check_site.py`

Expected: FAIL because the HTML files do not exist yet

- [ ] **Step 3: Write the shared stylesheet**

```css
:root {
  --bg: #f5f1e8;
  --surface: rgba(255, 252, 247, 0.92);
  --surface-strong: #fffdf8;
  --text: #1e2b33;
  --muted: #53616a;
  --accent: #4d6b52;
  --accent-dark: #324a38;
  --border: rgba(30, 43, 51, 0.14);
  --shadow: 0 24px 60px rgba(31, 41, 45, 0.08);
  --radius: 22px;
  --content-width: 1120px;
}

*,
*::before,
*::after {
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
}

body {
  margin: 0;
  font-family: "Source Sans 3", "Trebuchet MS", sans-serif;
  color: var(--text);
  background:
    radial-gradient(circle at top left, rgba(132, 157, 120, 0.18), transparent 32rem),
    linear-gradient(180deg, #fbf8f2 0%, var(--bg) 100%);
  line-height: 1.6;
}

a {
  color: var(--accent-dark);
}

a:hover,
a:focus-visible {
  color: var(--accent);
}

img,
iframe {
  max-width: 100%;
}

.site-shell {
  width: min(calc(100% - 2rem), var(--content-width));
  margin: 0 auto;
}

.site-header {
  position: sticky;
  top: 0;
  z-index: 20;
  backdrop-filter: blur(14px);
  background: rgba(251, 248, 242, 0.86);
  border-bottom: 1px solid var(--border);
}

.site-header__inner,
.site-footer,
.page-section,
.hero,
.page-hero {
  width: min(calc(100% - 2rem), var(--content-width));
  margin: 0 auto;
}

.site-header__inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  padding: 1rem 0;
}

.site-brand {
  text-decoration: none;
  color: var(--text);
}

.site-brand__eyebrow {
  display: block;
  font-size: 0.8rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--muted);
}

.site-brand__name,
.hero h1,
.page-hero h1,
.section-title {
  font-family: "Cormorant Garamond", Georgia, serif;
}

.site-brand__name {
  display: block;
  font-size: 1.8rem;
  line-height: 1;
}

.site-nav {
  display: flex;
  gap: 0.75rem;
  flex-wrap: wrap;
  align-items: center;
}

.site-nav a {
  text-decoration: none;
  color: var(--text);
  padding: 0.45rem 0.8rem;
  border-radius: 999px;
}

.site-nav a[aria-current="page"] {
  background: rgba(77, 107, 82, 0.14);
  color: var(--accent-dark);
}

.menu-toggle {
  display: none;
  border: 1px solid var(--border);
  border-radius: 999px;
  background: var(--surface-strong);
  color: var(--text);
  padding: 0.55rem 0.9rem;
}

.hero,
.page-hero {
  padding: 4rem 0 1.5rem;
}

.hero-copy,
.page-hero__copy,
.card,
.map-card,
.directory-group,
.placeholder-panel,
.member-table,
.fact-panel {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
}

.hero-copy,
.page-hero__copy,
.placeholder-panel,
.fact-panel {
  padding: 2rem;
}

.hero h1,
.page-hero h1 {
  margin: 0 0 1rem;
  font-size: clamp(2.8rem, 5vw, 4.8rem);
  line-height: 0.92;
}

.hero-actions,
.card-grid,
.map-grid,
.quick-facts,
.directory-grid {
  display: grid;
  gap: 1.25rem;
}

.card-grid,
.directory-grid {
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
}

.map-grid,
.quick-facts {
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
}

.card,
.map-card,
.directory-group {
  padding: 1.5rem;
}

.button-link {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 44px;
  padding: 0.8rem 1.2rem;
  border-radius: 999px;
  background: var(--accent);
  color: #f9f7f3;
  text-decoration: none;
}

.button-link--secondary {
  background: transparent;
  color: var(--accent-dark);
  border: 1px solid rgba(77, 107, 82, 0.38);
}

.page-section {
  padding: 1.5rem 0 3rem;
}

.section-title {
  margin: 0 0 1rem;
  font-size: clamp(2rem, 3vw, 3rem);
}

.member-table {
  width: 100%;
  border-collapse: collapse;
  overflow: hidden;
}

.member-table th,
.member-table td {
  padding: 0.95rem 1rem;
  border-bottom: 1px solid var(--border);
  text-align: left;
}

.member-table th {
  background: rgba(77, 107, 82, 0.1);
}

.site-footer {
  padding: 0 0 3rem;
  color: var(--muted);
}

.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}

:focus-visible {
  outline: 3px solid rgba(77, 107, 82, 0.38);
  outline-offset: 3px;
}

@media (max-width: 860px) {
  .menu-toggle {
    display: inline-flex;
  }

  .site-nav {
    display: none;
    width: 100%;
    flex-direction: column;
    align-items: stretch;
    padding-top: 0.75rem;
  }

  .site-nav.is-open {
    display: flex;
  }

  .site-header__inner {
    flex-wrap: wrap;
  }
}
```

- [ ] **Step 4: Write the shared JavaScript**

```js
const nav = document.querySelector("[data-site-nav]");
const toggle = document.querySelector("[data-menu-toggle]");

if (nav && toggle) {
  toggle.addEventListener("click", () => {
    const isOpen = nav.classList.toggle("is-open");
    toggle.setAttribute("aria-expanded", String(isOpen));
  });
}

const currentPath = window.location.pathname.split("/").pop() || "index.html";

document.querySelectorAll("[data-nav-link]").forEach((link) => {
  const href = link.getAttribute("href");
  if (href === currentPath || (href === "index.html" && currentPath === "")) {
    link.setAttribute("aria-current", "page");
  }
});
```

- [ ] **Step 5: Create the shared HTML shell on the homepage**

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Brookline Precinct 1</title>
    <meta
      name="description"
      content="A non-partisan information site for Brookline, Massachusetts Precinct 1."
    />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Source+Sans+3:wght@400;600;700&display=swap"
      rel="stylesheet"
    />
    <link rel="stylesheet" href="styles.css" />
    <script src="script.js" defer></script>
  </head>
  <body>
    <header class="site-header">
      <div class="site-header__inner">
        <a class="site-brand" href="index.html">
          <span class="site-brand__eyebrow">Brookline, Massachusetts</span>
          <span class="site-brand__name">Precinct 1</span>
        </a>
        <button
          class="menu-toggle"
          type="button"
          data-menu-toggle
          aria-expanded="false"
          aria-controls="site-nav"
        >
          Menu
        </button>
        <nav class="site-nav" id="site-nav" data-site-nav aria-label="Primary">
          <a data-nav-link href="index.html">Welcome</a>
          <a data-nav-link href="tmms.html">TMMs P1</a>
          <a data-nav-link href="election-information.html">Election Information</a>
          <a data-nav-link href="about.html">About Precinct 1</a>
          <a data-nav-link href="warrant-may-2026.html">May 2026 Warrant</a>
          <a data-nav-link href="events.html">P1 Events</a>
          <a data-nav-link href="links.html">Links</a>
        </nav>
      </div>
    </header>

    <main>
      <section class="hero">
        <div class="hero-copy">
          <p class="site-brand__eyebrow">Non-partisan civic information</p>
          <h1>Brookline Precinct 1</h1>
          <p>
            A simple public information site for residents looking for voting details,
            precinct maps, Town Meeting information, and useful Brookline resources.
          </p>
        </div>
      </section>
    </main>

    <footer class="site-footer">
      <p>
        This site is intended as a non-partisan information resource for Brookline
        Precinct 1.
      </p>
    </footer>
  </body>
</html>
```

- [ ] **Step 6: Create the three placeholder pages with the same header and footer**

```html
<main>
  <section class="page-hero">
    <div class="page-hero__copy">
      <p class="site-brand__eyebrow">Precinct 1 reference</p>
      <h1>About Precinct 1</h1>
      <p>This page will be expanded soon with more precinct background information.</p>
    </div>
  </section>
</main>
```

```html
<main>
  <section class="page-hero">
    <div class="page-hero__copy">
      <p class="site-brand__eyebrow">Town meeting materials</p>
      <h1>May 2026 Warrant</h1>
      <p>This page will be expanded soon with warrant-related information.</p>
    </div>
  </section>
</main>
```

```html
<main>
  <section class="page-hero">
    <div class="page-hero__copy">
      <p class="site-brand__eyebrow">Precinct 1 community calendar</p>
      <h1>P1 Events</h1>
      <p>This page will be expanded soon with precinct event information.</p>
    </div>
  </section>
</main>
```

- [ ] **Step 7: Run the validation script**

Run: `python3 tests/check_site.py`

Expected: FAIL because `tmms.html`, `election-information.html`, `links.html`, and `README.md` do not exist yet

- [ ] **Step 8: Commit the shared shell**

```bash
git add styles.css script.js index.html about.html warrant-may-2026.html events.html
git commit -m "feat: add shared static site shell"
```

## Task 3: Build the Welcome Page Content and Map Section

**Files:**
- Modify: `/Users/robschoen/Dropbox/CC/P1/index.html`

- [ ] **Step 1: Extend the validation script to check for map asset links and homepage cards**

```python
PAGE_NEEDLES["index.html"] += [
    "Precinct Maps",
    "assets/Precinct34x46_202208241152573823.pdf",
    "assets/GIS-Precinct11x17_202205201122255708.pdf",
    "Town Meeting Members",
    "P1 Events",
]
```

- [ ] **Step 2: Run the validation script to verify the homepage content check fails**

Run: `python3 tests/check_site.py`

Expected: FAIL because the homepage does not yet include the map assets and section labels

- [ ] **Step 3: Replace the homepage `<main>` with the full welcome content**

```html
<main>
  <section class="hero">
    <div class="hero-copy">
      <p class="site-brand__eyebrow">Non-partisan civic information</p>
      <h1>Brookline Precinct 1</h1>
      <p>
        This website is a neutral public reference for Brookline Precinct 1,
        designed to make election information, precinct maps, and town resources
        easy to find.
      </p>
      <div class="hero-actions">
        <a class="button-link" href="election-information.html">Election Information</a>
        <a class="button-link button-link--secondary" href="#maps">Precinct Maps</a>
      </div>
    </div>
  </section>

  <section class="page-section" id="maps">
    <h2 class="section-title">Precinct Maps</h2>
    <div class="map-grid">
      <article class="map-card">
        <h3>Brookline precinct map</h3>
        <p>
          A larger townwide precinct map for understanding how Precinct 1 relates
          to the rest of Brookline.
        </p>
        <a class="button-link" href="assets/Precinct34x46_202208241152573823.pdf">Open precinct map</a>
      </article>
      <article class="map-card">
        <h3>Precinct 1 map</h3>
        <p>
          A closer precinct map focused on the Precinct 1 area and boundary detail.
        </p>
        <a class="button-link" href="assets/GIS-Precinct11x17_202205201122255708.pdf">Open P1 map</a>
      </article>
    </div>
    <p>
      Additional precinct boundary file:
      <a href="assets/Precinct1BWbook_202205201023379661.pdf">Precinct 1 boundary reference PDF</a>.
    </p>
  </section>

  <section class="page-section">
    <h2 class="section-title">Quick Access</h2>
    <div class="card-grid">
      <article class="card">
        <h3>Election Information</h3>
        <p>Find the Precinct 1 polling place, voting guidance, and official election resources.</p>
        <a href="election-information.html">Go to election information</a>
      </article>
      <article class="card">
        <h3>Town Meeting Members</h3>
        <p>See the current list of Precinct 1 Town Meeting Members and their term expiration years.</p>
        <a href="tmms.html">Go to TMMs P1</a>
      </article>
      <article class="card">
        <h3>P1 Events</h3>
        <p>Check this page for precinct-related event information as it is added.</p>
        <a href="events.html">Go to events</a>
      </article>
      <article class="card">
        <h3>Links</h3>
        <p>Browse local civic, budget, news, and town meeting resources in one place.</p>
        <a href="links.html">Go to links</a>
      </article>
    </div>
  </section>
</main>
```

- [ ] **Step 4: Run the validation script**

Run: `python3 tests/check_site.py`

Expected: FAIL because `tmms.html`, `election-information.html`, `links.html`, and `README.md` still do not exist

- [ ] **Step 5: Commit the homepage**

```bash
git add index.html
git commit -m "feat: add precinct homepage and map access"
```

## Task 4: Build the Public Town Meeting Members Page

**Files:**
- Create: `/Users/robschoen/Dropbox/CC/P1/tmms.html`

- [ ] **Step 1: Tighten the validation script to check the full public TMM list**

```python
PAGE_NEEDLES["tmms.html"] = [
    "Town Meeting Members",
    "Term expires",
    "Ana Albuquerque",
    "Rui Albuquerque",
    "Cathleen C. Cavell",
    "Susan Helms Daley",
    "Sarah Ericsson",
    "Amy R. Evenson",
    "Neil R. Gordon",
    "Carol B. Hillman",
    "Katherine A Ingraham",
    "Bradford Kimball",
    "Louise King",
    "Sean M. Lynn-Jones",
    "Sarah Moghtader",
    "Bettina Neuefeind",
    "Robert Schoen",
]
```

- [ ] **Step 2: Run the validation script to verify the TMM page check fails**

Run: `python3 tests/check_site.py`

Expected: FAIL because `tmms.html` does not exist yet

- [ ] **Step 3: Create the TMM page with public-safe data only**

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>TMMs P1 | Brookline Precinct 1</title>
    <meta
      name="description"
      content="Town Meeting Members for Brookline Precinct 1."
    />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Source+Sans+3:wght@400;600;700&display=swap"
      rel="stylesheet"
    />
    <link rel="stylesheet" href="styles.css" />
    <script src="script.js" defer></script>
  </head>
  <body>
    <header class="site-header">
      <div class="site-header__inner">
        <a class="site-brand" href="index.html">
          <span class="site-brand__eyebrow">Brookline, Massachusetts</span>
          <span class="site-brand__name">Precinct 1</span>
        </a>
        <button class="menu-toggle" type="button" data-menu-toggle aria-expanded="false" aria-controls="site-nav">Menu</button>
        <nav class="site-nav" id="site-nav" data-site-nav aria-label="Primary">
          <a data-nav-link href="index.html">Welcome</a>
          <a data-nav-link href="tmms.html">TMMs P1</a>
          <a data-nav-link href="election-information.html">Election Information</a>
          <a data-nav-link href="about.html">About Precinct 1</a>
          <a data-nav-link href="warrant-may-2026.html">May 2026 Warrant</a>
          <a data-nav-link href="events.html">P1 Events</a>
          <a data-nav-link href="links.html">Links</a>
        </nav>
      </div>
    </header>

    <main>
      <section class="page-hero">
        <div class="page-hero__copy">
          <p class="site-brand__eyebrow">Town meeting reference</p>
          <h1>Town Meeting Members</h1>
          <p>
            Brookline Town Meeting Members represent their precincts at Town Meeting.
            This page lists the current public member names for Precinct 1 and the
            year each term expires.
          </p>
        </div>
      </section>

      <section class="page-section">
        <table class="member-table">
          <thead>
            <tr>
              <th scope="col">Member</th>
              <th scope="col">Term expires</th>
            </tr>
          </thead>
          <tbody>
            <tr><td>Ana Albuquerque</td><td>2028</td></tr>
            <tr><td>Rui Albuquerque</td><td>2026</td></tr>
            <tr><td>Cathleen C. Cavell</td><td>2028</td></tr>
            <tr><td>Susan Helms Daley</td><td>2028</td></tr>
            <tr><td>Sarah Ericsson</td><td>2026</td></tr>
            <tr><td>Amy R. Evenson</td><td>2026</td></tr>
            <tr><td>Neil R. Gordon</td><td>2027</td></tr>
            <tr><td>Carol B. Hillman</td><td>2026</td></tr>
            <tr><td>Katherine A Ingraham</td><td>2027</td></tr>
            <tr><td>Bradford Kimball</td><td>2028</td></tr>
            <tr><td>Louise King</td><td>2027</td></tr>
            <tr><td>Sean M. Lynn-Jones</td><td>2028</td></tr>
            <tr><td>Sarah Moghtader</td><td>2027</td></tr>
            <tr><td>Bettina Neuefeind</td><td>2026</td></tr>
            <tr><td>Robert Schoen</td><td>2027</td></tr>
          </tbody>
        </table>
      </section>
    </main>

    <footer class="site-footer">
      <p>This page intentionally omits private contact details from the source spreadsheet.</p>
    </footer>
  </body>
</html>
```

- [ ] **Step 4: Run the validation script**

Run: `python3 tests/check_site.py`

Expected: FAIL because `election-information.html`, `links.html`, and `README.md` still do not exist

- [ ] **Step 5: Commit the TMM page**

```bash
git add tmms.html
git commit -m "feat: publish precinct 1 town meeting members"
```

## Task 5: Build the Election Information Page

**Files:**
- Create: `/Users/robschoen/Dropbox/CC/P1/election-information.html`

- [ ] **Step 1: Expand the validation script to check the election image and civic links**

```python
PAGE_NEEDLES["election-information.html"] = [
    "Election Information",
    "43 Hawes Street",
    "Where Do I Vote",
    "Town Clerk",
    "assets/P1 election info.png",
]
```

- [ ] **Step 2: Run the validation script to verify the election page check fails**

Run: `python3 tests/check_site.py`

Expected: FAIL because `election-information.html` does not exist yet

- [ ] **Step 3: Create the election information page**

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Election Information | Brookline Precinct 1</title>
    <meta
      name="description"
      content="Voting and election information for Brookline Precinct 1."
    />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Source+Sans+3:wght@400;600;700&display=swap"
      rel="stylesheet"
    />
    <link rel="stylesheet" href="styles.css" />
    <script src="script.js" defer></script>
  </head>
  <body>
    <header class="site-header">
      <div class="site-header__inner">
        <a class="site-brand" href="index.html">
          <span class="site-brand__eyebrow">Brookline, Massachusetts</span>
          <span class="site-brand__name">Precinct 1</span>
        </a>
        <button class="menu-toggle" type="button" data-menu-toggle aria-expanded="false" aria-controls="site-nav">Menu</button>
        <nav class="site-nav" id="site-nav" data-site-nav aria-label="Primary">
          <a data-nav-link href="index.html">Welcome</a>
          <a data-nav-link href="tmms.html">TMMs P1</a>
          <a data-nav-link href="election-information.html">Election Information</a>
          <a data-nav-link href="about.html">About Precinct 1</a>
          <a data-nav-link href="warrant-may-2026.html">May 2026 Warrant</a>
          <a data-nav-link href="events.html">P1 Events</a>
          <a data-nav-link href="links.html">Links</a>
        </nav>
      </div>
    </header>

    <main>
      <section class="page-hero">
        <div class="page-hero__copy">
          <p class="site-brand__eyebrow">Voting information</p>
          <h1>Election Information</h1>
          <p>
            This page is a practical guide to voting in Brookline Precinct 1.
            For the latest deadlines, ballots, and election notices, check the
            Town Clerk and Massachusetts election resources linked below.
          </p>
        </div>
      </section>

      <section class="page-section">
        <div class="quick-facts">
          <article class="fact-panel">
            <h2>Polling location</h2>
            <p>Precinct 1 votes at <strong>43 Hawes Street</strong>.</p>
          </article>
          <article class="fact-panel">
            <h2>Where do I vote?</h2>
            <p>
              Use the Massachusetts lookup tool to confirm your registration,
              precinct, and polling location.
            </p>
            <p>
              <a class="button-link" href="https://www.sec.state.ma.us/WhereDoIVoteMA">Where Do I Vote</a>
            </p>
          </article>
        </div>
      </section>

      <section class="page-section">
        <h2 class="section-title">Voting Resources</h2>
        <div class="card-grid">
          <article class="card">
            <h3>Town Clerk</h3>
            <p>Check Brookline election notices, sample ballots, and local filing information.</p>
            <a href="https://www.brooklinema.gov/">Visit the Town Clerk resources</a>
          </article>
          <article class="card">
            <h3>Vote by mail and registration</h3>
            <p>Use Massachusetts election resources for registration and vote-by-mail guidance.</p>
            <a href="https://www.sec.state.ma.us/">Visit Massachusetts election resources</a>
          </article>
        </div>
      </section>

      <section class="page-section">
        <h2 class="section-title">Precinct 1 voting reference</h2>
        <div class="card">
          <img
            src="assets/P1 election info.png"
            alt="Precinct 1 election information reference graphic."
          />
        </div>
      </section>
    </main>

    <footer class="site-footer">
      <p>Always confirm dates and official election notices through state and town election sources.</p>
    </footer>
  </body>
</html>
```

- [ ] **Step 4: Run the validation script**

Run: `python3 tests/check_site.py`

Expected: FAIL because `links.html` and `README.md` still do not exist

- [ ] **Step 5: Commit the election page**

```bash
git add election-information.html
git commit -m "feat: add precinct 1 election information page"
```

## Task 6: Build the Links Directory and Project README

**Files:**
- Create: `/Users/robschoen/Dropbox/CC/P1/links.html`
- Create: `/Users/robschoen/Dropbox/CC/P1/README.md`

- [ ] **Step 1: Expand the validation script to check the full links directory and README**

```python
PAGE_NEEDLES["links.html"] = [
    "Brookline PAX",
    "Brookline By Design",
    "Brookline For Everyone",
    "Biking Brookline",
    "Brookline for Responsible Government",
    "Brookline Equity Coalition",
    "League of Women Voters of Brookline",
    "Town Meeting Analyzer",
    "brookline.info",
    "Budget Central",
    "Town Agendas and Meetings",
    "Brookline News",
    "FY2027 Financial Plan",
    "Town Organization chart",
    "Open Checkbook",
    "School Budget",
    "Brookline Town Meeting - current files",
    "Brookline Town Meeting - older files",
]

README_NEEDLES = [
    "GitHub Pages",
    "index.html",
    "assets/",
]
```

```python
def main() -> None:
    for path_str in REQUIRED_FILES:
        assert (ROOT / path_str).exists(), f"Missing file: {path_str}"

    for page, needles in PAGE_NEEDLES.items():
        html = read_text(page)
        for needle in needles:
            assert needle in html, f"{page} is missing: {needle}"

    readme = read_text("README.md")
    for needle in README_NEEDLES:
        assert needle in readme, f"README.md is missing: {needle}"

    tmms_html = read_text("tmms.html")
    for forbidden in FORBIDDEN_TMM_STRINGS:
        assert forbidden not in tmms_html, f"Forbidden public detail found in tmms.html: {forbidden}"

    print("All site checks passed.")
```

- [ ] **Step 2: Run the validation script to verify the links and README checks fail**

Run: `python3 tests/check_site.py`

Expected: FAIL because `links.html` and `README.md` do not exist yet

- [ ] **Step 3: Create the links page**

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Links | Brookline Precinct 1</title>
    <meta
      name="description"
      content="Local civic and reference links for Brookline Precinct 1."
    />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Source+Sans+3:wght@400;600;700&display=swap"
      rel="stylesheet"
    />
    <link rel="stylesheet" href="styles.css" />
    <script src="script.js" defer></script>
  </head>
  <body>
    <header class="site-header">
      <div class="site-header__inner">
        <a class="site-brand" href="index.html">
          <span class="site-brand__eyebrow">Brookline, Massachusetts</span>
          <span class="site-brand__name">Precinct 1</span>
        </a>
        <button class="menu-toggle" type="button" data-menu-toggle aria-expanded="false" aria-controls="site-nav">Menu</button>
        <nav class="site-nav" id="site-nav" data-site-nav aria-label="Primary">
          <a data-nav-link href="index.html">Welcome</a>
          <a data-nav-link href="tmms.html">TMMs P1</a>
          <a data-nav-link href="election-information.html">Election Information</a>
          <a data-nav-link href="about.html">About Precinct 1</a>
          <a data-nav-link href="warrant-may-2026.html">May 2026 Warrant</a>
          <a data-nav-link href="events.html">P1 Events</a>
          <a data-nav-link href="links.html">Links</a>
        </nav>
      </div>
    </header>

    <main>
      <section class="page-hero">
        <div class="page-hero__copy">
          <p class="site-brand__eyebrow">Civic reference directory</p>
          <h1>Links</h1>
          <p>
            A curated set of Brookline civic, election, budget, and town meeting
            resources for Precinct 1 residents.
          </p>
        </div>
      </section>

      <section class="page-section">
        <div class="directory-grid">
          <section class="directory-group">
            <h2>Local civic and community groups</h2>
            <ul>
              <li><a href="https://brooklinepax.wordpress.com/">Brookline PAX</a></li>
              <li><a href="https://www.brooklinebydesign.com/">Brookline By Design</a></li>
              <li><a href="https://www.brooklineforeveryone.com/">Brookline For Everyone</a></li>
              <li><a href="https://www.bikingbrookline.org/">Biking Brookline</a></li>
              <li><a href="https://www.responsiblebrookline.com/">Brookline for Responsible Government</a></li>
              <li><a href="https://www.brooklineequitycoalition.org/">Brookline Equity Coalition</a></li>
              <li><a href="https://my.lwv.org/massachusetts/brookline">League of Women Voters of Brookline</a></li>
            </ul>
          </section>

          <section class="directory-group">
            <h2>Voting and election resources</h2>
            <ul>
              <li><a href="https://millxing.github.io/TM/TMMvotes.html">Town Meeting Analyzer</a></li>
              <li><a href="https://brookline.info/">brookline.info</a></li>
              <li><a href="https://www.sec.state.ma.us/WhereDoIVoteMA">Where to Vote</a></li>
            </ul>
          </section>

          <section class="directory-group">
            <h2>Budget, finance, and government reference</h2>
            <ul>
              <li><a href="https://www.brooklinema.gov/851/Budget-Central">Budget Central</a></li>
              <li><a href="https://stories.opengov.com/brooklinema/5cf061e0-65c6-428e-be0f-fee5a4848e8f/published/mpRiIYj5M?currentPageId=TOC">FY2027 Financial Plan</a></li>
              <li><a href="https://www.brooklinema.gov/DocumentCenter/View/3327/Town-of-Brookline-Organizational-Chart?bidId=">Town Organization chart</a></li>
              <li><a href="https://stories.opengov.com/brooklinema/published/3gE577bjs">Open Checkbook</a></li>
              <li><a href="https://brooklinema.portal.civicclerk.com/event/14954/files/attachment/10857">School Budget</a></li>
            </ul>
          </section>

          <section class="directory-group">
            <h2>Town meeting materials and local news</h2>
            <ul>
              <li><a href="https://brooklinema.portal.civicclerk.com/">Town Agendas and Meetings</a></li>
              <li><a href="https://brookline.news/">Brookline News</a></li>
              <li><a href="https://www.brooklinema.gov/3599/Current-Town-Meeting-Files">Brookline Town Meeting - current files</a></li>
              <li><a href="https://www.brooklinema.gov/3884/Older-Town-Meeting-Files">Brookline Town Meeting - older files</a></li>
            </ul>
          </section>
        </div>
      </section>
    </main>

    <footer class="site-footer">
      <p>External links are provided as a convenience and should be checked for the latest official updates.</p>
    </footer>
  </body>
</html>
```

- [ ] **Step 4: Create the README**

```md
# Brookline Precinct 1 Website

This repository contains a minimal static website for Brookline, Massachusetts Precinct 1.

## Files

- `index.html`: Welcome page with map links and quick access cards
- `tmms.html`: Public Town Meeting Member names and term expiration years
- `election-information.html`: Precinct 1 voting location and election resources
- `about.html`: Placeholder page for precinct background
- `warrant-may-2026.html`: Placeholder page for warrant information
- `events.html`: Placeholder page for precinct events
- `links.html`: Curated civic and reference links
- `styles.css`: Shared design system and page styling
- `script.js`: Mobile navigation toggle and active link highlighting
- `assets/`: Source files and PDFs used by the site

## GitHub Pages

To publish with GitHub Pages:

1. Push these files to a GitHub repository.
2. In the repository settings, enable GitHub Pages from the default branch root.
3. Confirm that `index.html` is at the repository root.

## Updating Content

- Update page copy directly in the HTML files.
- Keep shared visual changes in `styles.css`.
- Keep JavaScript minimal in `script.js`.
- Do not publish private contact information from `assets/P1_TMMs.xlsx`.
```

- [ ] **Step 5: Run the full validation script**

Run: `python3 tests/check_site.py`

Expected: PASS with `All site checks passed.`

- [ ] **Step 6: Manually smoke-test the site locally**

Run: `python3 -m http.server 8000`

Expected: Local server starts and each page loads in a browser with working navigation, readable mobile layout, and accessible map and image assets

- [ ] **Step 7: Commit the links page and documentation**

```bash
git add links.html README.md tests/check_site.py
git commit -m "feat: add civic links directory and project docs"
```

## Self-Review

- Spec coverage check:
  - Welcome page with map access is covered in Task 3.
  - TMM public list and privacy requirement are covered in Task 4 and the forbidden-string assertions in Task 1.
  - Election Information page with `43 Hawes Street` and the image asset is covered in Task 5.
  - Placeholder pages are covered in Task 2.
  - Links page and grouped resource directory are covered in Task 6.
  - Shared civic visual system, responsive navigation, and no-build hosting are covered in Task 2 and README guidance in Task 6.
- Placeholder scan:
  - Removed vague references to future implementation by naming exact files, commands, strings, and content.
- Type and naming consistency:
  - Navigation labels, file names, and validation script keys match the planned page files.
