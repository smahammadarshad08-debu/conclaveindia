# Developer Onboarding & Local Setup Handbook

Welcome to the **AccessMap India** development team! Follow this guide to set up your local environment, test changes, and submit pull requests.

---

## 1. Prerequisites

- **Python 3.8+** (installed and added to system `PATH`)
- **Git 2.25+**
- Modern Chromium or WebKit-based browser (Chrome, Edge, Safari, Firefox)

---

## 2. Quick Setup

```bash
# 1. Clone the repository
git clone https://github.com/smahammadarshad08-debu/conclaveindia.git
cd conclaveindia

# 2. Start the local server
python server.py

# 3. Open in your browser
# URL: http://localhost:8000
```

---

## 3. Directory Structure

```text
├── .github/              # GitHub Actions workflows & templates
├── accessmap-site/       # Core web application assets
│   ├── index.html        # Main HTML5 application shell & HUD
│   ├── styles.css        # Responsive CSS & mobile bottom sheet
│   ├── app.js            # Leaflet GIS, OSRM routing, live voice
│   └── manifest.json     # PWA manifest
├── docs/                 # Architectural & compliance documentation
├── tests/                # Automated test scripts & verification suites
├── server.py             # Zero-dependency HTTP static server
└── README.md             # Project overview & quickstart
```
