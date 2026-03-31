# Precinct 1 Website Design

Date: 2026-03-30

## Overview

This project is a minimal static website for Brookline, Massachusetts Precinct 1. The site will be hosted on GitHub Pages and built with hand-written HTML, CSS, and a small amount of JavaScript. Its purpose is to provide clear, non-partisan civic information for residents, with emphasis on election logistics, precinct maps, Town Meeting Member information, and useful local links.

The site should feel official, calm, and trustworthy rather than campaign-oriented or activist-branded. It should be easy to scan on desktop and mobile, simple to maintain, and structured so future copy can be added page by page without introducing a build step.

## Goals

- Present Brookline Precinct 1 information in a neutral, civic tone.
- Make election information and precinct maps easy to find from the homepage.
- Publish the current Precinct 1 Town Meeting Members using only names and term expiration years.
- Provide placeholders for pages whose content will be filled in later.
- Keep the implementation compatible with no-build GitHub Pages hosting.

## Non-Goals

- No CMS, database, or build pipeline.
- No publication of Town Meeting Member addresses, email addresses, or phone numbers from the source spreadsheet.
- No partisan framing, endorsements, or campaign messaging.
- No advanced interactive map tooling.

## Audience

The primary audience is Brookline residents looking for practical Precinct 1 information, especially voters and residents who want a simple directory of town-meeting-related resources. Secondary audiences include Town Meeting Members and residents trying to understand precinct boundaries or find town reference materials.

## Site Structure

The site will use a simple top-level navigation with these pages:

- `Welcome`
- `TMMs P1`
- `Election Information`
- `About Precinct 1`
- `May 2026 Warrant`
- `P1 Events`
- `Links`

This keeps the information architecture shallow and predictable. Detail pages for individual Town Meeting Members or standalone map pages are intentionally out of scope for the first version.

## Page Requirements

### Welcome

The homepage is the primary entry point and should lead with a short statement that this is a non-partisan informational site for Brookline Precinct 1. The first screen should surface the two most common user paths:

- Election information
- Precinct maps

The page should then preview:

- Town Meeting Members
- Events
- Links

The Welcome page should include access to both precinct map assets already in the repository, presented with clear labels and obvious open or download actions.

### TMMs P1

This page should include:

- A short explanation of what Town Meeting Members are in plain language.
- A clean list or table of the 15 Precinct 1 Town Meeting Members.
- One column or label for each member's term expiration year.

The source data comes from `/assets/P1_TMMs.xlsx`, but only names and term expiration years should be published.

### Election Information

This page should be modeled structurally on the practical flow of the Brookline Precinct 6 election page while keeping original writing and design. The content should be ordered as:

1. Brief election overview
2. Polling location
3. Voting logistics and where-to-vote guidance
4. Related election resources

Known required content:

- Precinct 1 voting location: `43 Hawes Street`
- Supporting image asset: `/assets/P1 election info.png`
- Link to the Massachusetts "Where Do I Vote" lookup

The page should prioritize useful facts over narrative copy and should be easy to update for future election cycles.

### About Precinct 1

This page should exist in the first version as a deliberate placeholder with a short note that expanded precinct background content will be added later.

### May 2026 Warrant

This page should exist in the first version as a deliberate placeholder with a short note that warrant-related content will be added later.

### P1 Events

This page should exist in the first version as a deliberate placeholder with a short note that precinct event information will be added later.

### Links

This page should present the provided resources in a clean, scannable directory format. Links should be grouped in a way that reduces cognitive load, for example:

- Local civic/community groups
- Voting and election resources
- Budget, finance, and government reference
- Town meeting materials and agendas
- Local news

The initial links list should include the resources provided by the user, including `brookline.info`, which should be rendered as a plain link once its final URL is confirmed in implementation.

## Visual Direction

The visual style should communicate "small civic information hub" rather than "campaign site" or "generic template." The design should follow these principles:

- Strong hierarchy on the homepage so the first actions are obvious.
- Restrained accent usage so emphasis remains meaningful.
- High readability and contrast.
- Quiet, intentional composition with clear grouping.
- Familiar navigation and controls.

Recommended visual language:

- Light warm-neutral background
- Deep navy or slate for primary text
- Muted green accent for links, highlights, and key actions
- Serif page headings paired with a clean sans-serif for body text and navigation

The design should feel formal enough to be trustworthy, but still welcoming and readable on phones.

## Interaction and Behavior

JavaScript should be minimal and only used where it improves usability. Acceptable uses include:

- Mobile navigation toggle
- Active navigation state
- Minor enhancements for asset presentation if needed

The site should not depend on JavaScript for basic reading or navigation.

## Accessibility

The first version should use semantic HTML and accessible defaults:

- Proper heading hierarchy
- Keyboard-accessible navigation
- Visible focus states
- Adequate color contrast
- Descriptive link text
- Readable font sizes and spacing

Images and embedded assets should include text context so critical information is not conveyed only visually.

## Content Sources

Existing repository assets to use:

- `/assets/P1_TMMs.xlsx`
- `/assets/P1 election info.png`
- `/assets/Precinct1BWbook_202205201023379661.pdf`
- `/assets/Precinct34x46_202208241152573823.pdf`
- `/assets/GIS-Precinct11x17_202205201122255708.pdf`

Implementation should treat these files as source materials and present them with clearer labeling in the website UI.

## Technical Shape

The first version should be implemented as a multi-page static site with shared styling and lightweight shared JavaScript. Expected files:

- `index.html`
- `tmms.html`
- `election-information.html`
- `about.html`
- `warrant-may-2026.html`
- `events.html`
- `links.html`
- `styles.css`
- `script.js`
- `README.md`

The `README.md` should explain:

- How to publish with GitHub Pages
- Which files contain page content
- Where the source assets live

## Deployment

The site is intended for GitHub Pages hosting with no build step. The implementation should assume static file hosting only.

## Risks and Constraints

- The current folder is not a git repository, so the design spec can be written locally but cannot be committed until git is initialized or the files are moved into an existing repository.
- The election page will need copy that is easy to update as dates change over time.
- The final URL for `brookline.info` should be verified during implementation to avoid a broken link.

## Success Criteria

The first release is successful if:

- A resident can land on the homepage and immediately find election information or precinct maps.
- The site reads as non-partisan and civic rather than promotional.
- The TMM page shows all 15 members with names and term expiration years only.
- The Election Information page clearly states the Precinct 1 polling location at `43 Hawes Street`.
- Placeholder pages feel intentional rather than broken or empty.
- The site works cleanly on desktop and mobile under GitHub Pages static hosting.
