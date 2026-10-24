# AccessMap — Accessible Places, Clearer Journeys (IC26-04-04)

**MoHUA Harmonised Guidelines 2021 & RPwD Act 2016 Aligned Accessible Route Planning, Barrier Reporting & Moderation Platform**

AccessMap transforms urban pedestrian navigation by treating accessibility as an indispensable route requirement rather than an afterthought. Built for the **IC26-04-04 AccessMap Challenge**, the platform bridges citizen reporting, multi-criteria accessible routing, and official government audit workflows under the Ministry of Housing and Urban Affairs (MoHUA) and Department of Empowerment of Persons with Disabilities (DEPwD).

---

## 🌟 Key Features & Capabilities

### 1. Curated Small-Area Demonstration Precincts (Field-Verified)
- **AIIMS Metro & Hospital Precinct (New Delhi):** Complete multi-modal transit hub with metro lifts, step-free concourse access, signalized pelican crossings with acoustic signals, dropped kerbs (lip $\le$ 10mm), tactile paving, and universal approach ramps (gradient 1:15).
- **IIT Delhi Campus Precinct (Hauz Khas):** Academic mobility corridor with universal administrative ramp access, Senate Hall flight barrier (18 steps), central library accessible ground lift, and student walkway network.
- **Bengaluru MG Road Transit Hub:** Commercial pedestrianised corridor along Church Street, metro concourse elevators, and dropped kerbs.
- **Full Offline Readiness:** All demo precincts are 100% interactive offline in direct browser file mode (`file:///`) as well as via localhost, complete with embedded pedestrian networks and verified audit features.

### 2. Multi-Criteria Accessible Routing Engine
- **Mobility Profiles:**
  - ♿ **Step-Free / Wheelchair:** Strictly avoids all steps and stairs; penalizes steep gradients ($> 1:12$ / $8.33\%$); requires minimum clear width $\ge 1200\text{ mm}$; avoids high-vibration surfaces like rough cobbles or unpaved gravel.
  - 🦯 **Tactile / Vision Guided:** Strongly prioritizes Tactile Ground Surface Indicators (TGSI guiding bars and warning blisters) and signalized crossings with audible beepers.
  - 🚶 **Easy Walk / Senior Friendly:** Minimizes stair flights and steep inclines ($> 5\%$), directing pedestrians to shaded resting corridors.
  - ⚡ **Standard Pedestrian:** Baseline shortest-distance walking route.
- **Side-by-Side Route Comparison:**
  - Simultaneously computes and visualizes the **Accessible Step-Free Route** (emerald solid line) versus the **Standard Direct Route** (crimson/dashed line).
  - Highlights exact hazards avoided (e.g. *"48 stairs avoided · Max slope 6.8% · 100% Step-Free"*).
- **Turn-by-Turn Accessible Directions & Audio Speech Synthesis:**
  - Granular, accessible step-by-step instructions specifying path width, surface material, ramp slope ratios, and handrail status.
  - Built-in text-to-speech engine (**Read Aloud**) providing spoken turn guidance for low-vision users.
  - Printable accessible route sheets and one-click GeoJSON export for GPS devices and GIS platforms.

### 3. Barrier Reporting & Official Moderation Workflow
- **In-Field Barrier Reporting:**
  - Citizens and auditors can drop a pin anywhere on the map to record physical barriers: steps without ramps, broken dropped kerbs ($> 15\text{ mm}$ lip), footpath obstructions, steep slopes, elevator outages, or construction blockages.
  - Records physical measurements: measured slope (%), clear width (mm), step count, and reporter role.
- **Moderation Desk (Sugamya Bharat / MoHUA Integration):**
  - Dedicated auditor dashboard showing **Pending Review**, **Field Verified**, and **Resolved** barriers.
  - **Verify Report:** Upgrades confidence from Medium to High, records official inspector credentials and timestamp, and publishes to the live routing engine.
  - **Mark as Resolved:** Dynamically clears barriers when repaired (e.g., ramp installed or obstruction removed), instantly unlocking previously blocked pathways.
  - **Data Export:** Export all records to standardized GeoJSON and CSV for municipal smart city dashboards.

