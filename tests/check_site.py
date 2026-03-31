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
        "Brookline's Precinct 1",
        "P1 Town Meeting Members",
        "P1 Voting Location",
        "May 5 Election",
        "Annual Town Meeting Warrant",
        "Precinct 1 Events and News",
        "Links and Resources",
    ],
    "tmms.html": [
        "Town Meeting Members",
        "Ana Albuquerque",
        "Rui Albuquerque",
        "Cathleen C. Cavell",
        "Susan Helms Daley",
        "Robert Schoen",
        "Term expires",
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
    ],
    "election-information.html": [
        "Precinct 1 Voting Location",
        "43 Hawes Street",
        "Where Do I Vote",
        "assets/P1 election info.png",
    ],
    "about.html": [
        "About Precinct 1",
        "Cottage Farm is also a Local Historic District",
        "Hall's Pond",
        "Amory Woods",
        "Boston University has a substantial footprint in the precinct",
        "assets/IMG_3876.png",
    ],
    "warrant-may-2026.html": [
        "Annual Town Meeting Warrant",
        "Current Town Meeting Files",
        "assets/warrant-2026-atm.pdf",
    ],
    "events.html": ["Precinct 1 Events", "P1 Events"],
    "links.html": [
        "Brookline PAX",
        "Brookline By Design",
        "Brookline For Everyone",
        "Biking Brookline",
        "Brookline for Responsible Government",
        "Brookline Equity Coalition",
        "League of Women Voters of Brookline",
        "Town Meeting Analyzer",
        "Brookline.info",
        "Where to Vote",
        "Town Clerk's office",
        "Brookline elections and voting",
        "Budget Central",
        "Town Agendas and Meetings",
        "Brookline News",
        "Town Meeting Members List",
        "Town Meeting Resources",
        "FY2027 Financial Plan",
        "Town Organization chart",
        "Open Checkbook",
        "School Budget",
        "Brookline Town Meeting - current files",
        "Brookline Town Meeting - older files",
    ],
    "README.md": [
        "GitHub Pages",
        "index.html",
        "assets/",
    ],
}

FORBIDDEN_TMM_STRINGS = [
    "mailto:",
    "tel:",
    "24 Euston Street",
    "79 Carlton Street",
    "albuquea@bu.edu",
    "rui.albuquerque@bc.edu",
    "cathleencavell@gmail.com",
    "susanhelmsdaley@gmail.com",
    "sarah_harpist@yahoo.com",
    "amyrevenson@gmail.com",
    "neil@nrgordon.com",
    "sarah.hillman@example.com",
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
