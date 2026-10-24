# Contributing to AccessMap India

Thank you for your interest in contributing to **AccessMap India**! Our mission is to provide high-precision, step-free, barrier-free, and universally accessible pedestrian navigation for Indian urban precincts in compliance with the **MoHUA Harmonised Guidelines and Standards for Universal Accessibility in India (2021)**.

---

## Code of Conduct

All contributors and participants are expected to adhere to our [Code of Conduct](CODE_OF_CONDUCT.md). Please treat all community members with empathy, respect, and constructive collaboration.

---

## Ways to Contribute

1. **Accessibility Audits & Data Curation:**
   - Field-verify infrastructure in your precinct (kerb ramp slopes, tactile guiding tiles, entrance clearances, stair flights).
   - Submit new precinct datasets in `PRECINCTS` format ([app.js](accessmap-site/app.js)).
2. **Feature Development:**
   - Improve routing algorithms, offline capabilities, or assistive device integrations.
   - Enhance the Moderation Desk and barrier verification workflows.
3. **Bug Reports & UI/UX Feedback:**
   - Report cross-device styling issues, screen reader accessibility gaps (ARIA), or touch target improvements.
4. **Documentation & Standards Compliance:**
   - Expand references to MoHUA Harmonised Guidelines 2021 clauses.

---

## Local Development Workflow

### Prerequisites
* Python 3.9+ (or any static HTTP server)
* Modern web browser (Chrome, Edge, Firefox, Safari)
* Git

### Step-by-Step Setup
1. **Fork and Clone the Repository:**
   ```bash
   git clone https://github.com/smahammadarshad08-debu/conclaveindia.git
   cd conclaveindia
   ```
2. **Start the Local Development Server:**
   ```bash
   python server.py
   ```
3. **Open the Application:**
   Navigate in your browser to:
   ```
   http://localhost:10000/
   ```
   *(Or on Windows, double-click `Start-AccessMap.bat`)*

---

## Harmonised Guidelines 2021 (HG-2021) Standards Reference

When adding or editing accessibility infrastructure data, ensure values adhere to the following MoHUA clauses:

| Feature | HG-2021 Clause | Mandatory Requirement |
| :--- | :--- | :--- |
| **Walkway Width** | § 4.1 | $\ge 1200\text{ mm}$ (clear continuous width), $1800\text{ mm}$ preferred |
| **Ramp Slope** | § 4.3 | Max $1:12$ ($8.33\%$), $1:15$ preferred for long spans |
| **Kerb Ramps** | § 4.2 | Flush lip with road surface ($\le 15\text{ mm}$) |
| **Stair Warning** | § 4.4 | Tactile warning strip $300\text{ mm}$ before top and bottom landings |
| **Tactile Guiding** | § 4.5 | Continuous sinusoidal guiding tiles leading to key entrances |
| **Doorway Width** | § 5.1 | Clear opening $\ge 900\text{ mm}$ |

---

## Pull Request Guidelines

1. **Branch Naming:**
   - `feature/your-feature-name`
   - `fix/issue-description`
   - `data/precinct-name-audit`
2. **Commit Messages:**
   Follow Conventional Commits:
   - `feat(routing): add elevation penalty parameter`
   - `fix(layers): prevent viewport shift on category switch`
   - `docs(readme): add architecture sequence diagram`
3. **Testing:**
   - Test on both desktop (width $> 1024\text{px}$) and mobile viewport (width $\le 430\text{px}$).
   - Ensure the Leaflet map and bottom sheet drawer render cleanly without scrollbar leaks or blank screens.
   - Verify all 6 category switches filter correctly.

---

## Questions or Need Help?

Open an issue on GitHub using our [Issue Templates](.github/ISSUE_TEMPLATE/) or reach out via the repository discussions.