### 4. Harmonised Guidelines 2021 (India) Compliance Checker
- Built-in digital inspector grounded in MoHUA's *Harmonised Guidelines and Standards for Universal Accessibility in India (2021)*:
  - **Ramps (§ 4.3):** Max gradient $1:12$ ($8.33\%$), min clear width $1200\text{ mm}$, continuous dual handrails at $750\text{ mm}$ and $900\text{ mm}$.
  - **Footpaths (§ 4.1):** Min clear walking width $1500\text{ mm}$, cross-slope $\le 2\%$, firm non-slip surface.
  - **Kerb Ramps (§ 4.2):** Max slope $1:10$ ($10\%$), flush lip transition $\le 15\text{ mm}$, $300\text{ mm}$ blister tactile warning band.
  - **TGSI (§ 4.5):** Directional bars along path of travel, hazard blisters at decision points.

### 5. Web Accessibility (WCAG 2.2 AAA Ready)
- **High Contrast Theme:** Dedicated high-contrast toggle for visually impaired and low-vision users.
- **Font Scaling:** One-click cycling between Standard, Large, and Extra Large typography.
- **Accessible Table/List View:** Toggle from map view to accessible tabular list with screen-reader live regions.
- **Keyboard Navigation:** Full keyboard shortcut and skip-link support.

---

## 🚀 How to Run Locally

### Option A: Windows PowerShell Launcher (Recommended)
Right-click `Start-AccessMap.ps1` and choose **Run with PowerShell**, or execute:
```powershell
.\Start-AccessMap.ps1
```
This automatically finds an available local port, starts a lightweight server, and launches your default browser at `http://127.0.0.1:<port>/`.

### Option B: Python Local Server
From the project folder, run:
```powershell
python -m http.server 8000
```
Then navigate to: [http://localhost:8000](http://localhost:8000)

### Option C: Direct File Opening
You can open `index.html` directly in any modern browser (`file:///.../index.html`). All verified demo precincts, vector networks, routing engines, compliance scorecards, and moderation workflows function seamlessly offline!

---

## 📁 Project Structure

```
d:\conclave\accessmap-site\
├── index.html            # Semantic accessible DOM, dialogs, tabs & controls
├── styles.css            # Responsive layout, High Contrast mode, accessible tokens
├── app.js                # A* Graph routing engine, Leaflet layers, moderation desk
├── Start-AccessMap.ps1   # PowerShell launcher for instant localhost startup
├── map-preview.svg       # Bundled illustrative vector base
└── README.md             # Project documentation & compliance benchmarks
```

---

## 🎯 Quick Demonstration Walkthrough (For Evaluators)

1. **Compare Step-Free vs Stairs:**
   - Under the precinct bar, click **"Compare Step-Free vs Stairs"**.
   - Notice how the platform routes from **Metro Gate 2 (Elevator)** to **Main OPD Entrance B (Universal Ramp)** avoiding 48 stairs, displaying the standard route in dashed gray and the step-free route in solid emerald green.
2. **Test Active Barrier Detour:**
   - Click **"Test Barrier Detour"**.
   - The routing engine automatically detects the reported construction blockage on the central walkway and routes via the tactile Ring Road corridor.
3. **Audit & Resolve a Barrier:**
   - Switch to the **Audits** tab.
   - Click **"Mark Resolved"** on the construction blockage card.
   - Switch back to **Explore** and re-run the route — the pathway is instantly reopened!
4. **Inspect Harmonised Guidelines Compliance:**
   - Switch to the **Standards** tab and click **"Inspect Selected Feature"** to view the MoHUA clause audit card with physical tolerances.
5. **Listen to Spoken Directions:**
   - Switch to the **Directions** tab and click **"Read Aloud"** to hear speech synthesis guidance for low-vision commuters.

---

## 📜 Regulatory Alignment
- **Ministry of Housing and Urban Affairs (MoHUA):** Harmonised Guidelines for Universal Accessibility in India (2021).
- **Department of Empowerment of Persons with Disabilities (DEPwD):** Rights of Persons with Disabilities (RPwD) Act 2016 (Sections 40–46).
- **Accessible India Campaign (Sugamya Bharat Abhiyan):** Built Environment and Transport Standards.
- **W3C:** Web Content Accessibility Guidelines (WCAG) 2.2 AA / AAA.
